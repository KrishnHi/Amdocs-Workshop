import { logger } from "../../utils/logger";

export interface DatabaseRow {
  id: string;
  [key: string]: unknown;
}

export class DatabaseClient {
  private tables: Map<string, Map<string, DatabaseRow>> = new Map();

  constructor() {
    this.tables.set("tasks", new Map());
    this.tables.set("audit_logs", new Map());
    this.tables.set("webhooks", new Map());
    logger.info("[DatabaseClient] In-memory storage engine initialized.");
  }

  public getTable(name: string): Map<string, DatabaseRow> {
    const table = this.tables.get(name);
    if (!table) {
      const newTable = new Map<string, DatabaseRow>();
      this.tables.set(name, newTable);
      return newTable;
    }
    return table;
  }

  public clear(): void {
    for (const table of this.tables.values()) {
      table.clear();
    }
  }
}

export const db = new DatabaseClient();
