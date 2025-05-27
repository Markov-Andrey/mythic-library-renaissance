<template>
  <div v-if="tagsArray.length" class="absolute bottom-0 left-0 right-0 flex flex-wrap gap-1 p-2 rounded-b-xl">
    <span
      v-for="(tag, index) in tagsArray"
      :key="index"
      class="border border-black text-[10px] font-semibold px-2 py-0.5 rounded uppercase select-none bg-blue-300"
    >
      {{ tag.trim() }}
    </span>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  tags: String,
});

const tagsArray = computed(() => {
  if (!props.tags) return [];
  return props.tags.split(',').map(t => t.trim()).filter(Boolean);
});
</script>
