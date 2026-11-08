"""Notifier module for formatting bounty alert messages and titles."""

def format_alert_title(count: int) -> str:
    """
    Format the bounty alert title with correct pluralization.

    Args:
        count: Number of new bounty opportunities found.

    Returns:
        Formatted title string.
    """
    word = "Opportunity" if count == 1 else "Opportunities"
    return f"🎯 Bounty Alert: {count} New {word} found"
