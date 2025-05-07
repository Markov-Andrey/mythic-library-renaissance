<script setup>
import { ref } from 'vue';
import HexElement from "@/components/HexElement.vue";

const cols = 10, rows = 10;
const h = 50;
const w = h * 0.866;
const oy = h * 0.75;

const hoveredCoords = ref(null);

const terrainTypes = ['meadow', 'forest', 'swamp', 'mountain', 'desert', 'water', 'savanna'];
const terrainColors = {
  meadow: 'fill-[#A8E6A1]',
  forest: 'fill-[#6BBF59]',
  mountain: 'fill-[#B0A7A3]',
  desert: 'fill-[#F0C28C]',
  water: 'fill-[#A4D8F7]',
  swamp: 'fill-[#6B8E23]',
  savanna: 'fill-[#D4C86C]',
};
/*
Biome     | Fertility | Humidity | Temperature | Plant Biomass
--------------------------------------------------------------
forest    |   80–100  |   60–80  |    50–70    |     80–100
meadow    |   50–100  |   30–80  |    50–70    |     40–80
swamp     |   60–100  |   90–100 |    50–60    |     70–90
water     |   0–10    |   100    |    50–70    |     10–20
savanna   |   30–60   |   30–50  |    60–80    |     30–50
desert    |   10–20   |   0–20   |    70–100   |     5–15
mountain  |   20–40   |   20–40  |    30–50    |     10–20
 */
const generateParams = (type) => {
  switch (type) {
    case 'meadow':
      return {
        fertility: Math.floor(Math.random() * 51) + 50,
        humidity: Math.floor(Math.random() * 51) + 30,
        temperature: Math.floor(Math.random() * 21) + 50,
        plantBiomass: Math.floor(Math.random() * 41) + 40
      };
    case 'forest':
      return {
        fertility: Math.floor(Math.random() * 21) + 80,
        humidity: Math.floor(Math.random() * 21) + 60,
        temperature: Math.floor(Math.random() * 21) + 50,
        plantBiomass: Math.floor(Math.random() * 21) + 80
      };
    case 'swamp':
      return {
        fertility: Math.floor(Math.random() * 41) + 60,
        humidity: Math.floor(Math.random() * 11) + 90,
        temperature: Math.floor(Math.random() * 11) + 50,
        plantBiomass: Math.floor(Math.random() * 21) + 70
      };
    case 'mountain':
      return {
        fertility: Math.floor(Math.random() * 21) + 20,
        humidity: Math.floor(Math.random() * 21) + 20,
        temperature: Math.floor(Math.random() * 21) + 30,
        plantBiomass: Math.floor(Math.random() * 11) + 10
      };
    case 'desert':
      return {
        fertility: Math.floor(Math.random() * 11) + 10,
        humidity: Math.floor(Math.random() * 21),
        temperature: Math.floor(Math.random() * 31) + 70,
        plantBiomass: Math.floor(Math.random() * 11) + 5
      };
    case 'water':
      return {
        fertility: Math.floor(Math.random() * 11),
        humidity: 100,
        temperature: Math.floor(Math.random() * 21) + 50,
        plantBiomass: Math.floor(Math.random() * 11) + 10
      };
    case 'savanna':
      return {
        fertility: Math.floor(Math.random() * 31) + 30,
        humidity: Math.floor(Math.random() * 21) + 30,
        temperature: Math.floor(Math.random() * 21) + 60,
        plantBiomass: Math.floor(Math.random() * 21) + 30
      };
    default:
      return {};
  }
};

// Генерация сетки с типами местности и их параметрами
const grid = Array.from({ length: cols * rows }, (_, i) => {
  const y = Math.floor(i / cols);
  const x = i % cols;
  const type = terrainTypes[Math.floor(Math.random() * terrainTypes.length)];
  return { x, y, type, params: generateParams(type) };
});

// Стиль для клетки
const style = ({x, y}) => ({
  width: `${w}px`,
  height: `${h}px`,
  left: `${x * w}px`,
  top: `${y * oy}px`,
  transform: y % 2 ? `translateX(${w / 2}px)` : "none",
});
</script>

<template>
  <div class="flex gap-10 p-4">
    <div class="relative" :style="{ width: `${cols * w}px`, height: `${rows * oy + h * 0.25}px` }">
      <div
          v-for="cell in grid"
          :key="`${cell.x}-${cell.y}`"
          class="absolute"
          :style="style(cell)"
          :data-x="cell.x"
          :data-y="cell.y"
          @mouseenter="hoveredCoords = cell"
          @mouseleave="hoveredCoords = null"
      >
        <HexElement :class="terrainColors[cell.type]"/>
      </div>
    </div>

    <button
        class="bg-blue-400 h-20 w-40 rounded-lg text-white font-semibold text-lg shadow-sm hover:bg-blue-500 active:bg-blue-600 active:scale-95 transition-all duration-150 cursor-pointer">
      Тик
    </button>

    <div
      v-if="hoveredCoords"
      class="fixed bottom-8 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white px-4 py-2 rounded shadow text-sm font-mono"
    >
      x: {{ hoveredCoords.x }}, y: {{ hoveredCoords.y }} — {{ hoveredCoords.type }}
      <div class="mt-1">
        <div v-for="(val, key) in hoveredCoords.params" :key="key">
          {{ key }}: {{ val }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
