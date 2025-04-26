<template>
  <div
    class="relative flex flex-col h-full bg-gray-100 rounded-xl shadow-md transition-all cursor-pointer group hover:shadow-lg"
    @click="goToWorldDetails"
  >
    <div
      class="absolute top-2 right-2 z-10 opacity-0 group-hover:opacity-100 transition"
      @click.stop="toggleMenu"
    >
      <div class="w-8 h-8 rounded-full bg-white shadow flex items-center justify-center hover:bg-gray-200 transition">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-700" fill="currentColor" viewBox="0 0 20 20">
          <circle cx="10" cy="4" r="1.5"/>
          <circle cx="10" cy="10" r="1.5"/>
          <circle cx="10" cy="16" r="1.5"/>
        </svg>
      </div>

      <div v-if="menuOpen" class="absolute right-0 mt-2 w-32 bg-white rounded-lg shadow-lg z-20 text-sm overflow-hidden">
        <button @click="goToWorldDetails" class="w-full text-left px-4 py-2 hover:bg-gray-100">Смотреть</button>
        <button @click="editWorld" class="w-full text-left px-4 py-2 hover:bg-gray-100">Изменить</button>
        <button @click="deleteWorld" class="w-full text-left px-4 py-2 hover:bg-gray-100 text-red-500">Удалить</button>
      </div>
    </div>

    <img
      v-if="world.cover_image_path && showImage"
      :src="`${apiBaseUrl}/${world.cover_image_path}`"
      alt="World Cover"
      class="w-full h-56 object-cover rounded-t-xl"
      @error="hideImage"
    />
    <div class="px-4 py-2">
      <h2 class="text-xl font-semibold">{{ world.name }}</h2>
      <p class="text-gray-600 mt-1 text-sm">{{ world.description }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  world: {
    type: Object,
    required: true
  }
})

const router = useRouter()
const showImage = ref(true)
const menuOpen = ref(false)
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const goToWorldDetails = () => router.push(`/${props.world.id}`);
const editWorld = () => console.log(`Edit world with ID: ${props.world.id}`)
const deleteWorld = () => console.log(`Delete world with ID: ${props.world.id}`)
const hideImage = () => showImage.value = false
const toggleMenu = () => menuOpen.value = !menuOpen.value

document.addEventListener('click', () => menuOpen.value = false)
</script>

<style scoped>
</style>
