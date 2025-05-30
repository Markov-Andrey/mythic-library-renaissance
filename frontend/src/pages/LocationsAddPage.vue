<script setup>
import { useRoute } from 'vue-router';
import AddFormElement from "../components/AddFormElement.vue";
import ky from "ky";
import { onMounted, ref, computed } from "vue";

const route = useRoute();
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
const locationsArray = ref([]);
const worldId = route.params.worldId;

const fetchLocationsArray = async () => {
  try {
    locationsArray.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/locations/array`).json();
  } catch (err) {
    console.error('Error fetching locations:', err);
  }
};

onMounted(() => {
  fetchLocationsArray();
});

const fields = computed(() => [
  { name: 'world_id', label: 'Мир', type: 'text', hidden: true, default: worldId },
  { name: 'cover', label: 'Обложка', type: 'image' },
  { name: 'name', label: 'Имя локации', type: 'text', required: true },
  { name: 'parent_location_id', label: 'Родительская локация', type: 'select', options: locationsArray.value, required: false },
  { name: 'description', label: 'Описание локации', type: 'textarea' },
  { name: 'type', label: 'Тип', type: 'text' },
  { name: 'tags', label: 'Теги', type: 'text' },
  { name: 'images_json', label: 'Иллюстрации', type: 'images' }
]);
</script>

<template>
  <AddFormElement
    :fields="fields"
    api-route="/api/add/locations"
    :success-redirect="`/${worldId}/locations`"
  />
</template>
