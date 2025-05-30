<template>
  <div class="relative">
  <router-link
    :to="to"
    class="flex flex-col h-full bg-gray-100 rounded-xl shadow-md transition-all cursor-pointer group hover:brightness-125 hover:shadow-lg no-underline text-inherit"
  >
    <div class="relative w-full h-56 rounded-t-xl overflow-hidden bg-gray-200">
      <img
        v-if="cover && showImage"
        :src="`${apiBaseUrl}/${cover}`"
        alt="World Cover"
        class="w-full h-full object-cover"
        @error="hideImage"
      />
    </div>
    <div class="px-4 py-2">
      <h2 class="name-heading">
        {{ name }}
      </h2>
    </div>
  </router-link>
  <TypeElement :type="type" />
  <TagList :tags="tags" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import TagList from './TagList.vue';
import TypeElement from './TypeElement.vue';

const props = defineProps({
  to: { type: String, required: true },
  cover: String,
  name: { type: String, required: true },
  tags: String,
  type: String,
});

const showImage = ref(true);
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const hideImage = () => {
  showImage.value = false;
};
</script>

<style scoped>
.name-heading {
  font-weight: 600;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: clamp(0.9rem, 1.2vw, 1.25rem);
  line-height: 1.2;
  min-height: calc(1.2em * 2);
}
</style>
