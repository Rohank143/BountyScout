import json
import os
import urllib.request
import urllib.parse
import re
from datetime import datetime, timezone

# Configuration
STATE_FILE = "seen_bounties.json"
MAX_COMMENTS = 25 # Filter out overcrowded threads

# GitHub search queries for active bounty opportunities
SEARCH_QUERIES = [
    'is:issue is:open bounty in:title,body sort:updated-desc',
    'is:issue is:open reward bounty sort:updated-desc',
    'is:issue is:open "paid" "PR" "bounty" sort:updated-desc',
    'is:issue is:open "Opire" bounty sort:updated-desc',
]

def load_seen_bounties():
    """Load previously seen bounty URLs from the state file."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return set(data)
        except Exception as e:
            print(f"Error loading state file: {e}")
    return set()

def save_seen_bounties(seen_urls):
    """Save the updated list of seen bounty URLs."""
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(list(seen_urls), f, indent=2)
    except Exception as e:
        print(f"Error saving state file: {e}")

def search_github(query, token=None):
    """Fetch search results from GitHub Issues API."""
    url = f"https://api.github.com/search/issues?{urllib.parse.urlencode({'q': query, 'per_page': 15})}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "MyPersonalBountyScout",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"GitHub Search API Error for query '{query}': {e}")
        return {}

def is_clean_candidate(item):
    """Triage logic to filter out noisy, assigned, closed, or spam tasks."""
    # 1. Skip if already a Pull Request
    if "pull_request" in item:
        return False
    # 2. Skip if already assigned
    if item.get("assignees"):
        return False
    # 3. Skip if thread is overcrowded (highly competitive)
    if int(item.get("comments", 0)) > MAX_COMMENTS:
        return False
    
    title = str(item.get("title", "")).lower()
    body = str(item.get("body", "")).lower()
    
    # 4. Skip cryptocurrency/article writing/spam keywords
    blocklist = [
        "airdrop", "referral", "casino", "gambling", "trading bot", 
        "blog post", "article writing", "tutorial proposal", "content creator"
    ]
    if any(term in title or term in body for term in blocklist):
        return False
        
    return True

def send_telegram_notification(token, chat_id, message):
    """Send a notification message via Telegram Bot API."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "MyPersonalBountyScout"
    }
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"Telegram API Error: {e}")
        return None

def main():
    github_token = os.environ.get("GITHUB_TOKEN")
    telegram_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    seen_bounties = load_seen_bounties()
    new_bounties = []

    for query in SEARCH_QUERIES:
        result = search_github(query, token=github_token)
        items = result.get("items", [])
        for item in items:
            if not is_clean_candidate(item):
                continue
            
            url = item.get("html_url")
            if not url or url in seen_bounties:
                continue

            # Extract repository name from url or repository_url
            repo_url = item.get("repository_url", "")
            repo_name = "/".join(repo_url.split("/")[-2:]) if repo_url else "Unknown Repository"
            
            bounty_info = {
                "title": item.get("title"),
                "url": url,
                "repository": repo_name,
                "comments": item.get("comments", 0),
                "updated_at": item.get("updated_at")
            }
            new_bounties.append(bounty_info)
            seen_bounties.add(url)

    if new_bounties:
        # Deduplicate by URL just in case multiple queries returned the same issue
        unique_bounties = {}
        for b in new_bounties:
            unique_bounties[b["url"]] = b
        
        bounty_list = list(unique_bounties.values())
        
        scan_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        msg_lines = [
            f"🎯 *Bounty Alert: {len(bounty_list)} New Opportunity(ies) found*",
            f"",
            f"*Scan Time:* {scan_time}",
            f""
        ]
        
        for idx, b in enumerate(bounty_list, 1):
            msg_lines.append(f"#### {idx}. [{b['title']}]({b['url']})")
            msg_lines.append(f"- **Repository:** [{b['repository']}](https://github.com/{b['repository']})")
            msg_lines.append(f"- **Comments:** {b['comments']}")
            msg_lines.append(f"- **Last Updated:** {b['updated_at']}")
            msg_lines.append("")

        message = "\n".join(msg_lines)
        
        if telegram_token and telegram_chat_id:
            send_telegram_notification(telegram_token, telegram_chat_id, message)
        else:
            print("Telegram credentials not found. Printing notification message:")
            print(message)
            
        save_seen_bounties(seen_bounties)
    else:
        print("No new clean bounty opportunities found during this scan.")

if __name__ == "__main__":
    main()