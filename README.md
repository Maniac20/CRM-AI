# AI-Powered CRM Assistant

A learning project demonstrating an LLM-powered backend assistant using FastAPI, Groq's OpenAI-compatible API, Python tool calling, Pydantic validation, and mock CRM data.

## Features

- Natural-language questions about customers and deals.
- Multi-turn conversation context keyed by user and conversation ID.
- Controlled backend tools for customer search and deal retrieval.
- Ambiguous customer handling (two customers named Rahul Sharma).
- Backend-calculated deal totals.
- Optional deal filtering by close month (`YYYY-MM`).
- Async LLM calls, request timeout, and bounded tool-call loop.
- Pydantic request/response and CRM data models.
- Unit tests that do not call the LLM API.

## Limitations

- CRM data is mock data in `app/crm/mock_data.py`.
- Conversation history is stored in process memory and disappears on restart.
- `user_id` is a demo identifier, not authentication. Do not expose this API publicly without real authentication and authorization.
- The model can request tools, but the backend allowlists tool names and performs execution.
- No real HubSpot/Salesforce credentials or customer data are used.

## Setup

Python 3.11+ recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add your Groq API key to `.env`.

## Run

```bash
uvicorn app.main:app --reload
```

API documentation: `http://127.0.0.1:8000/docs`

## Example request

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "demo-user",
    "message": "Show Rahul Sharma'''s deals",
    "conversation_id": null
  }'
```

The response includes a `conversation_id`. Include it in later requests to continue the same conversation.

There are two mock customers named Rahul Sharma. The assistant should ask whether you mean Acme Corp or GlobalTech.

Example specific request:
"Show Rahul Sharma from Acme Corp's deals closing in November 2026."

## Tests

Tests do not call the LLM API:

```bash
pytest -q
```

## Structure

```text
crm-ai-assistant/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── crm/
│   │   └── mock_data.py
│   ├── schemas/
│   │   ├── chat.py
│   │   └── crm.py
│   ├── services/
│   │   ├── assistant.py
│   │   └── crm_service.py
│   └── tools/
│       └── definitions.py
├── tests/
│   └── test_crm_service.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
