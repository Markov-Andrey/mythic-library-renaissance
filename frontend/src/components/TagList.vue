<template>
  <div v-if="tagsArray.length" class="absolute bottom-[20%] left-0 right-0 flex flex-wrap gap-1 p-2 rounded-b-xl pointer-events-none">
    <span
      v-for="(tag, index) in tagsArray"
      :key="index"
      @click="() => tagChange(tag)"
      :class="['hover:brightness-125 border border-black text-[10px] font-semibold px-2 py-0.5 rounded uppercase select-none pointer-events-auto cursor-pointer', { 'bg-blue-600 text-white': isActive(tag), 'bg-blue-300': !isActive(tag) }]"
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

const isActive = (tag) => {
  if (!route.query.tags) return false;
  if (Array.isArray(route.query.tags)) {
    return route.query.tags.includes(tag);
  }
  return route.query.tags === tag;
};

const tagChange = (tag) => {
  const newQuery = {...route.query};
  if (isActive(tag)) {
    delete newQuery.tags;
  } else {
    newQuery.tags = tag;
  }
  router.push({
    path: route.path,
    query: newQuery,
  });
};
</script>
