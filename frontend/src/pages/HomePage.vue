<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-7xl px-2 py-2 mx-auto">
      <h1 class="text-4xl font-bold text-gray-900">Worlds Library</h1>
      <hr class="p-1">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">

        <WorldCard
          v-for="world in worlds"
          :key="world.id"
          :world="world"
        />

        <WorldAdd/>

      </div>
    </div>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue';
import ky from 'ky';
import WorldCard from '../components/WorldCard.vue';
import WorldAdd from '../components/WorldAdd.vue';

const worlds = ref([]);
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchWorlds = async () => {
  try {
    worlds.value = await ky.get(`${apiBaseUrl}/worlds`).json();
  } catch (error) {
    console.error('Ошибка при получении данных:', error);
  }
};

onMounted(() => {
  fetchWorlds();
});
</script>

<style scoped>
</style>

<style scoped>
</style>
