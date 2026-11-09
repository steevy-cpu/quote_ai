# QuoteAI

QuoteAI is an AI quote and proposal generator for service businesses. It will use MCP, RAG, and an agentic workflow to find company information, look up pricing, and help create customer proposals.

## Team

| Person | Responsibility | Folder |
| --- | --- | --- |
| Oleksii Kundenko | User interface and PDF presentation | frontend/, app/presentation/ |
| Steeve A. Celestin | Company knowledge and RAG | app/knowledge/ |
| Jorge Diaz | MCP server and backend operations | app/backend/ |
| Vanessa Guzman | Agentic pipeline | app/agent/ |
| Everyone | Shared contracts and testing | app/contracts/, tests/ |

## Setup

Clone the repository:

```bash
git clone https://github.com/steevy-cpu/quote_ai.git
cd quote_ai
```

## Structure

```text
quote_ai/
├── frontend/
├── app/
│   ├── presentation/
│   ├── knowledge/
│   ├── backend/
│   ├── agent/
│   └── contracts/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── end_to_end/
├── data/
│   └── samples/
├── docs/
├── .env.example
├── .gitignore
└── README.md
```

Empty `.gitkeep` files keep the folders visible in GitHub.
