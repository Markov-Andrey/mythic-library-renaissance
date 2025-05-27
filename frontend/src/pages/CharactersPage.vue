<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ky from 'ky';
import NewCardAdd from "@/components/NewCardAdd.vue";
import MiniCard from "@/components/MiniCard.vue";

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
    <div class="w-full max-w-7xl px-2 py-6 mx-auto">
      <div class="grid grid-cols-4 gap-8">
        <div v-for="character in characters">
          <MiniCard
            :to="`/${worldId}/characters/${character.id}`"
            :cover="character.photo_path"
            :name="character.name"
          />
        </div>
        <NewCardAdd
          :to="`/${worldId}/characters/characters-add`"
        />
      </div>
    </div>
  </div>
</template>