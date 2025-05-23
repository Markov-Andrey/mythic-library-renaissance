<script setup>
  import AddFormElement from "../components/AddFormElement.vue";
</script>

<template>
  <AddFormElement
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
