# Testing protocol
## What works now
The unittest suite validates the shared CustomerRequest parser using synthetic data.
No integration or end-to-end product tests exist yet. The suite must grow with implementation.

## What each person adds
| Owner | Required evidence |
| --- | --- |
| Oleksii | Form success/validation, clarification display, review/revision flow, PDF content and layout |
| Steeve | Retrieval finds expected source on a small evaluation set, citations match documents, empty/unrelated queries handled |
| Jorge | Known prices produce exact totals; invalid inputs rejected; approval/version checked; duplicate sends prevented; persisted follow-up behavior |
| Vanessa | Extraction and clarification with scripted model responses; allowed tool selection; malformed tool arguments/timeouts; tool loop stops |

Put isolated tests in tests/unit; connected component tests in tests/integration; full user journeys in tests/end_to_end.
Use test_*.py names and keep __init__.py files for unittest discovery.
Frontend framework tests may use their native runner; add that runner to CI before merging frontend features.

## Integration scenarios to build
1. Request → agent → MCP → pricing and retrieval → saved proposal → draft PDF.
2. Missing property size or ambiguous service → clarification, no invented quote.
3. Unsupported service → manual review.
4. Empty retrieval → explicit missing context.
5. Unapproved delivery → blocked.
6. Revised proposal → old approval rejected.
7. Retried delivery → only one email.
8. Customer reply/acceptance/decline → follow-up canceled.
9. Worker restart → scheduled jobs survive.

CI uses mocked LLM/email and synthetic fixtures; it must never send real messages.
Separately run a real-model, real-MCP demo at milestones to validate model behavior. Record model/version, prompt, result and failures.
A green check proves only the tests that actually ran. Do not mark placeholder tests as successful integration coverage.
