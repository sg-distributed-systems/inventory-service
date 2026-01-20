# inventory-service

Manages inventory and stock tracking for products.

## Why this repo exists

Real-time inventory tracking requires a dedicated service to handle concurrent stock updates and prevent overselling across multiple sales channels.

## Core Components

### `reserve_inventory(sku: str) -> bool`
Attempts to reserve stock for a given SKU.

**Logs:**
- `inventory_reserved` — Logged when stock is successfully reserved

### `mark_unavailable(sku: str)`
Marks a SKU as out of stock.

**Logs:**
- `inventory_unavailable` — Logged when requested inventory cannot be fulfilled

### `load_config(service_name: str) -> ServiceConfig`
Loads service configuration from environment variables including `APP_ENV` and `SHUTDOWN_TIMEOUT_SECONDS`.

### `AppError`
Base exception class for application errors. Provides `to_log_fields()` for structured error logging.

### `install_signal_handlers(service_logger_name: str)`
Installs SIGINT/SIGTERM handlers for graceful shutdown with logging.

### `init_correlation_id() -> str`
Initializes a correlation ID from the `CORRELATION_ID` environment variable or generates a UUID4.

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/inventory/reserve` | POST | Reserves inventory for a SKU |

### Running the service

```bash
uvicorn src.inventory_service.app:app --host 0.0.0.0 --port 8005
```
