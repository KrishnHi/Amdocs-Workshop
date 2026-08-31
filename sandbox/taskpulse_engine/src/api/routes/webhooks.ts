import { Router, Request, Response } from "express";
import { notificationService } from "../../core/services/notification";
import { logger } from "../../utils/logger";

export const webhooksRouter = Router();

// POST /api/v1/webhooks/subscribe
webhooksRouter.post("/subscribe", (req: Request, res: Response) => {
  try {
    const { url, eventTypes } = req.body;
    if (!url || !Array.isArray(eventTypes)) {
      res.status(400).json({
        success: false,
        data: null,
        error: { code: "INVALID_PAYLOAD", message: "url (string) and eventTypes (string[]) are required." },
      });
      return;
    }

    const sub = notificationService.registerWebhook(url, eventTypes);
    res.status(201).json({
      success: true,
      data: sub,
      error: null,
    });
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : "Registration failed";
    logger.error(`[WebhooksRouter] Error creating subscription: ${msg}`);
    res.status(400).json({
      success: false,
      data: null,
      error: { code: "WEBHOOK_REGISTRATION_ERROR", message: msg },
    });
  }
});

// GET /api/v1/webhooks/subscriptions
webhooksRouter.get("/subscriptions", (req: Request, res: Response) => {
  const subs = notificationService.getSubscriptions();
  res.json({
    success: true,
    data: subs,
    error: null,
  });
});
