// src/utils/poiGenerator.js

export function generatePOIsWithRules(grid, poiTypes, rng) {
  const result = [];
  const forbidden = new Set();

  const distance = (a, b) => Math.max(Math.abs(a.x - b.x), Math.abs(a.y - b.y));
  const totalCells = grid.length;

  for (const poi of poiTypes) {
    const candidates = grid.filter(cell => poi.allowedTerrains.includes(cell.type));
    const shuffled = [...candidates].sort(() => rng() - 0.5);

    const count = Math.floor(poi.density / 100 * totalCells);
    let placed = 0;

    for (const cell of shuffled) {
      const key = `${cell.x},${cell.y}`;
      if (forbidden.has(key)) continue;

      const isNear = result.some(p => distance(p, cell) <= poi.spreadRadius);
      if (isNear) continue;

      result.push({ ...cell, poi });
      forbidden.add(key);

      placed++;
      if (placed >= count) break;
    }
  }

  return result;
}
