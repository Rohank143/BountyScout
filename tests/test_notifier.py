import pytest
from bountyscout.notifier import format_bounty_alert_title

def test_format_bounty_alert_title_plural():
    assert format_bounty_alert_title(13) == "🎯 Bounty Alert: 13 New Opportunities found"

def test_format_bounty_alert_title_singular():
    assert format_bounty_alert_title(1) == "🎯 Bounty Alert: 1 New Opportunity found"

def test_format_bounty_alert_title_zero():
    assert format_bounty_alert_title(0) == "🎯 Bounty Alert: 0 New Opportunities found"
