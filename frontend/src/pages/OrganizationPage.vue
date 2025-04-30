<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';

const organization = ref(null);
const route = useRoute();
const organizationId = route.params.organizationId;
const worldId = route.params.worldId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchOrganization = async () => {
  try {
    organization.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/organizations/${organizationId}`).json();
  } catch (err) {
    console.error('Error fetching organization:', err);
  }
};

onMounted(() => {
  fetchOrganization();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-5xl px-4 py-6 mx-auto">
      <div v-if="organization">
        <div class="flex flex-col items-center">
          <img
            v-if="organization.logo_image_path"
            :src="`${apiBaseUrl}/${organization.logo_image_path}`"
            alt="Organization Logo"
            class="w-32 h-32 object-cover rounded-full mb-4"
          />
          <h1 class="text-4xl font-bold mb-4">{{ organization.name }}</h1>
          <p v-if="organization.description" class="text-lg mb-4">{{ organization.description }}</p>
          <p class="text-sm text-gray-500">
            Статус:
            <span :class="organization.status ? 'text-green-600' : 'text-red-600'">
              {{ organization.status ? 'Активна' : 'Неактивна' }}
            </span>
          </p>
          <p v-if="organization.tags" class="text-sm mt-2">
            Теги: <span>{{ organization.tags }}</span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
