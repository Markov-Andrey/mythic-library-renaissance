<script setup>
import { useRoute } from 'vue-router';
import AddFormPage from "@/pages/AddFormPage.vue";

const route = useRoute();
const worldId = route.params.worldId;
</script>

<template>
  <AddFormPage
    :fields="[
      { name: 'world', label: 'Мир', type: 'text', hidden: true, default: worldId },
      { name: 'cover', label: 'Обложка', type: 'image' },
      { name: 'name', label: 'Имя локации', type: 'text', required: true },
      { name: 'description', label: 'Описание локации', type: 'textarea' },
      { name: 'type', label: 'Тип', type: 'text' },
      { name: 'tags', label: 'Теги', type: 'text' },
      { name: 'images_json', label: 'Иллюстрации', type: 'image' }
    ]"
    api-route="/api/location_add"
    :success-redirect="`/${worldId}/locations`"
  />
</template>

<style scoped>
</style>
