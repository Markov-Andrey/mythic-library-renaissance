<script setup>
import {onMounted, ref, watch} from 'vue';
import {useRoute, useRouter} from 'vue-router';
import ky from 'ky';
import NewCardAdd from "@/components/NewCardAdd.vue";
import MiniCard from "@/components/MiniCard.vue";

const locations = ref([]);
const locationsTypes = ref([]);
const locationsTags = ref([]);

const route = useRoute();
const router = useRouter();
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

const fetchLocationsTypes = async () => {
  try {
    const url = `${apiBaseUrl}/api/worlds/${worldId}/location-types`;
    locationsTypes.value = await ky.get(url).json();
  } catch (err) {
    console.error('Error fetching location types:', err);
  }
};

const fetchLocationsTags = async () => {
  try {
    const url = `${apiBaseUrl}/api/worlds/${worldId}/location-tags`;
    locationsTags.value = await ky.get(url).json();
  } catch (err) {
    console.error('Error fetching location tags:', err);
  }
};

const selectedType = ref(route.query.type || '');
const selectedTags = ref(route.query.tags || '');

watch(() => route.query, () => {
  fetchLocations();
  selectedType.value = route.query.type || '';
  selectedTags.value = route.query.tags || '';
}, {deep: true});

watch(selectedType, (newType) => {
  const newQuery = {...route.query};
  if (newType) {
    newQuery.type = newType;
  } else {
    delete newQuery.type;
  }
  router.push({path: route.path, query: newQuery});
});

watch(selectedTags, (newTags) => {
  const newQuery = {...route.query};
  if (newTags) {
    newQuery.tags = newTags;
  } else {
    delete newQuery.tags;
  }
  router.push({path: route.path, query: newQuery});
});

onMounted(() => {
  fetchLocationsTypes();
  fetchLocationsTags();
  fetchLocations();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-7xl px-2 py-6 mx-auto">
      <div class="flex gap-2">
        <div class="mb-4">
          <label for="type-select" class="block mb-1 font-semibold">Filter by Type:</label>
          <select
              id="type-select"
              v-model="selectedType"
              class="border border-gray-300 rounded px-2 py-1"
          >
            <option value="">All types</option>
            <option v-for="type in locationsTypes" :key="type" :value="type">
              {{ type }}
            </option>
          </select>
        </div>

        <div class="mb-6">
          <label for="tags-select" class="block mb-1 font-semibold">Filter by Tag:</label>
          <select
              id="tags-select"
              v-model="selectedTags"
              class="border border-gray-300 rounded px-2 py-1"
          >
            <option value="">All tags</option>
            <option v-for="tag in locationsTags" :key="tag" :value="tag">
              {{ tag }}
            </option>
          </select>
        </div>
      </div>

      <div class="grid grid-cols-5 gap-3">
        <div v-for="location in locations" :key="location.id">
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
