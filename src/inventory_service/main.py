from core_logger import get_logger

logger = get_logger("inventory-service")


def reserve_inventory(sku: str) -> bool:
    logger.info("inventory_reserved", sku=sku)
    return True


def mark_unavailable(sku: str) -> None:
    logger.warning("inventory_unavailable", sku=sku)


def main() -> None:
    reserve_inventory("SKU-12345")
    mark_unavailable("SKU-99999")


if __name__ == "__main__":
    main()
