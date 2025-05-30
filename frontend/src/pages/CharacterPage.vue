<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';
import ConfirmModal from "@/components/ConfirmModal.vue";
import router from "@/router.js";

const character = ref(null);
const route = useRoute();
const worldId = route.params.worldId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
const showConfirmModal = ref(false);

const fetchCharacter = async () => {
  try {
    character.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/characters/${route.params.id}`).json();
  } catch (err) {
    console.error('Error fetching character:', err);
  }
};

const deleteConfirmed = async () => {
  try {
    await ky.delete(`${apiBaseUrl}/api/worlds/${worldId}/characters/${route.params.id}`);
    router.push(`/${worldId}/characters`);
  } finally {
    showConfirmModal.value = false;
  }
};

onMounted(() => {
  fetchCharacter();
});
</script>

<template>
  <div class="min-h-screen bg-gray-100 py-10 px-4 text-gray-800">
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-6">

      <template v-if="character">
        <div class="flex flex-col sm:flex-row gap-6">
          <div class="flex-shrink-0 w-full sm:w-auto">
            <img
              v-if="character.cover"
              :src="`${apiBaseUrl}/${character.cover}`"
              alt="Item Cover"
              class="w-full max-w-md max-h-[400px] object-contain rounded-lg shadow mx-auto mb-6"
            />
          </div>

          <div class="flex-1 space-y-4">
            <div>
              <h1 class="text-3xl font-bold text-gray-900">{{ character.name }}</h1>
              <p v-if="character.description" class="mt-2 text-gray-600 whitespace-pre-line">
                {{ character.description }}
              </p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-2 text-sm">
              <p><strong class="text-gray-500">Тип: </strong>{{ character.type ?? '-' }}</p>
              <p><strong class="text-gray-500">Возраст: </strong>{{ character.age ?? '-' }}</p>
              <p><strong class="text-gray-500">Пол: </strong>{{ character.gender ?? '-' }}</p>
              <p><strong class="text-gray-500">Раса: </strong>{{ character.race ?? '-' }}</p>
              <p><strong class="text-gray-500">Класс: </strong>{{ character.character_class ?? '-' }}</p>
              <p>
                <strong class="text-gray-500">Статус: </strong>
                <span :class="character.status ? 'text-green-600' : 'text-red-600'">
                  {{ character.status ? 'Alive' : 'Dead' }}
                </span>
              </p>
            </div>
          </div>
        </div>

        <div class="mt-6 flex gap-4">
          <router-link :to="`/${worldId}/characters/${route.params.id}/edit`" class="inline-block px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600">Редактировать</router-link>
          <button @click="showConfirmModal = true" class="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 cursor-pointer">Удалить</button>
          <router-link :to="`/${worldId}/characters`" class="inline-block px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Назад</router-link>
        </div>

        <ConfirmModal
          :show="showConfirmModal"
          message="Вы уверены, что хотите удалить этого персонажа?"
          @confirm="deleteConfirmed"
          @cancel="showConfirmModal = false"
        />
      </template>

      <div v-else class="text-center text-gray-500 mt-8">
        Персонаж не найден.
      </div>

    </div>
  </div>
</template>
