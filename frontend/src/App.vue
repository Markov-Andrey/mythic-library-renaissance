<script setup>
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'

onMounted(() => {
    initFlowbite();
})
</script>

<template>
  <header>
  </header>
  <main>
    <router-view></router-view>
  </main>
</template>

<style scoped>
</style>
