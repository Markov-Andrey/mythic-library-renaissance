<script setup>
import {onMounted, ref} from 'vue';
import {useRoute} from 'vue-router';
import ky from 'ky';
import NewCardAdd from "@/components/NewCardAdd.vue";
import MiniCard from "@/components/MiniCard.vue";

const items = ref([]);
const route = useRoute();
const worldId = route.params.id;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetch = async () => {
  try {
    items.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/items`).json();
  } catch (err) {
    console.error('Error fetching items:', err);
  }
};

onMounted(() => {
  fetch();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-7xl px-2 py-2 mx-auto">
      <h1 class="text-4xl font-bold text-gray-900">Items</h1>
      <hr class="p-1">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <div v-for="item in items">
          <MiniCard
            :to="`items/${item.id}`"
            :cover="item.cover"
            :name="item.name"
          />
        </div>
        <NewCardAdd :to="`/${worldId}/items/items-add`"/>
      </div>
    </div>
  </div>
</template>
