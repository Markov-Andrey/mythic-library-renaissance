<script setup>
  import AddFormPage from "@/pages/AddFormPage.vue";
</script>

<template>
  <AddFormPage
    :fields="[
      { name: 'name', label: 'Имя мира', type: 'text', required: true },
      { name: 'description', label: 'Описание мира', type: 'textarea' },
      { name: 'visual_style', label: 'Визуальный стиль', type: 'text' },
      { name: 'tags', label: 'Теги', type: 'text' },
      { name: 'cover', label: 'Обложка', type: 'image' }
    ]"
    api-route="/api/worlds_add"
    success-redirect="/"
  />
</template>

<style scoped>
</style>
