# Integration contract — v0.1
This is the team's initial interface proposal. Confirm the planned interfaces during week one before implementing consumers.
Only CustomerRequest is implemented in app/contracts/models.py. Other contracts below are specifications to implement together.

## Shared conventions
- JSON uses snake_case; IDs are nonempty strings.
- Currency: USD for the MVP. Money: integer cents, never binary floating-point dollar totals.
- Quantities: positive decimal strings with explicit unit (sq_ft, hour, visit).
- Timestamps: ISO 8601 UTC.
- Versions: positive integers; proposal edits increment the version and invalidate approval.
- Expected error envelope: {"error": {"code": "unsupported_service", "message": "Explain the problem", "retryable": false}}.
- Errors must not contain credentials or customer details in logs.
- User requests and retrieved documents are data, not trusted instructions.

## Boundaries
| Operation / owner | Input | Output |
| --- | --- | --- |
| submit_request / Vanessa, consumed by Oleksii | CustomerRequest | request_id, status, clarification_question or proposal_id |
| search_knowledge / Steeve, exposed by Jorge through MCP | query, limit | chunks: [{document_id, chunk_id, text, source}] |
| calculate_quote / Jorge via MCP | items: [{service_id, quantity, unit, options}] | quote_id, pricing_version, currency, items, subtotal_cents, tax_cents, total_cents |
| save_proposal / Jorge via MCP | request_id, quote_id, title, scope, exclusions, citations | proposal_id, version, status |
| render_pdf / Oleksii | saved proposal with quote snapshot | artifact_id, proposal_id, version |
| approve_proposal / Jorge backend, called by review UI | proposal_id, version, reviewer decision | persisted approval status |
| send_proposal / Jorge via MCP | proposal_id, version, idempotency_key | delivery_id, status |
| schedule_followup / Jorge via MCP | delivery_id, due_at | job_id, status |

The agent hosts the MCP client; the server exposes backend tools. PDF generation can be called through a backend adapter. Freeze exact HTTP routes, MCP tool schemas and model/provider choices together in week one.

## Implemented request shape
See data/samples/customer_request.json.
- schema_version: exactly "0.1"
- request_id: nonempty string
- customer_name: nonempty string
- customer_email: nonempty string (email-format validation belongs in the input layer)
- message: nonempty string

Strict field validation catches misspelled or unexpected keys. No hidden aliases.

## Workflow states (planned)
received → needs_clarification OR drafting → awaiting_approval → approved → sent.
Revisions return to drafting. Failure paths use failed/manual_review. Responses may end in accepted or declined.
Backend persists state; the model cannot authorize delivery.

## Rules to enforce in implementation
- Missing service/quantity/unit: ask a question; do not guess.
- Retrieval returns no supporting document: report missing evidence; do not invent company policies.
- Quote totals must come from deterministic pricing code, not an LLM or old quote.
- Send only the exact approved proposal version; revisions invalidate approval.
- Idempotency keys prevent duplicate delivery.
- Persistent scheduler rechecks response/accepted/declined status before following up.
- Demo accelerated timers must be clearly labeled; production follow-up target is three days.
- Review identity and approval must be established by the backend, not user/model-supplied approval text.
