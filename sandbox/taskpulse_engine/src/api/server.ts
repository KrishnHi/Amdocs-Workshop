import express, { Request, Response, NextFunction } from "express";
import { tasksRouter } from "./routes/tasks";
import { webhooksRouter } from "./routes/webhooks";
import { exportRouter } from "./routes/export";
import { applyRateLimiting } from "./middleware/rate-limiter";
import { runMigrations } from "../core/database/migrations";
import { logger } from "../utils/logger";

const app = express();
const PORT = process.env.PORT || 3030;

// Middleware
app.use(express.json());
app.use(applyRateLimiting);

// Route Registrations
app.use("/api/v1/tasks", tasksRouter);
app.use("/api/v1/webhooks", webhooksRouter);
app.use("/api/v1/export", exportRouter);

// Health Endpoint
app.get("/health", (req: Request, res: Response) => {
  res.json({
    success: true,
    data: { status: "UP", timestamp: new Date().toISOString() },
    error: null,
  });
});

// Centralized Error Handling Middleware (Compliant with .cursorrules)
app.use((err: Error, req: Request, res: Response, _next: NextFunction) => {
  logger.error(`[UnhandledException] ${err.message}`, { stack: err.stack });
  res.status(500).json({
    success: false,
    data: null,
    error: {
      code: "INTERNAL_SERVER_ERROR",
      message: err.message || "An unexpected internal server error occurred.",
    },
  });
});

// Initialize database schema and start server
runMigrations();

if (process.env.NODE_ENV !== "test") {
  app.listen(PORT, () => {
    logger.info(`[TaskPulseEngine] Server listening on port ${PORT}`);
  });
}

export default app;
