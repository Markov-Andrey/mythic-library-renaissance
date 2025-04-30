<script setup>
import {onMounted, ref} from 'vue';
import {useRoute} from 'vue-router';
import ky from 'ky';
import NewCardAdd from "@/components/NewCardAdd.vue";
import CardElement from "@/components/CardElement.vue";

const organizations = ref([]);
const route = useRoute();
const worldId = route.params.id;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchLocations = async () => {
  try {
    organizations.value = await ky.get(`${apiBaseUrl}/api/worlds/${worldId}/organizations`).json();
  } catch (err) {
    console.error('Error fetching locations:', err);
  }
};

onMounted(() => {
  fetchLocations();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-5xl px-4 py-6 mx-auto">
      <h1 class="text-3xl font-bold mb-4">Организации</h1>
      <div v-if="organizations.length" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <CardElement
          v-for="organization in organizations"
          :key="organization.id"
          :title="organization.name"
          :route="`/${worldId}/organizations/${organization.id}`"
          :imagePath="organization.logo_image_path"
        />
        <NewCardAdd to="/organizations-add"/>
      </div>
    </div>
  </div>
</template>
