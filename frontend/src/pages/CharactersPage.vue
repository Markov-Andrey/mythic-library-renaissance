<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';
import NewCardAdd from "@/components/NewCardAdd.vue";
import CardElement from "@/components/CardElement.vue";

const characters = ref([]);
const route = useRoute();
const worldId = route.params.id;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchCharacters = async () => {
  try {
    characters.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/characters`).json();
  } catch (err) {
    console.error('Error fetching characters:', err);
  }
};

onMounted(() => {
  fetchCharacters();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-5xl px-4 py-6 mx-auto">
      <h1 class="text-3xl font-bold mb-4">Персонажи</h1>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <CardElement
          v-for="character in characters"
          :key="character.id"
          :title="character.name"
          :route="`/${worldId}/characters/${character.id}`"
          :imagePath="character.photo_path"
        />
        <NewCardAdd :to="`/${worldId}/characters/characters-add`"/>
      </div>
    </div>
  </div>
</template>

