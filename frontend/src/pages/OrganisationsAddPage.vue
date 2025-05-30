<script setup>
import { useRoute } from 'vue-router';
import AddFormElement from "../components/AddFormElement.vue";
import { computed } from "vue";

const route = useRoute();
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
const worldId = route.params.worldId;


const fields = computed(() => [
  { name: 'world_id', label: 'Мир', type: 'text', hidden: true, default: worldId },
  { name: 'cover', label: 'Обложка', type: 'image' },
  { name: 'name', label: 'Имя организации', type: 'text', required: true },
  { name: 'type', label: 'Тип организации', type: 'text' },
  { name: 'description', label: 'Описание', type: 'textarea' },
  { name: 'tags', label: 'Теги', type: 'text' },
  { name: 'images_json', label: 'Галерея', type: 'images' },
  { name: 'status', label: 'Статус. Активна', type: 'checkbox', default: true }
]);
</script>

<template>
  <AddFormElement
    :fields="fields"
    api-route="/api/organizations/add"
    :success-redirect="`/${worldId}/organizations`"
  />
</template>
