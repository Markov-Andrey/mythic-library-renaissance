<script setup>
import { useRoute } from 'vue-router';
import AddFormElement from "../components/AddFormElement.vue";
import ky from "ky";
import { onMounted, ref, computed } from "vue";

const route = useRoute();
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
const organisation = ref(null);
const worldId = route.params.worldId;

const fetchLocation = async () => {
  try {
    organisation.value = await ky
      .get(`${apiBaseUrl}/api/worlds/${worldId}/characters/${route.params.id}`)
      .json();
  } catch (err) {
    console.error('Error fetching organisation:', err);
  }
};

onMounted(() => {
  fetchLocation();
});

const fields = computed(() => {
  const object = organisation.value ?? {};
  return [
    { name: 'world_id', label: 'Мир', type: 'text', hidden: true, default: worldId },
    { name: 'id', label: 'Персонаж', type: 'text', hidden: true, default: route.params.id },
    { name: 'cover', label: 'Обложка', type: 'image', default: null },
    { name: 'name', label: 'Имя', type: 'text', required: true, default: object.name },
    { name: 'description', label: 'Описание', type: 'textarea', default: object.description },
    { name: 'age', label: 'Возраст', type: 'text', default: object.age },
    { name: 'gender', label: 'Пол', type: 'text', default: object.gender },
    { name: 'race', label: 'Раса', type: 'text', default: object.race },
    { name: 'type', label: 'Тип', type: 'text', default: object.type },
    { name: 'tags', label: 'Теги', type: 'text', default: object.tags },
    { name: 'character_class', label: 'Класс', type: 'text', default: object.character_class },
    { name: 'status', label: 'Статус. Жив', type: 'checkbox', default: true }
  ];
});
</script>

<template>
  <AddFormElement
    :fields="fields"
    api-route="/api/characters_edit"
    :success-redirect="`/${worldId}/characters`"
  />
</template>
