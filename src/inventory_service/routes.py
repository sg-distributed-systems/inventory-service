"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import (
    CheckStockRequest,
    CheckStockResponse,
    ReserveStockRequest,
    ReserveStockResponse,
)
from .service import check_stock, reserve_stock

router = APIRouter()


@router.post("/inventory/check", response_model=CheckStockResponse, status_code=200)
def check_stock_route(req: CheckStockRequest) -> CheckStockResponse:
    result = check_stock(sku=req.sku, warehouse_id=req.warehouse_id)
    return CheckStockResponse(
        sku=result["sku"],
        available=result["available"],
        reserved=result["reserved"],
        updated_at=result["updated_at"],
    )


@router.post("/inventory/reserve", response_model=ReserveStockResponse, status_code=200)
def reserve_stock_route(req: ReserveStockRequest) -> ReserveStockResponse:
    result = reserve_stock(
        sku=req.sku,
        warehouse_id=req.warehouse_id,
        quantity=req.quantity,
    )
    return ReserveStockResponse(
        sku=result["sku"],
        available=result["available"],
        reserved=result["reserved"],
        updated_at=result["updated_at"],
    )
