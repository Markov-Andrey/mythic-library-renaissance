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
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-5xl px-4 py-6 mx-auto">
      <div v-if="character">
        <div class="flex flex-col items-center">
          <img
            v-if="character.photo_path"
            :src="`${apiBaseUrl}/${character.photo_path}`"
            alt="Character Photo"
            class="w-32 h-32 object-cover rounded-full mb-4"
          />
          <h1 class="text-4xl font-bold mb-4">{{ character.name }}</h1>
          <p v-if="character.description" class="text-lg mb-4 text-center whitespace-pre-line">
            {{ character.description }}
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm text-gray-600">
            <p><strong>Тип:</strong> {{ character.type ?? '-' }}</p>
            <p><strong>Возраст:</strong> {{ character.age ?? '-' }}</p>
            <p><strong>Пол:</strong> {{ character.gender ?? '-' }}</p>
            <p><strong>Раса:</strong> {{ character.race ?? '-' }}</p>
            <p><strong>Класс:</strong> {{ character.character_class ?? '-' }}</p>
            <p>
              <strong>Статус: </strong>
              <span :class="character.status ? 'text-green-600' : 'text-red-600'">
                {{ character.status ? 'Активен' : 'Неактивен' }}
              </span>
            </p>
          </div>
        </div>
      </div>
      <div v-else class="text-center text-gray-500 mt-8">Персонаж не найден.</div>
    </div>
  </div>
</template>
