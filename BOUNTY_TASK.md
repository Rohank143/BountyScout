# Bounty Fix

**Reward:** $20.00
**Issue:** https://github.com/Rohank143/BountyScout/issues/127
**Repo:** https://github.com/Rohank143/BountyScout

---

## Issue

🎯 Bounty Alert: 14 New Opportunityies found

### Active Bounty Scan Results

**Scan Time:** 2026-11-20 02:08 UTC

#### 1. [🪙 [Web3] [Wave 3: 2 × $20 USDC | 3-Year Protocol Trajectory](https://github.com/alfrexo95/bounty-bot/issues/96)
- **Repository:** [alfrexo95/bounty-bot](https://github.com/alfrexo95/bounty-bot)
- **Comments:** 1
- **Last Updated:** 2026-11-20T02:07:09Z

#### 2. [🎯 Bounty Alert: 12 New Opportunityies found](https://github.com/dev-kp-eloper/BountyScout/issues/1784)
- **Repository:** [dev-kp-eloper/BountyScout](https://github.com/dev-kp-eloper/BountyScout)
- **Comments:** 0
- **Last Updated:** 2026-11-20T02:05:38Z

#### 3. [[P0][Delivery] Two-sided agentic audit MVP and Dec 9 submission](https://github.com/huydo2105/veripoc/issues/19)
- **Repository:** [huydo2105/veripoc](https://github.com/huydo2105/veripoc)
- **Comments:** 0
- **Last Updated:** 2026-11-20T02:05:38Z

#### 4. [[Bounty #28] Temporal memory benchmark · agents (LongMemEval)](https://github.com/hanzoai/agents/issues/82)
- **Repository:** [hanzoai/agents](https://github.com/hanzoai/agents)
- **Comments:** 4
- **Last Updated:** 2026-11-20T02:04:53Z

#### 5. [Card coverage: Guilds of Ravnica (GRN)](https://github.com/krakenhavoc/cmd_and_ctrl/issues/5525)
- **Repository:** [krakenhavoc/cmd_and_ctrl](https://github.com/krakenhavoc/cmd_and_ctrl)
- **Comments:** 1
- **Last Updated:** 2026-11-20T02:04:08Z

#### 6. [[Bounty #35] Durable event-driven agent workflow replay · agents](https://github.com/hanzoai/agents/issues/85)
- **Repository:** [hanzoai/agents](https://github.com/hanzoai/agents)
- **Comments:** 5
- **Last Updated:** 2026-11-20T02:04:01Z

#### 7. [[P1][Review] Team finding inbox, manual triage and patch retest](https://github.com/huydo2105/veripoc/issues/36)
- **Repository:** [huydo2105/veripoc](https://github.com/huydo2105/veripoc)
- **Comments:** 0
- **Last Updated:** 2026-11-20T02:00:59Z

#### 8. [[P0][Auth] Concordium wallet login and compact header account menu](https://github.com/huydo2105/veripoc/issues/50)
- **Repository:** [huydo2105/veripoc](https://github.com/huydo2105/veripoc)
- **Comments:** 0
- **Last Updated:** 2026-11-20T02:00:09Z

#### 9. [Partner sales kit: getting companies to post tasks](https://github.com/ADT-community/adt-community.github.io/issues/12)
- **Repository:** [ADT-community/adt-community.github.io](https://github.com/ADT-community/adt-community.github.io)
- **Comments:** 2
- **Last Updated:** 2026-11-20T01:45:21Z

#### 10. [Daily report: summary of open bounties across repos](https://github.com/ADT-community/ADT_agent/issues/3)
- **Repository:** [ADT-community/ADT_agent](https://github.com/ADT-community/ADT_agent)
- **Comments:** 4
- **Last Updated:** 2026-11-20T01:44:57Z

#### 11. [Admitted + confirmed op-0 policy rule never enters the application-rules accumulation (block 29, fee charged, gettaustate unchanged)](https://github.com/IDNI/tau-testnet/issues/42)
- **Repository:** [IDNI/tau-testnet](https://github.com/IDNI/tau-testnet)
- **Comments:** 18
- **Last Updated:** 2026-11-20T02:00:49Z

#### 12. [Payout ledger: what's owed, and marking it paid](https://github.com/ADT-community/ADT_agent/issues/6)
- **Repository:** [ADT-community/ADT_agent](https://github.com/ADT-community/ADT_agent)
- **Comments:** 5
- **Last Updated:** 2026-11-20T01:46:15Z

#### 13. [MVP definition: help shape v1](https://github.com/ADT-community/ADT_agent/issues/1)
- **Repository:** [ADT-community/ADT_agent](https://github.com/ADT-community/ADT_agent)
- **Comments:** 0
- **Last Updated:** 2026-11-20T01:46:12Z

#### 14. [[Regression on closed #102 / #367] markMergedAndRelease marks a team bounty PAID when the team has no splits or no longer exists, skipping the payout entirely](https://github.com/MergeFi/backend/issues/746)
- **Repository:** [MergeFi/backend](https://github.com/MergeFi/backend)
- **Comments:** 3
- **Last Updated:** 2026-11-20T01:31:09Z



---

## Process

### 1. Orient yourself first
Before touching any code:
- Read the README and any relevant docs
- Run: find . -type f | grep -v node_modules | grep -v .git | grep -v dist | head -60
- Grep for the key terms from the issue title to find the relevant files
- Read the files around the bug — understand what's currently happening

### 2. Find and read the tests
- Look for test files near the relevant code (*.test.ts, *.spec.js, __tests__, etc.)
- Read them — they tell you what behavior is expected
- Understand what a passing fix looks like before writing a line

### 3. Implement the fix
- Make the MINIMAL change that fixes the issue — nothing more
- Do not refactor, rename, reorganize, or clean up unrelated code
- Do not add dependencies unless the issue explicitly requires it
- Do not modify config files (package.json, tsconfig.json, etc.) unless that IS the fix
- One logical change, one commit

### 4. Verify
- Run the test suite: check package.json scripts for "test", "lint", "typecheck"
  Common commands: npm test, yarn test, pnpm test, pytest, go test ./..., cargo test
- If TypeScript is present: npx tsc --noEmit
- Fix any test failures your change caused — if a test was wrong before, update it

### 5. Commit and document
- git add -A
- git commit -m "fix: 🎯 Bounty Alert: 14 New Opportunityies found"
- Write AGENT_SUMMARY.md with:
  - Root cause: what was wrong and why
  - Fix: what you changed and the reasoning
  - Verification: how to confirm it works
  - Concerns: anything a reviewer should know

---

## Stop conditions

If ANY of these are true, write "UNCERTAIN: [reason]" at the top of AGENT_SUMMARY.md, make NO code changes, and stop:
- The fix requires changing more than ~5 files
- You cannot determine what the correct behavior should be
- The issue requires a database migration, API key, or external service
- You find 3+ open PRs already attempting this fix (high competition)
- The repo is not in a language/framework you can reason about confidently

A clean UNCERTAIN is better than a bad PR.
