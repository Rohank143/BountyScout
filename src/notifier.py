"""Notifier module for BountyScout alert generation and dispatch."""

from typing import List, Dict, Any


def format_bounty_alert_title(count: int) -> str:
    """Format the bounty alert notification title with correct pluralization.

    Args:
        count: The number of new bounty opportunities found.

    Returns:
        Formatted alert title string.
    """
    opportunity_text = "Opportunity" if count == 1 else "Opportunities"
    return f"🎯 Bounty Alert: {count} New {opportunity_text} found"


def generate_bounty_alert(opportunities: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate notification payload for a set of discovered bounty opportunities.

    Args:
        opportunities: List of bounty opportunity dictionaries.

    Returns:
        Notification alert dictionary containing title and body payload.
    """
    count = len(opportunities)
    title = format_bounty_alert_title(count)
    
    return {
        "title": title,
        "count": count,
        "items": opportunities,
    }
