import { Router, Request, Response, NextFunction } from "express";
import { taskService } from "../../core/services/task.service";
import { TaskStatus, TaskPriority } from "../../core/models/task.model";
import { logger } from "../../utils/logger";

export const tasksRouter = Router();

// GET /api/v1/tasks
tasksRouter.get("/", (req: Request, res: Response, next: NextFunction) => {
  try {
    const priority = req.query.priority as TaskPriority | undefined;
    const since = req.query.since as string | undefined;

    let tasks = taskService.getAllTasks();
    if (priority || since) {
      tasks = taskService.filterTasksByPriorityAndDate(tasks, priority, since);
    }

    res.json({
      success: true,
      data: tasks,
      error: null,
    });
  } catch (err) {
    next(err);
  }
});

// GET /api/v1/tasks/:id
tasksRouter.get("/:id", (req: Request, res: Response) => {
  const task = taskService.getTaskById(req.params.id);
  if (!task) {
    res.status(404).json({
      success: false,
      data: null,
      error: { code: "TASK_NOT_FOUND", message: `Task with id ${req.params.id} does not exist.` },
    });
    return;
  }

  res.json({
    success: true,
    data: task,
    error: null,
  });
});

// POST /api/v1/tasks
tasksRouter.post("/", (req: Request, res: Response, next: NextFunction) => {
  try {
    const { title, description, priority, tags, assignee } = req.body;
    if (!title || !description) {
      res.status(400).json({
        success: false,
        data: null,
        error: { code: "INVALID_PAYLOAD", message: "title and description are required fields." },
      });
      return;
    }

    const task = taskService.createTask({ title, description, priority, tags, assignee });
    res.status(201).json({
      success: true,
      data: task,
      error: null,
    });
  } catch (err) {
    next(err);
  }
});

// PATCH /api/v1/tasks/:id/status
tasksRouter.patch("/:id/status", (req: Request, res: Response, next: NextFunction) => {
  try {
    const { status } = req.body;
    if (!status || !Object.values(TaskStatus).includes(status)) {
      res.status(400).json({
        success: false,
        data: null,
        error: { code: "INVALID_STATUS", message: `Status must be one of: ${Object.values(TaskStatus).join(", ")}` },
      });
      return;
    }

    const updated = taskService.updateTaskStatus(req.params.id, status);
    if (!updated) {
      res.status(404).json({
        success: false,
        data: null,
        error: { code: "TASK_NOT_FOUND", message: `Task with id ${req.params.id} does not exist.` },
      });
      return;
    }

    res.json({
      success: true,
      data: updated,
      error: null,
    });
  } catch (err) {
    next(err);
  }
});

// DELETE /api/v1/tasks/:id (Target for Lab 3.2 Rule Verification)
tasksRouter.delete("/:id", (req: Request, res: Response) => {
  const deleted = taskService.deleteTask(req.params.id);
  if (!deleted) {
    logger.warn(`[TasksRouter] Attempted delete on non-existent task ${req.params.id}`);
    res.status(404).json({
      success: false,
      data: null,
      error: { code: "TASK_NOT_FOUND", message: `Task with id ${req.params.id} does not exist.` },
    });
    return;
  }

  res.json({
    success: true,
    data: { id: req.params.id, deleted: true },
    error: null,
  });
});
