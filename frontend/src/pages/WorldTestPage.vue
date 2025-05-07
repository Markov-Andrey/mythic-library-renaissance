<script setup>
import { ref } from 'vue';
import HexElement from "@/components/HexElement.vue";

const cols = 10, rows = 10;
const h = 50;
const w = h * 0.866;
const oy = h * 0.75;

const hoveredCoords = ref(null);

const terrainTypes = ['meadow', 'forest', 'mountain', 'desert', 'water'];
const terrainColors = {
  meadow: 'fill-[#A8E6A1]',
  forest: 'fill-[#6BBF59]',
  mountain: 'fill-[#B0A7A3]',
  desert: 'fill-[#F0C28C]',
  water: 'fill-[#A4D8F7]',
};

const grid = Array.from({ length: cols * rows }, (_, i) => {
  const y = Math.floor(i / cols);
  const x = i % cols;
  const type = terrainTypes[Math.floor(Math.random() * terrainTypes.length)];
  return { x, y, type };
});

const style = ({ x, y }) => ({
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
        <HexElement :class="terrainColors[cell.type]" />
      </div>
    </div>

    <button class="bg-blue-400 h-20 w-40 rounded-lg text-white font-semibold text-lg shadow-sm hover:bg-blue-500 active:bg-blue-600 active:scale-95 transition-all duration-150 cursor-pointer">
      Тик
    </button>

    <div
        v-if="hoveredCoords"
        class="fixed bottom-8 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white px-4 py-2 rounded shadow"
      >
        x: {{ hoveredCoords.x }}, y: {{ hoveredCoords.y }} — {{ hoveredCoords.type }}
      </div>
  </div>
</template>
