<script setup>
import { ref } from 'vue';
import HexElement from "@/components/HexElement.vue";
import { terrainColors } from "@/utils/terrain";
import { generateGrid, getCellStyle } from "@/utils/terrainGenerator";
import { POI_TYPES } from "@/utils/poi.js";
import { generatePOIsWithRules } from "@/utils/poiGenerator";
import seedrandom from "seedrandom";

const cols = 25, rows = 15;
const h = 50;
const w = h * 0.866;
const oy = h * 0.75;
const seed = Math.random().toString(36).substring(2, 12);
const biome = "continental";
const rng = seedrandom(seed);

const hoveredCoords = ref(null);

const grid = generateGrid(cols, rows, rng, biome);
const style = ({ x, y }) => getCellStyle(x, y, w, oy);

const pois = generatePOIsWithRules(grid, POI_TYPES, rng);
const poiMap = new Map(pois.map(p => [`${p.x},${p.y}`, p]));

function handleMouseEnter(cell) {
  const poi = poiMap.get(`${cell.x},${cell.y}`);
  if (poi) {
    hoveredCoords.value = {
      x: cell.x,
      y: cell.y,
      type: cell.type,
      params: cell.params,
      poi: poi.poi,
    };
  } else {
    hoveredCoords.value = {
      x: cell.x,
      y: cell.y,
      type: cell.type,
      params: cell.params,
      poi: null,
    };
  }
}

function handleMouseLeave() {
  hoveredCoords.value = null;
}
</script>

<template>
  <div class="flex gap-10 p-4">
    <div
      class="relative"
      :style="{ width: `${cols * w}px`, height: `${rows * oy + h * 0.25}px` }"
    >
      <div
        v-for="cell in grid"
        :key="`${cell.x}-${cell.y}`"
        class="absolute"
        :style="style(cell)"
        :data-x="cell.x"
        :data-y="cell.y"
        @mouseenter="handleMouseEnter(cell)"
        @mouseleave="handleMouseLeave"
      >
        <HexElement :class="`fill-[${terrainColors[cell.type]}]`" />
        <component
          v-if="poiMap.has(`${cell.x},${cell.y}`)"
          :is="poiMap.get(`${cell.x},${cell.y}`).poi.icon"
          class="absolute top-1 left-1 w-6 h-6 text-yellow-400 drop-shadow"
        />
      </div>
    </div>

    <button
      class="bg-blue-400 h-20 w-40 rounded-lg text-white font-semibold text-lg shadow-sm hover:bg-blue-500 active:bg-blue-600 active:scale-95 transition-all duration-150 cursor-pointer"
    >
      Тик
    </button>

    <div
      v-if="hoveredCoords"
      class="fixed bottom-8 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white px-4 py-2 rounded shadow text-sm font-mono"
    >
      <div v-if="hoveredCoords.type">
        <p>x: {{ hoveredCoords.x }}, y: {{ hoveredCoords.y }} — {{ hoveredCoords.type }}</p>
        <div class="mt-1">
          <div v-for="(val, key) in hoveredCoords.params" :key="key">
            {{ key }}: {{ val }}
          </div>
        </div>
      </div>

      <div v-if="hoveredCoords.poi" class="mt-3 text-yellow-300">
        <p><strong>POI: {{ hoveredCoords.poi.name }}</strong></p>
        <p>{{ hoveredCoords.poi.description }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
