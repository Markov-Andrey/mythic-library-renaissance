<template>
  <div
    class="flex flex-col h-full bg-gray-100 hover:brightness-125 rounded-xl shadow-md hover:shadow-lg transition-all cursor-pointer"
    @click="goToWorldDetails"
  >
    <img
      :src="world.cover_image_path"
      alt="World Cover"
      class="w-full h-56 object-cover rounded-xl"
    />
    <div class="rounded-xl flex justify-center my-4">
      <h2 class="text-xl font-semibold">{{ world.name }}</h2>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

defineProps({
  world: {
    type: Object,
    required: true
  }
})

const router = useRouter();

const goToWorldDetails = () => {
  // router.push({ name: 'world-details', params: { id: world.id } });
}
</script>

<style scoped>
</style>
