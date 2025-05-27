<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import MenuHeader from './components/MenuHeader.vue';

const route = useRoute();
const worldId = computed(() => route.params.worldId || route.params.id || null);
const showMenu = computed(() => Boolean(worldId.value));
</script>

<template>
  <div>
    <MenuHeader v-if="showMenu" />
    <main>
      <router-view />
    </main>
  </div>
</template>
