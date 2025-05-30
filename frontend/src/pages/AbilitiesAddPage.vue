<script setup>
import {useRoute} from 'vue-router';
import AddFormElement from "../components/AddFormElement.vue";
import {onMounted, ref, computed} from "vue";

const route = useRoute();
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
const worldId = route.params.worldId;

onMounted(() => {
});

const fields = computed(() => [
  { name: 'world_id', label: 'Мир', type: 'text', hidden: true, default: worldId },
  { name: 'cover', label: 'Обложка', type: 'image' },
  { name: 'name', label: 'Название способности', type: 'text', required: true },
  { name: 'description', label: 'Описание', type: 'textarea' },
  { name: 'type', label: 'Тип', type: 'text' },
  { name: 'tags', label: 'Теги', type: 'text' },
]);
</script>

<template>
  <AddFormElement
      :fields="fields"
      api-route="/api/add/abilities"
      :success-redirect="`/${worldId}/abilities`"
  />
</template>
