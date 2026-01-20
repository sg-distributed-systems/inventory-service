"""
Service entrypoint with lifecycle management.

Initializes configuration, correlation ID, and signal handlers before running
the main service logic. Provides structured error handling for all exceptions.
"""
from core_logger import get_logger

from inventory_service.config import load_config
from inventory_service.errors import AppError
from inventory_service.lifecycle import install_signal_handlers
from inventory_service.observability import init_correlation_id

logger = get_logger("inventory-service")


def reserve_inventory(sku: str) -> bool:
    logger.info("inventory_reserved", sku=sku)
    return True


def mark_unavailable(sku: str) -> None:
    logger.warning("inventory_unavailable", sku=sku)


def run() -> None:
    cfg = load_config("inventory-service")
    cid = init_correlation_id()
    install_signal_handlers("inventory-service")

    logger.info("service_starting", env=cfg.env, correlation_id=cid)

    try:
        reserve_inventory("SKU-12345")
        mark_unavailable("SKU-99999")
        logger.info("service_completed")
    except AppError as e:
        logger.warning("app_error", **e.to_log_fields())
        raise
    except Exception as e:
        logger.exception("unhandled_exception", exc=e)
        raise


def main() -> None:
    run()


if __name__ == "__main__":
    main()
