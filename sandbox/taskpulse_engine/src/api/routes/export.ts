import { Router, Request, Response, NextFunction } from "express";
import { taskService } from "../../core/services/task.service";
import { generateSecureToken, createHmacSignature, verifySignature } from "../../utils/crypto";
import { logger } from "../../utils/logger";

export const exportRouter = Router();

const EXPORT_PAGE_SIZE = 100;

/**
 * Capstone Practical 3.4: Secure Batch Task Export & HMAC-signed download.
 * Tokens use crypto.randomBytes (not Math.random). Signatures use timingSafeEqual.
 * Download streams paged chunks to avoid loading the full table into one buffer.
 */
exportRouter.post("/tasks", async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { format = "json" } = req.body ?? {};
    const token = generateSecureToken(32);
    const signature = createHmacSignature(token);

    logger.info("[ExportRouter] Generated secure export session");

    res.status(202).json({
      success: true,
      data: {
        token,
        signature,
        format,
        status: "PROCESSING",
        downloadUrl: `/api/v1/export/download?token=${token}&sig=${signature}`,
      },
      error: null,
    });
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : "Unknown error";
    logger.error(`[ExportRouter] Failed to create export session: ${msg}`, { error: err });
    next(err);
  }
});

exportRouter.get("/download", (req: Request, res: Response) => {
  const { token, sig } = req.query;

  if (typeof token !== "string" || typeof sig !== "string") {
    res.status(400).json({
      success: false,
      data: null,
      error: { code: "INVALID_PARAMS", message: "token and signature query params required." },
    });
    return;
  }

  const expectedSig = createHmacSignature(token);
  if (!verifySignature(sig, expectedSig)) {
    logger.warn("[ExportRouter] Tampered or invalid signature attempt");
    res.status(403).json({
      success: false,
      data: null,
      error: { code: "FORBIDDEN", message: "Invalid signature." },
    });
    return;
  }

  try {
    res.setHeader("Content-Disposition", `attachment; filename="tasks-export-${Date.now()}.json"`);
    res.setHeader("Content-Type", "application/json");
    res.write("[");

    let offset = 0;
    let first = true;
    while (true) {
      const chunk = taskService.getTasksPaged(offset, EXPORT_PAGE_SIZE);
      if (!chunk.length) {
        break;
      }
      for (const task of chunk) {
        if (!first) {
          res.write(",");
        }
        first = false;
        res.write(JSON.stringify(task));
      }
      offset += EXPORT_PAGE_SIZE;
    }

    res.write("]");
    res.end();
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : "Unknown error";
    logger.error(`[ExportRouter] Export stream failed: ${msg}`, { error: err });
    if (!res.headersSent) {
      res.status(500).json({
        success: false,
        data: null,
        error: { code: "EXPORT_FAILED", message: msg },
      });
    } else {
      res.end();
    }
  }
});
