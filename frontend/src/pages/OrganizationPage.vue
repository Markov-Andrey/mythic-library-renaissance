<script setup>
import {onMounted, ref, watch} from 'vue';
import {useRoute, useRouter} from 'vue-router';
import ky from 'ky';
import ConfirmModal from "@/components/ConfirmModal.vue";

const route = useRoute();
const router = useRouter();
const worldId = route.params.worldId;
const organizationId = route.params.organizationId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const organization = ref(null);
const showCover = ref(true);
const images = ref([]);
const showConfirmModal = ref(false);

const fetchOrganization = async () => {
  try {
    const data = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/organizations/${organizationId}`).json();
    organization.value = data;
    images.value = data.images_json ? JSON.parse(data.images_json) : [];
    showCover.value = true;
  } catch {
    organization.value = null;
    images.value = [];
  }
};

const deleteConfirmed = async () => {
  try {
    await ky.delete(`${apiBaseUrl}/api/worlds/${worldId}/organizations/${route.params.organizationId}`);
    router.push(`/${worldId}/organizations`);
  } finally {
    showConfirmModal.value = false;
  }
};

const hideCover = () => {
  showCover.value = false;
};

watch(() => route.params.organizationId, fetchOrganization, { immediate: true });
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
          <div class="mb-4">
            <p class="text-justify" v-html="(organization.description || 'No description available').replace(/\r\n|\n|\r|\u2028|\u2029/g, '<br>')"></p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-2 text-sm text-gray-700">
            <p><strong>Тип:</strong> {{ organization.type || '-' }}</p>
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

      <div class="mt-6 flex gap-4">
        <router-link :to="`/${worldId}/organizations/${route.params.organizationId}/edit`" class="inline-block px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600">Редактировать</router-link>
        <button @click="showConfirmModal = true" class="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 cursor-pointer">Удалить</button>
        <router-link :to="`/${worldId}/organizations`" class="inline-block px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Назад</router-link>
      </div>

      <ConfirmModal
        :show="showConfirmModal"
        message="Вы уверены, что хотите удалить эту локацию?"
        @confirm="deleteConfirmed"
        @cancel="showConfirmModal = false"
      />
    </div>
  </div>
</template>
