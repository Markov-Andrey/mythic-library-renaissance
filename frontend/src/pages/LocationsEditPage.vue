<script setup>
import { useRoute } from 'vue-router';
import AddFormElement from "../components/AddFormElement.vue";
import ky from "ky";
import { onMounted, ref, computed } from "vue";

const route = useRoute();
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const locationsArray = ref([]);
const location = ref(null);

const worldId = route.params.worldId;
const locationId = route.params.locationId;

const fetchLocationsArray = async () => {
  try {
    locationsArray.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/locations_array`).json();
  } catch (err) {
    console.error('Error fetching locations:', err);
  }
};

const fetchLocation = async () => {
  try {
    location.value = await ky
      .get(`${apiBaseUrl}/api/worlds/${worldId}/locations/${locationId}`)
      .json();
  } catch (err) {
    console.error('Error fetching location:', err);
  }
};

onMounted(() => {
  fetchLocationsArray();
  fetchLocation();
});

const fields = computed(() => {
  const loc = location.value ?? {};
  return [
    { name: 'world_id', label: 'Мир', type: 'text', hidden: true, default: worldId },
    { name: 'location_id', label: 'Локация', type: 'text', hidden: true, default: locationId },
    { name: 'cover', label: 'Обложка', type: 'image', default: null },
    { name: 'name', label: 'Имя локации', type: 'text', required: true, default: loc.name },
    {
      name: 'parent_location_id',
      label: 'Родительская локация',
      type: 'select',
      options: locationsArray.value,
      required: false,
      default: loc.parent_location_id
    },
    { name: 'description', label: 'Описание локации', type: 'textarea', default: loc.description },
    { name: 'type', label: 'Тип', type: 'text', default: loc.type },
    { name: 'tags', label: 'Теги', type: 'text', default: loc.tags },
    { name: 'images_json', label: 'Иллюстрации', type: 'images', default: [] }
  ];
});
</script>

<template>
  <AddFormElement
    :fields="fields"
    api-route="/api/location_edit"
    :success-redirect="`/${worldId}/locations`"
  />
</template>
