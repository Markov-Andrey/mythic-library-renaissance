<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';

const route = useRoute();
const worldId = route.params.worldId;
const locationId = route.params.locationId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const location = ref(null);
const showCover = ref(true);
const images = ref([]);

const fetchLocation = async () => {
  try {
    location.value = await ky
      .get(`${apiBaseUrl}/api/worlds/${worldId}/locations/${locationId}`)
      .json();

    if (location.value.images_json) {
      try {
        images.value = JSON.parse(location.value.images_json) || [];
      } catch {
        images.value = [];
      }
    }
  } catch {}
};

const hideCover = () => {
  showCover.value = false;
};

onMounted(() => {
  fetchLocation();
});
</script>

<template>
  <div class="max-w-3xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <div v-if="location">
      <div v-if="location.cover && showCover" class="mb-6">
        <img
          :src="`${apiBaseUrl}/${location.cover}`"
          alt="Location Cover"
          class="rounded w-full max-h-[300px] object-cover"
          @error="hideCover"
        />
      </div>

      <h1 class="text-3xl font-bold mb-4">{{ location.name }}</h1>
      <p class="mb-2"><strong>Type:</strong> {{ location.type || 'N/A' }}</p>
      <p class="mb-2"><strong>Tags:</strong> {{ location.tags || 'None' }}</p>
      <p class="mb-4"><strong>Description:</strong> {{ location.description || 'No description available' }}</p>

      <div v-if="images.length" class="grid grid-cols-2 gap-4">
        <img
          v-for="(img, index) in images"
          :key="index"
          :src="`${apiBaseUrl}/${img}`"
          alt="Location image"
          class="rounded w-full max-h-64 object-cover"
          loading="lazy"
        />
      </div>

      <div class="mt-6">
        <router-link
          :to="`/${worldId}/locations/${locationId}/edit`"
          class="inline-block px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600"
        >
          Редактировать
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
