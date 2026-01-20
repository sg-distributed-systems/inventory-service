"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from datetime import datetime

from pydantic import BaseModel, Field


class CheckStockRequest(BaseModel):
    sku: str
    warehouse_id: str


class CheckStockResponse(BaseModel):
    sku: str
    available: int
    reserved: int
    updated_at: datetime


class ReserveStockRequest(BaseModel):
    sku: str
    warehouse_id: str
    quantity: int = Field(gt=0)


class ReserveStockResponse(BaseModel):
    sku: str
    available: int
    reserved: int
    updated_at: datetime
