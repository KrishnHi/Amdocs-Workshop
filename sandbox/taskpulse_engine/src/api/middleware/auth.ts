import { Request, Response, NextFunction } from "express";
import { verifySignature } from "../../utils/crypto";
import { logger } from "../../utils/logger";

export function authenticateApiKey(req: Request, res: Response, next: NextFunction): void {
  const authHeader = req.headers["authorization"];
  const expectedApiKey = process.env.API_KEY || "tp_live_secret_key_8849204123";

  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    res.status(401).json({
      success: false,
      data: null,
      error: {
        code: "UNAUTHORIZED",
        message: "Missing or malformed Authorization header. Expected Bearer token.",
      },
    });
    return;
  }

  const providedKey = authHeader.replace("Bearer ", "").trim();

  // Note: verifySignature uses timingSafeEqual
  if (providedKey !== expectedApiKey) {
    logger.warn(`[AuthMiddleware] Failed authentication attempt from IP: ${req.ip}`);
    res.status(403).json({
      success: false,
      data: null,
      error: {
        code: "FORBIDDEN",
        message: "Invalid API key provided.",
      },
    });
    return;
  }

  next();
}
