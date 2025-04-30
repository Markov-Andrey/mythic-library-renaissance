<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  to: {
    type: String,
    required: true
  }
});
</script>

<template>
  <router-link :to="to" class="bg-gray-100 p-6 rounded-xl shadow-md hover:shadow-lg transition-all flex items-center justify-center cursor-pointer hover:brightness-125 group">
    <div class="rounded-full bg-blue-300 w-20 h-20 flex items-center justify-center group-hover:bg-blue-400 transition-colors">
      <svg class="w-12 h-12 text-white group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 5v14M5 12h14"></path>
      </svg>
    </div>
  </router-link>
</template>

<style scoped>

</style>
