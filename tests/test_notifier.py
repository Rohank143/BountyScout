import unittest
from bountyscout.notifier import format_alert_title


class TestNotifier(unittest.TestCase):
    def test_format_alert_title_singular(self):
        self.assertEqual(
            format_alert_title(1),
            "🎯 Bounty Alert: 1 New Opportunity found"
        )

    def test_format_alert_title_plural(self):
        self.assertEqual(
            format_alert_title(14),
            "🎯 Bounty Alert: 14 New Opportunities found"
        )

    def test_format_alert_title_zero(self):
        self.assertEqual(
            format_alert_title(0),
            "🎯 Bounty Alert: 0 New Opportunities found"
        )


if __name__ == "__main__":
    unittest.main()
