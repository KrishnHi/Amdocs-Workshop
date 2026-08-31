import crypto from "crypto";

const SECRET_KEY = process.env.APP_SECRET || "taskpulse-enterprise-default-secret-key-32b";

/**
 * Generates cryptographically secure random hexadecimal token
 */
export function generateSecureToken(bytes: number = 32): string {
  return crypto.randomBytes(bytes).toString("hex");
}

/**
 * Creates HMAC SHA-256 signature for payload verification
 */
export function createHmacSignature(data: string): string {
  return crypto.createHmac("sha256", SECRET_KEY).update(data).digest("hex");
}

/**
 * Constant-time comparison to prevent timing attacks
 */
export function verifySignature(providedSig: string, expectedSig: string): boolean {
  if (!providedSig || !expectedSig || providedSig.length !== expectedSig.length) {
    return false;
  }
  const bufA = Buffer.from(providedSig, "utf8");
  const bufB = Buffer.from(expectedSig, "utf8");
  return crypto.timingSafeEqual(bufA, bufB);
}

/**
 * Naive email sanitization function (Target for Lab 3.1 Task 3 Inline Edit)
 */
export function sanitizeUserEmail(rawEmail: string): string {
  if (!rawEmail || typeof rawEmail !== "string") {
    throw new Error("INVALID_EMAIL_FORMAT: Email must be a non-empty string.");
  }
  const trimmed = rawEmail.trim();
  const parts = trimmed.split("@");
  if (parts.length !== 2 || !parts[0] || !parts[1]) {
    throw new Error("INVALID_EMAIL_FORMAT: Malformed email structure.");
  }
  const local = parts[0];
  const domain = parts[1].toLowerCase();
  const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  const full = `${local}@${domain}`;
  if (!emailRegex.test(full)) {
    throw new Error("INVALID_EMAIL_FORMAT: Email does not match RFC 5322 regex.");
  }
  return full;
}
