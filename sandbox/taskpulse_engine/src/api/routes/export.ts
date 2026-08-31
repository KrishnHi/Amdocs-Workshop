import { Router, Request, Response, NextFunction } from "express";
import { taskService } from "../../core/services/task.service";
import { generateSecureToken, createHmacSignature, verifySignature } from "../../utils/crypto";
import { logger } from "../../utils/logger";

export const exportRouter = Router();

/**
 * Capstone Practical 3.4 Target:
 * Secure Batch Task Export & Cryptographic Signature Verification
 */
exportRouter.post("/tasks", async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { format = "json" } = req.body;
    const token = generateSecureToken(32);
    const signature = createHmacSignature(token);

    logger.info(`[ExportRouter] Generated secure export session: token=${token}`);

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
  } catch (err) {
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
    logger.warn(`[ExportRouter] Tampered or invalid signature attempt: token=${token}`);
    res.status(403).json({
      success: false,
      data: null,
      error: { code: "FORBIDDEN", message: "Invalid signature." },
    });
    return;
  }

  const tasks = taskService.getAllTasks();
  res.setHeader("Content-Disposition", `attachment; filename="tasks-export-${Date.now()}.json"`);
  res.setHeader("Content-Type", "application/json");
  res.send(JSON.stringify(tasks, null, 2));
});
