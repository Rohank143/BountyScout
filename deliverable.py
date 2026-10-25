"""
Patch for Rohank143/BountyScout Issue #12: 🎯 Bounty Alert: 9 New Opportunities found

This module implements a clean, modular solution for detecting and reporting new bounty opportunities.
It includes a BountyOpportunity data class, a BountyScout class for managing opportunities,
and test cases to verify correct behavior.

Constraints:
- Pure Python, no external dependencies.
- No use of subprocess, ctypes, socket, sys.exit, os.system, or eval.

Author: OpenAI Assistant
"""

from typing import List, Dict, Optional
from dataclasses import dataclass, field


@dataclass
class BountyOpportunity:
    """Represents a bounty opportunity."""
    id: int
    title: str
    url: str
    reward_usd: float
    description: Optional[str] = None

    def __str__(self) -> str:
        return f"[{self.id}] {self.title} (${self.reward_usd:.2f}): {self.url}"


class BountyScout:
    """
    Manages bounty opportunities and detects new ones.
    """

    def __init__(self) -> None:
        self.known_opportunities: Dict[int, BountyOpportunity] = {}

    def update_opportunities(self, fetched: List[BountyOpportunity]) -> List[BountyOpportunity]:
        """
        Update the list of known opportunities and return the new ones.

        Args:
            fetched: List of fetched BountyOpportunity objects.

        Returns:
            List of new BountyOpportunity objects not seen before.
        """
        new_opps: List[BountyOpportunity] = []
        for opp in fetched:
            if opp.id not in self.known_opportunities:
                self.known_opportunities[opp.id] = opp
                new_opps.append(opp)
        return new_opps

    def get_known_opportunities(self) -> List[BountyOpportunity]:
        """Returns all known opportunities."""
        return list(self.known_opportunities.values())

    def format_alert(self, new_opps: List[BountyOpportunity]) -> str:
        """
        Format an alert message for new opportunities.

        Args:
            new_opps: List of new BountyOpportunity objects.

        Returns:
            Formatted string alert.
        """
        if not new_opps:
            return "No new bounty opportunities found."
        lines = [
            f"🎯 Bounty Alert: {len(new_opps)} New Opportunit{'y' if len(new_opps)==1 else 'ies'} found"
        ]
        for opp in new_opps:
            lines.append(f"- {opp}")
        return "\n".join(lines)


# --- Test Cases ---

def _test_bounty_scout() -> None:
    scout = BountyScout()

    # Initial fetch
    fetched1 = [
        BountyOpportunity(id=1, title="Fix Security Bug", url="https://example.com/1", reward_usd=100.0),
        BountyOpportunity(id=2, title="Improve Docs", url="https://example.com/2", reward_usd=25.0),
        BountyOpportunity(id=3, title="Add Feature X", url="https://example.com/3", reward_usd=50.0),
    ]
    new1 = scout.update_opportunities(fetched1)
    alert1 = scout.format_alert(new1)
    assert len(new1) == 3, "Should detect all as new on first fetch"
    assert "3 New Opportunities found" in alert1

    # Second fetch with 2 old, 1 new
    fetched2 = [
        BountyOpportunity(id=1, title="Fix Security Bug", url="https://example.com/1", reward_usd=100.0),
        BountyOpportunity(id=2, title="Improve Docs", url="https://example.com/2", reward_usd=25.0),
        BountyOpportunity(id=4, title="Refactor Code", url="https://example.com/4", reward_usd=75.0),
    ]
    new2 = scout.update_opportunities(fetched2)
    alert2 = scout.format_alert(new2)
    assert len(new2) == 1, "Should detect only 1 new opportunity"
    assert "1 New Opportunity found" in alert2 or "1 New Opportunities found" in alert2
    assert "- [4] Refactor Code ($75.00): https://example.com/4" in alert2

    # Third fetch, no new
    fetched3 = [
        BountyOpportunity(id=1, title="Fix Security Bug", url="https://example.com/1", reward_usd=100.0),
        BountyOpportunity(id=2, title="Improve Docs", url="https://example.com/2", reward_usd=25.0),
        BountyOpportunity(id=3, title="Add Feature X", url="https://example.com/3", reward_usd=50.0),
        BountyOpportunity(id=4, title="Refactor Code", url="https://example.com/4", reward_usd=75.0),
    ]
    new3 = scout.update_opportunities(fetched3)
    alert3 = scout.format_alert(new3)
    assert len(new3) == 0, "Should detect no new opportunities"
    assert "No new bounty opportunities found." in alert3

    print("All BountyScout tests passed.")


if __name__ == "__main__":
    _test_bounty_scout()