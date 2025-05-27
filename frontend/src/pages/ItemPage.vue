<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';

const item = ref(null);
const route = useRoute();
const itemId = route.params.itemId;
const worldId = route.params.worldId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetch = async () => {
  try {
    item.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/items/${itemId}`).json();
  } catch (err) {
    console.error('Error fetching item:', err);
  }
};

onMounted(() => {
  fetch();
});
</script>

<template>
  <div class="min-h-screen bg-gray-100 py-10 px-4 text-gray-800">
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-6">
      <div v-if="item" class="flex flex-col sm:flex-row gap-6">
        <div class="flex-shrink-0 w-full sm:w-auto">
          <img
            v-if="item.cover"
            :src="`${apiBaseUrl}/${item.cover}`"
            alt="Item Cover"
            class="w-full max-w-md max-h-[400px] object-contain rounded-lg shadow mx-auto mb-6"
          />
        </div>

        <div class="flex-1 space-y-4">
          <div>
            <h1 class="text-3xl font-bold text-gray-900">{{ item.name }}</h1>
            <p v-if="item.description" class="mt-2 text-gray-600 whitespace-pre-line">
              {{ item.description }}
            </p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-2 text-sm">
            <p><strong class="text-gray-500">Тип:</strong> {{ item.type ?? '-' }}</p>
            <p><strong class="text-gray-500">Ценность:</strong> {{ item.value ?? '-' }}</p>
            <p><strong class="text-gray-500">Вес:</strong> {{ item.weight ?? '-' }}</p>
          </div>
        </div>
      </div>

      <div v-else class="text-center text-gray-500 mt-8">
        Предмет не найден.
      </div>
    </div>
  </div>
</template>
