<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';

const item = ref(null);
const route = useRoute();
const worldId = route.params.worldId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetch = async () => {
  try {
    item.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/abilities/${route.params.id}`).json();
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
            <div class="mb-4">
              <p class="text-justify" v-html="(item.description || 'No description available').replace(/\r\n|\n|\r|\u2028|\u2029/g, '<br>')"></p>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-2 text-sm">
            <p><strong class="text-gray-500">Тип:</strong> {{ item.type ?? '-' }}</p>
            <p><strong class="text-gray-500">Теги:</strong> {{ item.tags ?? '-' }}</p>
          </div>
        </div>
      </div>

      <div v-else class="text-center text-gray-500 mt-8">
        Ability not found.
      </div>
    </div>
  </div>
</template>
