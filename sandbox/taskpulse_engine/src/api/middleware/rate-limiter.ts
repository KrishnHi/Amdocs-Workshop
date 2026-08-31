import { Request, Response, NextFunction } from "express";
import { logger } from "../../utils/logger";

interface ClientRateLimitState {
  timestamps: number[];
}

const rateLimitStore = new Map<string, ClientRateLimitState>();
const WINDOW_MS = 60 * 1000;
const MAX_REQUESTS = 100;

/**
 * In-memory sliding-window limiter: 100 requests per 60s per client IP.
 * Prunes timestamps older than the window so the Map cannot grow without bound.
 */
export function applyRateLimiting(req: Request, res: Response, next: NextFunction): void {
  const clientIp = req.ip || req.socket.remoteAddress || "unknown_client";
  const now = Date.now();

  let state = rateLimitStore.get(clientIp);
  if (!state) {
    state = { timestamps: [] };
    rateLimitStore.set(clientIp, state);
  }

  state.timestamps = state.timestamps.filter((ts) => now - ts < WINDOW_MS);

  if (state.timestamps.length === 0) {
    rateLimitStore.delete(clientIp);
    state = { timestamps: [] };
    rateLimitStore.set(clientIp, state);
  }

  if (state.timestamps.length >= MAX_REQUESTS) {
    logger.warn(`[RateLimiter] Rate limit exceeded for IP: ${clientIp}`);
    res.status(429).json({
      success: false,
      data: null,
      error: {
        code: "RATE_LIMIT_EXCEEDED",
        message: "Too many requests. Please try again later.",
      },
    });
    return;
  }

  state.timestamps.push(now);
  next();
}
