from pydantic import BaseModel


class ReserveInventoryRequest(BaseModel):
    sku: str


class ReserveInventoryResponse(BaseModel):
    reserved: bool
