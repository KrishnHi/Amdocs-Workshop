import { db } from "./client";
import { logger } from "../../utils/logger";

export function runMigrations(): void {
  // Ensures all base tables exist and initializes sample seed data
  db.getTable("tasks");
  db.getTable("audit_logs");
  db.getTable("webhooks");
  logger.info("[Migrations] Base schema initialized successfully.");
}
