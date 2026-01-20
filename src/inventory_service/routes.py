"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .main import reserve_inventory
from .schemas import ReserveInventoryRequest, ReserveInventoryResponse

router = APIRouter()


@router.post("/inventory/reserve", response_model=ReserveInventoryResponse)
def reserve_inventory_route(req: ReserveInventoryRequest) -> ReserveInventoryResponse:
    result = reserve_inventory(req.sku)
    return ReserveInventoryResponse(reserved=result)
