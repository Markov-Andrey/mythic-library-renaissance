<!-- components/SearchInput.vue -->
<template>
  <div>
    <label class="block mb-1 font-semibold">{{ label }}</label>
    <input
      :id="id"
      v-model="modelValueLocal"
      type="text"
      :placeholder="placeholder"
      class="px-3 py-1 border border-gray-300 rounded-md"
      @input="$emit('update:modelValue', modelValueLocal)"
    />
  </div>
</template>

<script>
export default {
  name: "SearchInput",
  props: {
    id: {
      type: String,
      default: "search-input",
    },
    modelValue: {
      type: String,
      default: "",
    },
    placeholder: {
      type: String,
      default: "Search...",
    },
    label: {
      type: String,
      default: "Search:",
    },
  },
  computed: {
    modelValueLocal: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit("update:modelValue", value);
      },
    },
  },
};
</script>
