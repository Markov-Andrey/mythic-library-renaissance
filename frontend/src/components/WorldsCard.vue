<template>
  <div
    class="relative flex flex-col h-full bg-gray-100 rounded-xl shadow-md transition-all cursor-pointer hover:shadow-lg"
    @click="goToWorldDetails"
  >
    <img
      v-if="world.cover && showImage"
      :src="`${apiBaseUrl}/${world.cover}`"
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
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL

const goToWorldDetails = () => router.push(`/${props.world.id}`)
const hideImage = () => showImage.value = false
</script>

<style scoped>
</style>
