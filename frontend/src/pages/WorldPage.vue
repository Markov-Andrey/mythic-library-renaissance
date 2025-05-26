<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';

const world = ref(null);
const showImage = ref(true);
const route = useRoute();
const worldId = route.params.id;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchWorld = async () => {
  try {
    world.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}`).json();
  } catch (err) {
    console.error('Error fetching world:', err);
  }
};

const hideImage = () => {
  showImage.value = false;
};

onMounted(() => {
  fetchWorld();
});
</script>

<template>
  <div class="p-6 bg-gray-100 rounded-xl shadow-md max-w-7xl mx-auto mt-6">
    <div v-if="world" class="flex space-x-8">
      <div v-if="world.cover" class="w-1/3">
        <img
          v-if="showImage"
          :src="`${apiBaseUrl}/${world.cover}`"
          alt="World Cover"
          class="w-full h-auto object-cover rounded-xl"
          @error="hideImage"
        />
      </div>
      <div class="flex-1 space-y-4">
        <h1 class="text-3xl font-bold mb-4">{{ world?.name || 'Заголовок не найден' }}</h1>
        <p><strong>Описание:</strong> {{ world.description || 'Нет описания' }}</p>
        <p><strong>Визуальный стиль:</strong> {{ world.visual_style || 'Не задано' }}</p>
        <p><strong>Теги:</strong> {{ world.tags || 'Нет тегов' }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
