import { notificationService } from "../../src/core/services/notification";
import { AuditAction, AuditRecord } from "../../src/core/models/audit.model";

describe("Webhook & Notification Unit Tests", () => {
  it("should register a valid webhook subscription", () => {
    const sub = notificationService.registerWebhook("https://example.com/webhook", ["TASK_CREATED", "STATUS_CHANGED"]);
    expect(sub.id).toBeDefined();
    expect(sub.url).toBe("https://example.com/webhook");
    expect(sub.eventTypes).toContain("TASK_CREATED");
  });

  it("should reject invalid webhook URLs without http/https prefix", () => {
    expect(() => {
      notificationService.registerWebhook("ftp://invalid-url", ["*"]);
    }).toThrow("INVALID_WEBHOOK_URL");
  });

  it("should dispatch audit events to matching subscriptions", async () => {
    notificationService.registerWebhook("https://hooks.slack.com/services/123", ["TASK_CREATED"]);
    
    const audit: AuditRecord = {
      id: "aud_123",
      taskId: "tsk_456",
      action: AuditAction.TASK_CREATED,
      timestamp: new Date().toISOString(),
    };

    const result = await notificationService.dispatchAuditEvent(audit);
    expect(result.dispatchedCount).toBeGreaterThanOrEqual(1);
  });
});
