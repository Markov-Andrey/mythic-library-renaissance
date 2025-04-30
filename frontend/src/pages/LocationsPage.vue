<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';
import LocationsCard from "@/components/LocationsCard.vue";
import NewCardAdd from '../components/NewCardAdd.vue';

const world = ref(null);
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
    <div class="w-full max-w-7xl px-2 py-2 mx-auto">
      <h1 class="text-4xl font-bold text-gray-900">Locations Library</h1>
      <hr class="p-1">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">

        <LocationsCard
          v-for="location in locations"
          :key="location.id"
          :location="location"
        />
        <NewCardAdd to="/locations-add"/>

      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
