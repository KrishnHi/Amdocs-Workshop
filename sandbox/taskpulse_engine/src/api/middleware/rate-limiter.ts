import { Request, Response, NextFunction } from "express";
import { logger } from "../../utils/logger";

/**
 * ============================================================================
 * LAB 3.1 EXERCISE 2: INLINE EDIT REFACTORING (Cmd/Ctrl+K)
 * ============================================================================
 * Trainee Task: Highlight the applyRateLimiting function below and use Cmd/Ctrl+K
 * to generate an in-memory sliding-window rate limiter (100 req / 60s per client IP)
 * that cleans up stale entries and returns the standard project error envelope on HTTP 429.
 */
export function applyRateLimiting(req: Request, res: Response, next: NextFunction): void {
  // PLACEHOLDER STUB: Replace this with your Cmd/Ctrl+K generated sliding-window logic
  logger.debug(`[RateLimiter] Pass-through placeholder executed for ${req.ip}`);
  next();
}
