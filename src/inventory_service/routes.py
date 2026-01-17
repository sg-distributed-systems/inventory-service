from fastapi import APIRouter

from .main import reserve_inventory
from .schemas import ReserveInventoryRequest, ReserveInventoryResponse

router = APIRouter()


@router.post("/inventory/reserve", response_model=ReserveInventoryResponse)
def reserve_inventory_route(req: ReserveInventoryRequest) -> ReserveInventoryResponse:
    result = reserve_inventory(req.sku)
    return ReserveInventoryResponse(reserved=result)
