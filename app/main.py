from fastapi import FastAPI, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.assistant import CRMAssistant
from app.services.crm_service import CRMService

app = FastAPI(title="AI-Powered CRM Assistant", version="1.0.0")
assistant = CRMAssistant(CRMService())


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        return await assistant.chat(
            message=request.message,
            conversation_id=request.conversation_id,
            user_id=request.user_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        # Keep provider details and secrets out of public responses.
        raise HTTPException(
            status_code=502,
            detail="The assistant could not complete the request.",
        ) from exc
