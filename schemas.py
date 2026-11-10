from pydantic import BaseModel , ConfigDict
from typing import  List , Optional

class Deal(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name:str
    amount:float 
    stage: str 


class CustomerDeals(BaseModel):
    model_config = ConfigDict(extra="forbid")

    customer_name: str
    total_deals: int
    total_value: float
    deals: List[Deal]
    
    
class CRMResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    success: bool
    message: str
    data: Optional[dict] = None