<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';

const route = useRoute();
const worldId = route.params.worldId;
const organizationId = route.params.organizationId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const organization = ref(null);
const showCover = ref(true);
const images = ref([]);

const fetchOrganization = async () => {
  try {
    organization.value = await ky
        .get(`${apiBaseUrl}/api/worlds/${worldId}/organizations/${organizationId}`)
        .json();

    if (organization.value.images_json) {
      try {
        images.value = JSON.parse(organization.value.images_json) || [];
      } catch (error) {
        console.error('Error parsing images JSON:', error);
        images.value = [];
      }
    }
  } catch (err) {
    console.error('Error fetching organization:', err);
  }
};

const hideCover = () => {
  showCover.value = false;
};

onMounted(() => {
  fetchOrganization();
});
</script>

<template>
  <div class="min-h-screen bg-gray-100 py-10 px-4 text-gray-800">
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-6">

      <div v-if="organization" class="flex flex-col sm:flex-row gap-6">
        <div class="flex-shrink-0" v-if="organization.cover && showCover">
          <img
              :src="`${apiBaseUrl}/${organization.cover}`"
              alt="Organization Cover"
              class="w-48 h-48 object-cover rounded-lg shadow"
              @error="hideCover"
          />
        </div>

        <div class="flex-1 space-y-4">
          <h1 class="text-3xl font-bold text-gray-900">{{ organization.name }}</h1>
          <p class="text-gray-600 whitespace-pre-line" v-if="organization.description">
            {{ organization.description }}
          </p>
          <p v-else class="text-gray-500 italic">Описание отсутствует.</p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-2 text-sm text-gray-700">
            <p><strong>Теги:</strong> {{ organization.tags || '-' }}</p>
            <p><strong>Статус:</strong> {{ organization.status ? 'Активна' : 'Неактивна' }}</p>
          </div>
        </div>
      </div>

      <div v-if="images.length" class="mt-8">
        <h2 class="text-xl font-semibold mb-4">Gallery</h2>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
          <img
              v-for="(img, index) in images"
              :key="index"
              :src="`${apiBaseUrl}/${img}`"
              alt="Organization image"
              class="rounded w-full max-h-48 object-cover"
              loading="lazy"
          />
        </div>
      </div>

      <div v-if="!organization" class="text-center text-gray-500 mt-8">
        Организация не найдена.
      </div>

    </div>
  </div>
</template>
