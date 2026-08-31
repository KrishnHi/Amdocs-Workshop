import { taskService } from "../../src/core/services/task.service";
import { TaskPriority, TaskStatus } from "../../src/core/models/task.model";
import { db } from "../../src/core/database/client";

describe("TaskService Unit Tests", () => {
  beforeEach(() => {
    db.clear();
  });

  it("should create a new task with TODO status", () => {
    const task = taskService.createTask({
      title: "Deploy auth microservice",
      description: "Setup JWT verification cluster",
      priority: TaskPriority.HIGH,
      tags: ["auth", "prod"],
    });

    expect(task.id).toMatch(/^tsk_/);
    expect(task.title).toBe("Deploy auth microservice");
    expect(task.status).toBe(TaskStatus.TODO);
    expect(task.priority).toBe(TaskPriority.HIGH);
    expect(task.tags).toContain("auth");
  });

  it("should update task status to COMPLETED and set completed_at", () => {
    const task = taskService.createTask({
      title: "Run database migrations",
      description: "Apply v2 schema",
    });

    const updated = taskService.updateTaskStatus(task.id, TaskStatus.COMPLETED);
    expect(updated).not.toBeNull();
    expect(updated?.status).toBe(TaskStatus.COMPLETED);
    expect(updated?.completed_at).toBeDefined();
  });

  it("should filter tasks by priority and date correctly", () => {
    const t1 = taskService.createTask({
      title: "Fix low CSS bug",
      description: "Navbar padding",
      priority: TaskPriority.LOW,
    });
    const t2 = taskService.createTask({
      title: "Fix critical payment bug",
      description: "Stripe webhook drop",
      priority: TaskPriority.CRITICAL,
    });

    const all = [t1, t2];
    const filtered = taskService.filterTasksByPriorityAndDate(all, TaskPriority.CRITICAL);
    expect(filtered.length).toBe(1);
    expect(filtered[0].title).toBe("Fix critical payment bug");
  });
});
