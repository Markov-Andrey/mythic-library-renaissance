<script setup>
import { useRoute } from 'vue-router';
import AddFormElement from "../components/AddFormElement.vue";
import ky from "ky";
import { onMounted, ref, computed } from "vue";

const route = useRoute();
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const organisation = ref(null);

const worldId = route.params.worldId;
const organizationId = route.params.organizationId;

const fetchLocation = async () => {
  try {
    organisation.value = await ky
      .get(`${apiBaseUrl}/api/worlds/${worldId}/organizations/${organizationId}`)
      .json();
  } catch (err) {
    console.error('Error fetching organisation:', err);
  }
};

onMounted(() => {
  fetchLocation();
});

const fields = computed(() => {
  const org = organisation.value ?? {};
  return [
    { name: 'world_id', label: 'Мир', type: 'text', hidden: true, default: worldId },
    { name: 'organization_id', label: 'Организация', type: 'text', hidden: true, default: organizationId },
    { name: 'cover', label: 'Обложка', type: 'image', default: null },
    { name: 'name', label: 'Имя локации', type: 'text', required: true, default: org.name },
    { name: 'description', label: 'Описание орга', type: 'textarea', default: org.description },
    { name: 'type', label: 'Тип', type: 'text', default: org.type },
    { name: 'tags', label: 'Теги', type: 'text', default: org.tags },
    { name: 'status', label: 'Статус. Активна', type: 'checkbox', default: true },
    { name: 'images_json', label: 'Иллюстрации', type: 'images', default: [] }
  ];
});
</script>

<template>
  <AddFormElement
    :fields="fields"
    api-route="/api/organization_edit"
    :success-redirect="`/${worldId}/organizations`"
  />
</template>
