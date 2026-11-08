# QuoteAI
A four-person NLP class project: generate service proposals using an LLM, RAG, and MCP.

**Status: project scaffold.** The application, MCP server, RAG pipeline, PDF renderer, and agent are not implemented yet. The starter tests validate our first shared request contract only.

## Team
| Person | Owns | Folder |
| --- | --- | --- |
| Oleksii Kundenko | Request form, clarification/review UI, PDF rendering | frontend/, app/presentation/ |
| Steeve A. Celestin | Company documents, RAG retrieval, citations, retrieval evaluation | app/knowledge/ |
| Jorge Diaz | MCP server, pricing database/calculations, storage, delivery and scheduling | app/backend/ |
| Vanessa Guzman | Agent workflow, model prompts, MCP client, tool loop and error handling | app/agent/ |
| Everyone | Shared contracts and integration tests | app/contracts/, tests/ |

## Setup
Use Python 3.11 or 3.12 for the initial shared baseline. No third-party dependencies are needed for the starter tests.
```bash
git clone https://github.com/steevy-cpu/quote_ai.git
cd quote_ai
python -m venv .venv
```
Activate with `source .venv/bin/activate` on macOS/Linux, or `.venv\Scripts\Activate.ps1` in Windows PowerShell.
If your computer uses `python3`, substitute it for `python`.
Copy `.env.example` to `.env` when implementing configuration. The scaffold does not load environment files yet.

## Test
Run from the repository root:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
GitHub Actions runs this on pushes and pull requests. A green starter check is not evidence that the finished product works.
Add dependencies explicitly and update both setup instructions and CI when introducing frameworks.

## Structure
```text
frontend/
app/
  presentation/
  knowledge/
  backend/
  agent/
  contracts/
tests/
  unit/
  integration/
  end_to_end/
data/samples/
docs/
  integration_contract.md
  testing.md
  milestones.md
.github/
  workflows/ci.yml
  pull_request_template.md
```

## MVP
One fictional landscaping company, web form input, retrieval with sources, database-based pricing, draft PDF, human review, test email and a persisted follow-up job.
Current prices come from the database; Python calculates totals. RAG provides company context. The agent coordinates the steps.
Real customer inbox ingestion and production deployment are outside this four-week MVP.

Start with [CONTRIBUTING.md](CONTRIBUTING.md), the [integration contract](docs/integration_contract.md), and the [four-week plan](docs/milestones.md).
