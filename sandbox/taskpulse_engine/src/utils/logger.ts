export interface LogEntry {
  timestamp: string;
  level: "INFO" | "WARN" | "ERROR" | "DEBUG";
  message: string;
  context?: Record<string, unknown>;
}

class StructuredLogger {
  private format(level: LogEntry["level"], message: string, context?: Record<string, unknown>): string {
    const entry: LogEntry = {
      timestamp: new Date().toISOString(),
      level,
      message,
      ...(context ? { context } : {}),
    };
    return JSON.stringify(entry);
  }

  public info(message: string, context?: Record<string, unknown>): void {
    process.stdout.write(this.format("INFO", message, context) + "\n");
  }

  public warn(message: string, context?: Record<string, unknown>): void {
    process.stdout.write(this.format("WARN", message, context) + "\n");
  }

  public error(message: string, context?: Record<string, unknown>): void {
    process.stderr.write(this.format("ERROR", message, context) + "\n");
  }

  public debug(message: string, context?: Record<string, unknown>): void {
    if (process.env.DEBUG) {
      process.stdout.write(this.format("DEBUG", message, context) + "\n");
    }
  }
}

export const logger = new StructuredLogger();
