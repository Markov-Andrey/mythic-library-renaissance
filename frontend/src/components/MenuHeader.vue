<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const worldId = computed(() => route.params.worldId || route.params.id || null);

const menuItems = computed(() => [
  { name: 'World', path: `/${worldId.value}` },
  { name: 'Locations', path: `/${worldId.value}/locations` },
  { name: 'Organizations', path: `/${worldId.value}/organizations` },
  { name: 'Characters', path: `/${worldId.value}/characters` },
  { name: 'Items', path: `/${worldId.value}/items` },
  { name: 'Abilities', path: `/${worldId.value}/abilities` },
]);

const currentPath = computed(() => route.path);
</script>

<template>
  <div class="pt-8"></div>
  <header class="fixed top-0 left-0 right-0 bg-gray-900 text-gray-300 py-1 shadow-md z-50">
    <nav class="max-w-5xl mx-auto flex">
      <router-link
        v-for="item in menuItems"
        :key="item.name"
        :to="item.path"
        :class="[
          'flex-1 text-center py-2 rounded-md font-semibold transition-colors duration-300',
          currentPath === item.path
            ? 'bg-teal-600 text-white shadow-md'
            : 'text-gray-400 hover:text-teal-400 hover:bg-gray-800'
        ]"
      >
        {{ item.name }}
      </router-link>
    </nav>
  </header>
</template>

<style scoped>
</style>
