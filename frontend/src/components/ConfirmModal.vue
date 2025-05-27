<script setup>
import { defineEmits, defineProps } from 'vue';

const props = defineProps({
  show: Boolean,
  message: {
    type: String,
    default: 'Вы уверены?'
  },
});

const emit = defineEmits(['confirm', 'cancel']);
</script>

<template>
  <div
    v-if="show"
    class="fixed inset-0 bg-white/20 backdrop-blur-sm flex items-center justify-center z-50"
  >
    <div class="bg-white rounded-lg p-6 w-full max-w-sm text-center shadow-lg">
      <p class="text-lg font-medium mb-4">{{ message }}</p>
      <div class="flex justify-around mt-4">
        <button
          @click="$emit('confirm')"
          class="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
        >
          Ok
        </button>
        <button
          @click="$emit('cancel')"
          class="px-4 py-2 bg-gray-300 text-gray-800 rounded hover:bg-gray-400"
        >
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>
