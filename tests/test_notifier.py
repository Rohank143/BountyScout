import pytest
from src.notifier import format_bounty_alert_title, generate_bounty_alert


def test_format_bounty_alert_title_plural():
    title = format_bounty_alert_title(14)
    assert title == "🎯 Bounty Alert: 14 New Opportunities found"
    assert "Opportunityies" not in title


def test_format_bounty_alert_title_singular():
    title = format_bounty_alert_title(1)
    assert title == "🎯 Bounty Alert: 1 New Opportunity found"


def test_format_bounty_alert_title_zero():
    title = format_bounty_alert_title(0)
    assert title == "🎯 Bounty Alert: 0 New Opportunities found"


def test_generate_bounty_alert():
    sample_bounties = [{"id": i, "title": f"Bounty {i}"} for i in range(14)]
    payload = generate_bounty_alert(sample_bounties)
    
    assert payload["title"] == "🎯 Bounty Alert: 14 New Opportunities found"
    assert payload["count"] == 14
    assert len(payload["items"]) == 14
