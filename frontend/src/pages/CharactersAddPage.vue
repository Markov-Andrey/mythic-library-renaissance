<script setup>
import {useRoute} from 'vue-router';
import AddFormElement from "../components/AddFormElement.vue";
import {onMounted, computed} from "vue";

const route = useRoute();
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
const worldId = route.params.worldId;

onMounted(() => {
});

const fields = computed(() => [
  {name: 'world_id', label: 'Мир', type: 'text', hidden: true, default: worldId},
  {name: 'photo_path', label: 'Фото', type: 'image'},
  {name: 'name', label: 'Имя персонажа', type: 'text', required: true},
  {name: 'description', label: 'Описание', type: 'textarea'},
  {name: 'type', label: 'Тип', type: 'text'},
  {name: 'age', label: 'Возраст', type: 'number'},
  {name: 'gender', label: 'Пол', type: 'text'},
  {name: 'race', label: 'Раса', type: 'text'},
  {name: 'character_class', label: 'Класс персонажа', type: 'text'},
  {name: 'status', label: 'Активен', type: 'checkbox', default: true}
]);
</script>

<template>
  <AddFormElement
      :fields="fields"
      api-route="/api/character_add"
      :success-redirect="`/${worldId}/characters`"
  />
</template>
