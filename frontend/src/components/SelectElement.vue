<script setup>
const props = defineProps({
  modelValue: [String, Number],
  options: {
    type: Array,
    default: () => [],
  },
  label: String,
  id: String,
  placeholder: {
    type: String,
    default: 'Select an option',
  },
});

const emit = defineEmits(['update:modelValue']);

function onChange(event) {
  emit('update:modelValue', event.target.value);
}
</script>

<template>
  <div>
    <label :for="id" class="block mb-1 font-semibold">{{ label }}</label>
    <select
      :id="id"
      :value="modelValue"
      @change="onChange"
      class="border border-gray-300 rounded px-2 py-1 w-full"
    >
      <option value="">{{ placeholder }}</option>
      <option v-for="option in options" :key="option" :value="option">
        {{ option }}
      </option>
    </select>
  </div>
</template>
