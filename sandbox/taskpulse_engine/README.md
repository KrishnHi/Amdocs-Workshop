# TaskPulse Engine — Cursor Orientation Sandbox

An enterprise-grade TypeScript/Express task orchestrator with structured logging, intentional concurrency bugs, stubbed middleware, and strict `.cursor/rules` configurations designed for hands-on Cursor IDE training.

---

## Workspace Setup

1. **Install Dependencies**:
   ```bash
   npm install
   ```
2. **Run Sanity Unit Tests**:
   ```bash
   npm test
   ```
3. **Start Development Server**:
   ```bash
   npm run dev
   ```

---

## Directory Overview

- `.cursor/rules/`: Cursor MDC rule files enforcing team standards.
- `docs/architecture.md`: Reference documentation for `@docs` context tests.
- `src/api/`: Express routes, middleware, and server bootstrap.
- `src/core/`: Domain models, persistence client, and service layers.
- `src/utils/`: Structured JSON logger and cryptographic helpers.
- `tests/`: Unit and adversarial security test suites.
