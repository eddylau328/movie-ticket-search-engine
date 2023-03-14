export function roundToNearestHalf(f: number): number {
  const inv = 1.0 / 0.5;
  return Math.round(f * inv) / inv;
}
