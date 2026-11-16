import json
import os
import requests

# Path to the JSON file that stores IDs of bounties we have already processed
SEEN_FILE = "seen_bounties.json"

# URL to fetch bounty issues – adjust as needed for the repository
BOUNTY_URL = "https://api.github.com/repos/dev-kp-eloper/BountyScout/issues?labels=bounty"


def load_seen() -> set:
    """Load the set of seen bounty IDs from SEEN_FILE.

    Returns an empty set if the file does not exist or is malformed.
    """
    if not os.path.exists(SEEN_FILE):
        return set()
    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data)
    except (json.JSONDecodeError, OSError):
        # If the file is corrupted we start fresh to avoid blocking the scout.
        return set()


def save_seen(seen: set) -> None:
    """Persist the set of seen bounty IDs back to SEEN_FILE.

    The file is written atomically to avoid partial writes.
    """
    tmp_path = SEEN_FILE + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(list(seen), f, indent=2, sort_keys=True)
    os.replace(tmp_path, SEEN_FILE)


def fetch_bounties() -> list:
    """Retrieve the list of bounty issues from GitHub.

    Returns the JSON payload as a list of issue dictionaries.
    """
    response = requests.get(BOUNTY_URL)
    response.raise_for_status()
    return response.json()


def main() -> None:
    seen = load_seen()
    try:
        bounties = fetch_bounties()
    except Exception as exc:
        print(f"Failed to fetch bounties: {exc}")
        return

    new_bounties = []
    for bounty in bounties:
        bounty_id = bounty.get("id")
        if bounty_id is None:
            continue
        if bounty_id not in seen:
            new_bounties.append(bounty)
            seen.add(bounty_id)

    if new_bounties:
        print(f"Found {len(new_bounties)} new bounty(ies):")
        for nb in new_bounties:
            print(f"- #{nb.get('number')} {nb.get('title')}")
        # Here you could add logic to create a summary issue or comment.
    else:
        print("No new bounties found.")

    # Persist the updated set of seen IDs.
    save_seen(seen)


if __name__ == "__main__":
    main()
