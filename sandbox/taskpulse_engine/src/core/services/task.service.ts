import { db } from "../database/client";
import { TaskRecord, CreateTaskPayload, UpdateTaskPayload, TaskStatus, TaskPriority } from "../models/task.model";
import { AuditAction, AuditRecord } from "../models/audit.model";
import { generateSecureToken } from "../../utils/crypto";
import { logger } from "../../utils/logger";
import { notificationService } from "./notification";

export class TaskService {
  private getTable() {
    return db.getTable("tasks");
  }

  private emitAudit(taskId: string, action: AuditAction, payload?: Record<string, unknown>): void {
    const audit: AuditRecord = {
      id: `aud_${generateSecureToken(8)}`,
      taskId,
      action,
      timestamp: new Date().toISOString(),
      payload,
    };
    void notificationService.dispatchAuditEvent(audit);
  }

  public createTask(payload: CreateTaskPayload): TaskRecord {
    const id = `tsk_${generateSecureToken(8)}`;
    const now = new Date().toISOString();

    const record: TaskRecord = {
      id,
      title: payload.title,
      description: payload.description,
      status: TaskStatus.TODO,
      priority: payload.priority || TaskPriority.MEDIUM,
      tags: payload.tags || [],
      assignee: payload.assignee,
      created_at: now,
      updated_at: now,
    };

    this.getTable().set(id, record as unknown as Record<string, unknown> & { id: string });
    logger.info(`[TaskService] Created task ${id}: ${record.title}`);
    this.emitAudit(id, AuditAction.TASK_CREATED, { title: record.title });
    return record;
  }

  public getTaskById(id: string): TaskRecord | null {
    const record = this.getTable().get(id);
    return record ? (record as unknown as TaskRecord) : null;
  }

  public getAllTasks(): TaskRecord[] {
    return Array.from(this.getTable().values()) as unknown as TaskRecord[];
  }

  public getTasksPaged(offset: number, limit: number): TaskRecord[] {
    const all = this.getAllTasks();
    return all.slice(offset, offset + limit);
  }

  /**
   * BUGGY METHOD FOR LAB 3.2 ROOT CAUSE ANALYSIS:
   * Notice that spreading `payload` directly without preserving `existing` properly can drop
   * existing unmentioned fields (such as `tags` or `created_at`).
   */
  public updateTaskStatus(id: string, newStatus: TaskStatus): TaskRecord | null {
    const existing = this.getTaskById(id);
    if (!existing) return null;

    const now = new Date().toISOString();
    
    // INTENTIONAL SHALLOW SPREAD CONCURRENCY DEFECT (Lab 3.2 target):
    const updated: TaskRecord = {
      id: existing.id,
      title: existing.title,
      description: existing.description,
      status: newStatus,
      priority: existing.priority,
      tags: existing.tags,
      assignee: existing.assignee,
      created_at: existing.created_at,
      updated_at: now,
      completed_at: newStatus === TaskStatus.COMPLETED ? now : existing.completed_at,
    };

    this.getTable().set(id, updated as unknown as Record<string, unknown> & { id: string });
    logger.info(`[TaskService] Updated task status ${id} -> ${newStatus}`);
    this.emitAudit(id, AuditAction.STATUS_CHANGED, { status: newStatus });
    return updated;
  }

  public updateTask(id: string, payload: UpdateTaskPayload): TaskRecord | null {
    const existing = this.getTaskById(id);
    if (!existing) return null;

    const updated: TaskRecord = {
      ...existing,
      ...payload,
      updated_at: new Date().toISOString(),
    };

    this.getTable().set(id, updated as unknown as Record<string, unknown> & { id: string });
    this.emitAudit(id, AuditAction.TASK_UPDATED, { ...payload });
    return updated;
  }

  public deleteTask(id: string): boolean {
    const removed = this.getTable().delete(id);
    if (removed) {
      this.emitAudit(id, AuditAction.TASK_DELETED);
    }
    return removed;
  }

  /**
   * PLACEHOLDER FOR LAB 3.1 (Ghost Text Tab Shaping Exercise):
   * Trainees use Cursor autocomplete/ghost text to complete this method with null-safety and no extra libraries.
   */
  public filterTasksByPriorityAndDate(
    tasks: TaskRecord[],
    priority?: TaskPriority,
    sinceDate?: string | Date
  ): TaskRecord[] {
    const targetTimestamp = sinceDate ? new Date(sinceDate).getTime() : 0;

    return tasks.filter((task) => {
      const matchesPriority = priority ? task.priority === priority : true;
      const createdAtTimestamp = new Date(task.created_at).getTime();
      const matchesDate =
        !isNaN(targetTimestamp) && targetTimestamp > 0
          ? createdAtTimestamp >= targetTimestamp
          : true;

      return matchesPriority && matchesDate;
    });
  }
}

export const taskService = new TaskService();
