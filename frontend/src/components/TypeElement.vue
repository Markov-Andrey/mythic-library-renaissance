<template>
  <div
    v-if="type"
    class="absolute top-0 left-0 right-0 flex flex-wrap gap-1 p-2 rounded-t-xl pointer-events-none"
  >
    <div
      @click="typeChange"
      :class="[
        'hover:brightness-125 border border-black text-[10px] font-semibold px-2 py-0.5 rounded uppercase select-none pointer-events-auto cursor-pointer',
        isActiveType ? 'bg-green-600 text-white' : 'bg-green-300'
      ]"
    >
      {{ type }}
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const props = defineProps({
  type: String
});

const router = useRouter();
const route = useRoute();

const isActiveType = computed(() => {
  return route.query.type === props.type;
});

const typeChange = () => {
  const newQuery = { ...route.query };

  if (isActiveType.value) {
    delete newQuery.type;
  } else {
    newQuery.type = props.type;
  }

  router.push({
    path: route.path,
    query: newQuery,
  });
};
</script>
