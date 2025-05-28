<template>
  <div v-if="tagsArray.length" class="absolute bottom-10 left-0 right-0 flex flex-wrap gap-1 p-2 rounded-b-xl pointer-events-none">
    <span
      v-for="(tag, index) in tagsArray"
      :key="index"
      @click="() => tagChange(tag)"
      class="hover:brightness-125 border border-black text-[10px] font-semibold px-2 py-0.5 rounded uppercase select-none bg-blue-300 pointer-events-auto cursor-pointer"
    >
      #{{ tag }}
    </span>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const props = defineProps({
  tags: String,
});

const route = useRoute();
const router = useRouter();

const tagsArray = computed(() => {
  if (!props.tags) return [];
  return props.tags.split(',').map(t => t.trim()).filter(Boolean);
});

const tagChange = (tag) => {
  const newQuery = { ...route.query };

  let currentTags = [];
  if (newQuery.tags) {
    if (Array.isArray(newQuery.tags)) {
      currentTags = [...newQuery.tags];
    } else {
      currentTags = [newQuery.tags];
    }
  }

  const tagIndex = currentTags.indexOf(tag);

  if (tagIndex !== -1) {
    currentTags.splice(tagIndex, 1);
  } else {
    currentTags.push(tag);
  }

  if (currentTags.length === 0) {
    delete newQuery.tags;
  } else {
    newQuery.tags = currentTags;
  }

  router.push({
    path: route.path,
    query: newQuery,
  });
};
</script>
