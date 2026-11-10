def format_bounty_alert_title(count: int) -> str:
    """Format the bounty alert notification title with correct pluralization."""
    noun = "Opportunity" if count == 1 else "Opportunities"
    return f"🎯 Bounty Alert: {count} New {noun} found"
