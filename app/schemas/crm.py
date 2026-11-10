from pydantic import BaseModel, ConfigDict, Field


class Deal(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    amount: float = Field(ge=0)
    currency: str = "INR"
    stage: str
    close_date: str
    customer_id: str


class Customer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    company: str
    email: str


class CustomerLookupResult(BaseModel):
    status: str
    message: str
    matches: list[Customer] = Field(default_factory=list)


class DealLookupResult(BaseModel):
    customer: Customer
    deals: list[Deal]
    total_deals: int
    total_value: float
