<script setup>
import { ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ky from 'ky';
import ConfirmModal from '../components/ConfirmModal.vue';

const route = useRoute();
const router = useRouter();
const worldId = route.params.worldId;
const location = ref(null);
const showCover = ref(true);
const images = ref([]);
const showConfirmModal = ref(false);

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchLocation = async () => {
  try {
    const data = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/locations/${route.params.locationId}`).json();
    location.value = data;
    images.value = data.images_json ? JSON.parse(data.images_json) : [];
    showCover.value = true;
  } catch {
    location.value = null;
    images.value = [];
  }
};

const deleteConfirmed = async () => {
  try {
    await ky.delete(`${apiBaseUrl}/api/worlds/${worldId}/locations/${route.params.locationId}`);
    router.push(`/${worldId}/locations`);
  } finally {
    showConfirmModal.value = false;
  }
};

const hideCover = () => showCover.value = false;

watch(() => route.params.locationId, fetchLocation, { immediate: true });
</script>

<template>
  <div v-if="location" class="max-w-3xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <div v-if="location.cover && showCover" class="mb-6">
      <img :src="`${apiBaseUrl}/${location.cover}`" alt="Location Cover" class="rounded w-full max-h-[300px] object-cover" @error="hideCover" />
    </div>

    <h1 class="text-3xl font-bold mb-4">{{ location.name }}</h1>
    <p><strong>Type:</strong> {{ location.type || 'N/A' }}</p>
    <p><strong>Tags:</strong> {{ location.tags || 'None' }}</p>
    <div class="mb-4">
      <p class="text-justify" v-html="(location.description || 'No description available').replace(/\r\n|\n|\r|\u2028|\u2029/g, '<br>')"></p>
    </div>

    <div v-if="images.length" class="grid grid-cols-2 gap-4 mb-4">
      <img v-for="(img, i) in images" :key="i" :src="`${apiBaseUrl}/${img}`" alt="Location image" class="rounded w-full max-h-64 object-cover" loading="lazy" />
    </div>

    <div>
      <strong>Родительская локация: </strong>
      <span v-if="location.parent">
        <router-link :to="`/${worldId}/locations/${location.parent.id}`" class="text-blue-600 hover:underline">{{ location.parent.name }}</router-link>
      </span>
      <span v-else>Отсутствует</span>
    </div>

    <div class="mt-4">
      <strong>Дочерние локации:</strong>
      <ul v-if="location.children?.length" class="list-disc list-inside mt-2">
        <li v-for="child in location.children" :key="child.id">
          <router-link :to="`/${worldId}/locations/${child.id}`" class="text-blue-600 hover:underline">{{ child.name }}</router-link>
        </li>
      </ul>
      <p v-else class="mt-2 text-gray-500">Отсутствуют</p>
    </div>

    <div class="mt-6 flex gap-4">
      <router-link :to="`/${worldId}/locations/${route.params.locationId}/edit`" class="inline-block px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600">Редактировать</router-link>
      <button @click="showConfirmModal = true" class="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 cursor-pointer">Удалить</button>
      <router-link :to="`/${worldId}/locations`" class="inline-block px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Назад</router-link>
    </div>

    <ConfirmModal
      :show="showConfirmModal"
      message="Вы уверены, что хотите удалить эту организацию?"
      @confirm="deleteConfirmed"
      @cancel="showConfirmModal = false"
    />
  </div>
</template>
