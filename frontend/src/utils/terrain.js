// terrain.js
export const terrainTypes = [
  'meadow',
  'forest_coniferous',
  'forest_deciduous',
  'forest_mixed',
  'swamp',
  'mountain',
  'desert',
  'water',
  'savanna',
];

export const terrainColors = {
  meadow: 'fill-[#A8E6A1]',
  forest_coniferous: 'fill-[#4C8C4A]',
  forest_deciduous: 'fill-[#6BBF59]',
  forest_mixed: 'fill-[#589E63]',
  mountain: 'fill-[#B0A7A3]',
  desert: 'fill-[#F0C28C]',
  water: 'fill-[#A4D8F7]',
  swamp: 'fill-[#6B8E23]',
  savanna: 'fill-[#D4C86C]'
};

export const globalBiomes = {
  continental: [
  'meadow',
  'meadow',
  'meadow',
  'forest_coniferous',
  'forest_deciduous',
  'forest_mixed',
  'swamp',
  'mountain',
  'water',
  ]
};

export const generateParams = (type, rng = Math.random) => {
  const rand = (min, max) => Math.floor(rng() * (max - min + 1)) + min;

  const biomeRanges = {
    meadow:            [[50, 100], [30, 80],  [50, 70],  [40, 80]],
    forest_coniferous: [[80, 100], [60, 75],  [45, 60],  [80, 100]],
    forest_deciduous:  [[80, 100], [65, 80],  [55, 70],  [80, 100]],
    forest_mixed:      [[80, 100], [60, 80],  [50, 70],  [80, 100]],
    swamp:             [[60, 100], [90, 100], [50, 60],  [70, 90]],
    mountain:          [[20, 40],  [20, 40],  [30, 50],  [10, 20]],
    desert:            [[10, 20],  [0, 20],   [70, 100], [5, 15]],
    water:             [[0, 10],   [100, 100],[50, 70],  [10, 20]],
    savanna:           [[30, 60],  [30, 50],  [60, 80],  [30, 50]],
  };

  const keys = ['fertility', 'humidity', 'temperature', 'plantBiomass'];
  const ranges = biomeRanges[type];
  if (!ranges) return {};

  return Object.fromEntries(
    keys.map((key, i) => [key, rand(...ranges[i])])
  );
};
