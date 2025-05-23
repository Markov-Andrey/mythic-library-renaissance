<template>
  <router-link
    :to="to"
    class="relative flex flex-col h-full bg-gray-100 rounded-xl shadow-md transition-all cursor-pointer group hover:shadow-lg no-underline text-inherit"
  >
    <img
      v-if="cover && showImage"
      :src="`${apiBaseUrl}/${cover}`"
      alt="World Cover"
      class="w-full h-56 object-cover rounded-t-xl"
      @error="hideImage"
    />
    <div class="px-4 py-2">
      <h2 class="text-xl font-semibold">{{ name }}</h2>
    </div>
  </router-link>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  to: {
    type: String,
    required: true
  },
  cover: {
    type: String
  },
  name: {
    type: String,
    required: true
  }
})

const showImage = ref(true)
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL

const hideImage = () => {
  showImage.value = false
}
</script>

<style scoped>
</style>
