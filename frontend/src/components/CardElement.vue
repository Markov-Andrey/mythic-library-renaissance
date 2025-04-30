<template>
  <div
    class="relative flex flex-col h-full bg-gray-100 rounded-xl shadow-md transition-all cursor-pointer hover:shadow-lg"
    @click="navigate"
  >
    <img
      v-if="imagePath && showImage"
      :src="`${apiBaseUrl}/${imagePath}`"
      alt="Card Image"
      class="w-full h-56 object-cover rounded-t-xl"
      @error="hideImage"
    />
    <div class="px-4 py-2">
      <h2 class="text-xl font-semibold">{{ title }}</h2>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  imagePath: {
    type: String,
    default: null
  },
  route: {
    type: String,
    required: true
  }
})

const router = useRouter()
const showImage = ref(true)
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL

const navigate = () => router.push(props.route)
const hideImage = () => (showImage.value = false)
</script>

<style scoped>
</style>
