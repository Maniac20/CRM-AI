from pydantic import BaseModel, ConfigDict, Field


class ChatRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    message: str = Field(min_length=1, max_length=4000)
    conversation_id: str | None = Field(default=None, max_length=100)
    # Demo identifier only. Replace with an authenticated principal in production.
    user_id: str = Field(default="demo-user", min_length=1, max_length=100)


class ChatResponse(BaseModel):
    conversation_id: str
    answer: str
    tool_calls: list[str] = Field(default_factory=list)
