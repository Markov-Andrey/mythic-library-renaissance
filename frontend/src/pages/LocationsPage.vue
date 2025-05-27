<script setup>
import {onMounted, ref} from 'vue';
import {useRoute} from 'vue-router';
import ky from 'ky';
import NewCardAdd from "@/components/NewCardAdd.vue";
import MiniCard from "@/components/MiniCard.vue";
import {w} from "@3d-dice/dice-box/dist/Dice.js";

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
    <div class="w-full max-w-7xl px-2 py-6 mx-auto">
      <div class="grid grid-cols-5 gap-3">
        <div v-for="location in locations">
          <MiniCard
            :to="`locations/${location.id}`"
            :cover="location.cover"
            :name="location.name"
          />
        </div>
        <NewCardAdd :to="`/${worldId}/locations/locations-add`"/>
      </div>
    </div>
  </div>
</template>
