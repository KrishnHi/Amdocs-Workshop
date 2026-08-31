# TaskPulse Architecture Reference

## Overview
TaskPulse is a modular, high-throughput task coordination engine.

### Layered Architecture
- **`src/api/`**: Express HTTP boundary. Houses routers, authentication middleware, rate limiting, and centralized error handling.
- **`src/core/models/`**: Domain entities (`TaskRecord`, `AuditRecord`, etc.) and enum definitions.
- **`src/core/services/`**: Business logic engines (`TaskService`, `NotificationService`).
- **`src/core/database/`**: In-memory / SQLite persistence layer abstraction.
- **`src/utils/`**: Shared infrastructure utilities (`logger.ts`, `crypto.ts`).

### Invariant Rules
1. Services must never import Express `req` or `res` objects.
2. Cross-cutting audit events must be published through `NotificationService`.
3. All logging must use the structured JSON logger.
