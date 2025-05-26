<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';

const character = ref(null);
const route = useRoute();
const characterId = route.params.characterId;
const worldId = route.params.worldId;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchCharacter = async () => {
  try {
    character.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/characters/${characterId}`).json();
  } catch (err) {
    console.error('Error fetching character:', err);
  }
};

onMounted(() => {
  fetchCharacter();
});
</script>

<template>
  <div class="min-h-screen bg-gray-100 py-10 px-4 text-gray-800">
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-6">
      <div v-if="character" class="flex flex-col sm:flex-row gap-6">
        <div class="flex-shrink-0">
          <img
            v-if="character.photo_path"
            :src="`${apiBaseUrl}/${character.photo_path}`"
            alt="Character Photo"
            class="w-40 h-40 object-cover rounded-lg shadow"
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

      <div v-else class="text-center text-gray-500 mt-8">
        Персонаж не найден.
      </div>
    </div>
  </div>
</template>
