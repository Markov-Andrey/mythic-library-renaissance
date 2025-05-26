<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const worldId = computed(() => route.params.worldId || route.params.id || null);

const showMenu = computed(() => Boolean(worldId.value));

const menuItems = computed(() => [
  { name: 'World', path: `/${worldId.value}` },
  { name: 'Локации', path: `/${worldId.value}/locations` },
  { name: 'Организации', path: `/${worldId.value}/organizations` },
  { name: 'Персонажи', path: `/${worldId.value}/characters` },
  { name: 'Предметы', path: `/${worldId.value}/items` },
]);

const currentPath = computed(() => route.path);
</script>

<template>
  <header v-if="showMenu" class="bg-gray-900 text-gray-300 p-4 shadow-md">
    <nav class="max-w-5xl mx-auto flex gap-6">
      <router-link
        v-for="item in menuItems"
        :key="item.name"
        :to="item.path"
        :class="[
          'px-5 py-2 rounded-md font-semibold transition-colors duration-300',
          currentPath === item.path
            ? 'bg-teal-600 text-white shadow-md'
            : 'text-gray-400 hover:text-teal-400 hover:bg-gray-800'
        ]"
      >
        {{ item.name }}
      </router-link>
    </nav>
  </header>

  <main>
    <router-view />
  </main>
</template>

<style scoped>
</style>
