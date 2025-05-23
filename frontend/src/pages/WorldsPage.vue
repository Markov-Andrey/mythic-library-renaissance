<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-7xl px-2 py-2 mx-auto">
      <h1 class="text-4xl font-bold text-gray-900">Worlds Library</h1>
      <hr class="p-1">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <div v-for="world in worlds">
          <MiniCard
            :to="`/${world.id}`"
            :cover="world.cover"
            :name="world.name"
          />
        </div>
        <NewCardAdd to="/worlds-add"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue';
import ky from 'ky';
import NewCardAdd from '../components/NewCardAdd.vue';
import MiniCard from "@/components/MiniCard.vue";

const worlds = ref([]);
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchWorlds = async () => {
  try {
    worlds.value = await ky.get(`${apiBaseUrl}/api/worlds`).json();
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
