// terrainGenerator.js
import { globalBiomes, terrainTypes, generateParams } from "@/utils/terrain";
import seedrandom from 'seedrandom';

export function generateGrid(cols, rows, seed, biome = 'temperate_forest') {
  const rng = seedrandom(seed);
  const allowedTypes = globalBiomes[biome] || terrainTypes;
  return Array.from({ length: cols * rows }, (_, i) => {
    const y = Math.floor(i / cols);
    const x = i % cols;
    const type = allowedTypes[Math.floor(rng() * allowedTypes.length)];
    return { x, y, type, params: generateParams(type, rng) };
  });
}

export function getCellStyle(x, y, w, oy) {
  return {
    width: `${w}px`,
    height: `${w}px`,
    left: `${x * w}px`,
    top: `${y * oy}px`,
    transform: y % 2 ? `translateX(${w / 2}px)` : "none",
  };
}
