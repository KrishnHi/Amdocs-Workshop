import { AuditRecord } from "../models/audit.model";
import { logger } from "../../utils/logger";
import { generateSecureToken } from "../../utils/crypto";

export interface WebhookSubscription {
  id: string;
  url: string;
  eventTypes: string[];
  createdAt: string;
}

export class NotificationService {
  private subscriptions: Map<string, WebhookSubscription> = new Map();

  public registerWebhook(url: string, eventTypes: string[]): WebhookSubscription {
    if (!url || !url.startsWith("http")) {
      throw new Error("INVALID_WEBHOOK_URL: URL must be a valid HTTP/HTTPS endpoint.");
    }
    const id = generateSecureToken(16);
    const sub: WebhookSubscription = {
      id,
      url,
      eventTypes,
      createdAt: new Date().toISOString(),
    };
    this.subscriptions.set(id, sub);
    logger.info(`[NotificationService] Registered webhook subscription: ${id} -> ${url}`);
    return sub;
  }

  public getSubscriptions(): WebhookSubscription[] {
    return Array.from(this.subscriptions.values());
  }

  public async dispatchAuditEvent(audit: AuditRecord): Promise<{ dispatchedCount: number }> {
    logger.info(`[NotificationService] Dispatching audit event ${audit.action} for task ${audit.taskId}`);
    let dispatched = 0;
    for (const sub of this.subscriptions.values()) {
      if (sub.eventTypes.includes("*") || sub.eventTypes.includes(audit.action)) {
        dispatched++;
      }
    }
    return { dispatchedCount: dispatched };
  }
}

export const notificationService = new NotificationService();
