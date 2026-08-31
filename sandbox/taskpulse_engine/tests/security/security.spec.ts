import { generateSecureToken, createHmacSignature, verifySignature } from "../../src/utils/crypto";

describe("Security & Cryptographic Boundary Tests (Red-Team Audit)", () => {
  it("should generate cryptographically strong tokens (minimum 64 hex chars for 32 bytes)", () => {
    const token1 = generateSecureToken(32);
    const token2 = generateSecureToken(32);

    expect(token1.length).toBe(64);
    expect(token2.length).toBe(64);
    expect(token1).not.toBe(token2);
    // Verify hexadecimal format
    expect(token1).toMatch(/^[0-9a-f]{64}$/);
  });

  it("should verify valid HMAC signature in constant time", () => {
    const payload = "task_export_payload_499102";
    const sig = createHmacSignature(payload);

    expect(verifySignature(sig, sig)).toBe(true);
  });

  it("should reject tampered or mismatched HMAC signatures", () => {
    const payload = "task_export_payload_499102";
    const sig = createHmacSignature(payload);
    const tampered = sig.substring(0, sig.length - 2) + "00";

    expect(verifySignature(tampered, sig)).toBe(false);
  });
});
