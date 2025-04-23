<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-7xl px-6 py-10 mx-auto">
      <h1 class="text-4xl font-bold text-gray-900 mb-8">Библиотека миров</h1>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">

        <WorldCard
          v-for="world in worlds"
          :key="world.id"
          :world="world"
        />

        <div class="bg-gray-100 p-6 rounded-xl shadow-md hover:shadow-lg transition-all flex items-center justify-center cursor-pointer hover:brightness-125 group">
          <div class="rounded-full bg-blue-300 w-20 h-20 flex items-center justify-center group-hover:bg-blue-400 transition-colors">
            <svg class="w-12 h-12 text-white group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 5v14M5 12h14"></path>
            </svg>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import WorldCard from '../components/WorldCard.vue';

const worlds = [
  { id: 1, name: 'Blood & Chrome', cover_image_path: 'storage/worlds/kAoC3uOj5RW23a71XkSgSa5UwJQTnA0HigyNmap6.jpg' },
];
</script>

<style scoped>
</style>
