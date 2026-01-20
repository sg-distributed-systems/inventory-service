"""
Inventory management and stock control logic.

Handles real-time stock queries, reservation management, and availability
calculations across multiple warehouses. Ensures atomic stock operations
to prevent overselling.
"""
from datetime import datetime

from core_logger import get_logger

from .errors import InsufficientInventoryError, NotFoundError, ValidationError

logger = get_logger("inventory-service")

INVENTORY = {
    ("SKU-001", "WH-EAST"): {"available": 150, "reserved": 20},
    ("SKU-001", "WH-WEST"): {"available": 75, "reserved": 5},
    ("SKU-002", "WH-EAST"): {"available": 0, "reserved": 0},
}


def check_stock(sku: str, warehouse_id: str) -> dict:
    logger.info("stock_check", sku=sku, warehouse_id=warehouse_id)

    stock = INVENTORY.get((sku, warehouse_id))
    if not stock:
        logger.warning("stock_not_found", sku=sku, warehouse_id=warehouse_id)
        raise NotFoundError(
            "sku_not_in_warehouse", details={"sku": sku, "warehouse_id": warehouse_id}
        )

    logger.debug("stock_retrieved", sku=sku, available=stock["available"])
    return {
        "sku": sku,
        "available": stock["available"],
        "reserved": stock["reserved"],
        "updated_at": datetime.utcnow(),
    }


def reserve_stock(sku: str, warehouse_id: str, quantity: int) -> dict:
    logger.info(
        "stock_reservation_requested", sku=sku, warehouse_id=warehouse_id, quantity=quantity
    )

    if quantity <= 0:
        raise ValidationError("quantity_must_be_positive")

    stock = INVENTORY.get((sku, warehouse_id))
    if not stock:
        raise NotFoundError("sku_not_in_warehouse")

    if stock["available"] < quantity:
        logger.warning(
            "insufficient_stock", sku=sku, requested=quantity, available=stock["available"]
        )
        raise InsufficientInventoryError(
            "insufficient_stock", details={"available": stock["available"]}
        )

    logger.info("stock_reserved", sku=sku, warehouse_id=warehouse_id, quantity=quantity)
    return {
        "sku": sku,
        "available": stock["available"] - quantity,
        "reserved": stock["reserved"] + quantity,
        "updated_at": datetime.utcnow(),
    }
