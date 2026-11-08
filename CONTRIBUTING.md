# Team Git protocol
Merge small, tested features throughout the project. Do not wait until week four.
Everyone pushes source code, tests, synthetic examples and updated run instructions.

## First setup
Steeve must add teammates as collaborators in GitHub Settings, and they must accept the invitation.
Public visibility alone does not grant push permission.
Authenticate Git using GitHub CLI (`gh auth login`), Git Credential Manager or SSH. Never paste tokens into repository files.

```bash
git clone https://github.com/steevy-cpu/quote_ai.git
cd quote_ai
```

Run ONLY your branch command:
| Person | Command |
| --- | --- |
| Oleksii | `git switch -c oleksii/interface` |
| Steeve | `git switch -c steeve/rag` |
| Jorge | `git switch -c jorge/backend` |
| Vanessa | `git switch -c vanessa/agent` |

These branches are created locally by these commands; they are not pre-created on GitHub.

## Each work session
Start with a clean working tree (commit your work first):
```bash
git fetch origin
git merge origin/main
```
If conflicts appear, agree on the intended behavior with the affected owner, edit the conflicting files, stage them and complete the merge. Rerun tests. Never resolve conflicts by blindly keeping one whole side.
To abandon an unresolved merge safely, use `git merge --abort`.

## Before pushing
```bash
python -m unittest discover -s tests -p "test_*.py" -v
git status
git diff
git add .
git diff --cached
git commit -m "Describe the completed change"
git push -u origin HEAD
```
Inspect staged changes before committing. Never commit real customer data, API keys, downloaded models, local databases or virtual environments.
After the first push, `git push` is sufficient.

## Pull requests
1. Open a pull request from your branch to main.
2. Explain what changed, how to run it and what tests passed.
3. Obtain one teammate's review. Shared contract changes need review from the affected owners.
4. Bring in latest main and rerun tests if needed.
5. Merge only when CI passes and the reviewer approves.

For these long-lived person branches, use **Create a merge commit**, then merge origin/main back into your branch before continuing. Alternatively, use fresh feature branches per PR; do not mix strategies without agreeing as a team.
Do not force-push shared branches. Do not push directly to main after this initial setup.

## Shared contract changes
Update app/contracts/, docs/integration_contract.md, examples, producers, consumers and tests in one coordinated PR.
Open a draft PR early when another teammate depends on your work.
A Git merge can be conflict-free while the application is broken; integration tests verify the connection.

## Repository owner setup (manual)
In GitHub repository Settings, configure a rule for main:
- Require a pull request and at least one approval.
- Dismiss stale approvals when new changes are pushed.
- Require the successful `tests` status check and require branches to be up to date.
- Block force pushes and branch deletion.

These are instructions, not settings applied by the scaffold. The connector does not expose repository administration writes.
Add frontend lint/build/test checks to CI when the frontend stack is chosen.

## Definition of done
Code runs from documented setup; meaningful success and failure tests pass; inputs/outputs match shared contracts; no secrets are committed; latest main is integrated; a teammate reviews the PR; CI passes.
