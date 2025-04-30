<script setup>
import {onMounted, ref} from 'vue';
import {useRoute} from 'vue-router';
import ky from 'ky';

const route = useRoute();
const worldId = route.params.worldId;
const locationId = route.params.locationId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const location = ref(null);
const showImage = ref(true);
const images = ref([]);  // Массив изображений

const fetchLocation = async () => {
  try {
    location.value = await ky
        .get(`${apiBaseUrl}/api/worlds/${worldId}/locations/${locationId}`)
        .json();

    // Преобразуем images_json в массив
    if (location.value.images_json) {
      try {
        images.value = JSON.parse(location.value.images_json) || [];
      } catch (error) {
        console.error('Error parsing images JSON:', error);
        images.value = [];
      }
    }
  } catch (err) {
    console.error('Error fetching location:', err);
  }
};

const hideImage = () => {
  showImage.value = false;
};

onMounted(() => {
  fetchLocation();
});
</script>

<template>
  <div class="max-w-3xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <div v-if="location">
      <h1 class="text-3xl font-bold mb-4">{{ location.name }}</h1>
      <p class="mb-2"><strong>Type:</strong> {{ location.type || 'N/A' }}</p>
      <p class="mb-2"><strong>Tags:</strong> {{ location.tags || 'None' }}</p>
      <p class="mb-4"><strong>Description:</strong> {{ location.description || 'No description available' }}</p>

      <div v-if="images.length && showImage" class="mb-4">
        <img
            v-if="images[0]"
            :src="`${apiBaseUrl}/${images[0]}`"
            class="rounded w-full max-h-96 object-cover"
            alt="Location Cover"
            @error="hideImage"
        />
      </div>

    </div>
  </div>
</template>

<style scoped>
</style>
