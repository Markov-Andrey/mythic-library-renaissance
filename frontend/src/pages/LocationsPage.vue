<script setup>
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';
import NewCardAdd from "@/components/NewCardAdd.vue";
import MiniCard from "@/components/MiniCard.vue";

const locations = ref([]);
const route = useRoute();
const worldId = route.params.id;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchLocations = async () => {
  try {
    const params = new URLSearchParams(route.query).toString();
    const url = `${apiBaseUrl}/api/worlds/${worldId}/locations${params ? '?' + params : ''}`;
    locations.value = await ky.get(url).json();
  } catch (err) {
    console.error('Error fetching locations:', err);
  }
};

onMounted(() => {
  fetchLocations();
});

watch(() => route.query, () => {
  fetchLocations();
}, { deep: true });
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
            :type="location.type"
            :tags="location.tags"
          />
        </div>
        <NewCardAdd :to="`/${worldId}/locations/locations-add`"/>
      </div>
    </div>
  </div>
</template>
