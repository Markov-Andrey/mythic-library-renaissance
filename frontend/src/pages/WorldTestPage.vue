<script setup>
import { ref } from 'vue';
import HexElement from "@/components/HexElement.vue";
import { terrainColors } from "@/utils/terrain";
import { generateGrid, getCellStyle } from "@/utils/terrainGenerator";

const cols = 25, rows = 15;
const h = 50;
const w = h * 0.866;
const oy = h * 0.75;
const seed = Math.random().toString(36).substring(2, 12);
// const seed = 'Andre';
const biome = "continental";

const hoveredCoords = ref(null);
const grid = generateGrid(cols, rows, seed, biome);
const style = ({x, y}) => getCellStyle(x, y, w, oy);
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
