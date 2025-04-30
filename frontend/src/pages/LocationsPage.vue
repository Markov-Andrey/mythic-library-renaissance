<script setup>
import {onMounted, ref} from 'vue';
import {useRoute} from 'vue-router';
import ky from 'ky';
import LocationElement from '../components/LocationElement.vue';

const locations = ref([]);
const route = useRoute();
const worldId = route.params.id;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchLocations = async () => {
  try {
    locations.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/locations`).json();
  } catch (err) {
    console.error('Error fetching locations:', err);
  }
};

onMounted(() => {
  fetchLocations();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-5xl px-4 py-6 mx-auto">
      <h1 class="text-3xl font-bold mb-4">Иерархия локаций</h1>
      <div v-if="locations.length">
        <LocationElement
            v-for="location in locations"
            :key="location.id"
            :location="location"
            :worldId="worldId"
        />
      </div>
      <div v-else class="text-gray-500">Нет локаций</div>
    </div>
  </div>
</template>
