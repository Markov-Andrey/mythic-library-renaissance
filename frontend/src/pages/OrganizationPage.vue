<script setup>
import {onMounted, ref} from 'vue';
import {useRoute} from 'vue-router';
import ky from 'ky';

const route = useRoute();
const worldId = route.params.worldId;
const organizationId = route.params.organizationId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const organization = ref(null);
const showCover = ref(true);
const images = ref([]);

const fetchLocation = async () => {
  try {
    organization.value = await ky
        .get(`${apiBaseUrl}/api/worlds/${worldId}/organizations/${organizationId}`)
        .json();

    if (organization.value.images_json) {
      try {
        images.value = JSON.parse(organization.value.images_json) || [];
      } catch (error) {
        console.error('Error parsing images JSON:', error);
        images.value = [];
      }
    }
  } catch (err) {
    console.error('Error fetching location:', err);
  }
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
    <div v-if="organization">
      <div v-if="organization.cover && showCover" class="mb-6">
        <img
            :src="`${apiBaseUrl}/${organization.cover}`"
            alt="Location Cover"
            class="rounded w-full max-h-[300px] object-cover"
            @error="hideCover"
        />
      </div>

      <h1 class="text-3xl font-bold mb-4">{{ organization.name }}</h1>
      <p class="mb-2"><strong>Tags:</strong> {{ organization.tags || 'None' }}</p>
      <p class="mb-4"><strong>Description:</strong> {{ organization.description || 'No description available' }}</p>
      <p class="mb-4"><strong>Status:</strong> {{ organization.status ? 'Activity' : 'No activity' }}</p>

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
    </div>
  </div>
</template>

<style scoped>
</style>
