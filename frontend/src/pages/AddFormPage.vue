<script setup>
import { reactive } from 'vue';
import ky from 'ky';
import router from '@/router.js';

const props = defineProps({
  fields: Array,
  apiRoute: String,
  successRedirect: String,
});

const values = reactive({});
const files = reactive({});

// Инициализация значений по умолчанию
props.fields.forEach(field => {
  const isMultipleImage = field.type === 'images[]';

  // default значение
  values[field.name] = field.default ?? (isMultipleImage ? [] : '');

  if (['image', 'images[]'].includes(field.type)) {
    files[field.name] = null;
  }
});

const handleFileChange = (e, name, multiple) => {
  files[name] = multiple ? Array.from(e.target.files) : e.target.files[0];
};

const handleSubmit = async () => {
  const formData = new FormData();

  for (const field of props.fields) {
    if (['image', 'images[]'].includes(field.type)) {
      const file = files[field.name];
      if (file) {
        if (Array.isArray(file)) {
          file.forEach(f => formData.append(field.name, f));
        } else {
          formData.append(field.name, file);
        }
      }
    } else {
      formData.append(field.name, values[field.name]);
    }
  }

  try {
    const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
    await ky.post(`${apiBaseUrl}${props.apiRoute}`, { body: formData }).json();
    if (props.successRedirect) await router.push(props.successRedirect);
  } catch (err) {
    console.error('Form submission error:', err);
  }
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="p-6 bg-gray-100 rounded-xl shadow-md space-y-4">
    <div
      v-for="field in fields"
      :key="field.name"
      v-show="!field.hidden"
    >
      <label v-if="!field.hidden" class="block mb-1 font-semibold">{{ field.label }}</label>

      <input
        v-if="field.type === 'text' || field.type === 'number'"
        :type="field.type"
        v-model="values[field.name]"
        :required="field.required"
        class="w-full p-2 border border-gray-300 rounded-md"
      />

      <textarea
        v-else-if="field.type === 'textarea'"
        v-model="values[field.name]"
        :required="field.required"
        rows="4"
        class="w-full p-2 border border-gray-300 rounded-md"
      ></textarea>

      <input
        v-else-if="field.type === 'image'"
        type="file"
        accept="image/*"
        @change="e => handleFileChange(e, field.name, false)"
        class="w-full"
      />

      <input
        v-else-if="field.type === 'images[]'"
        type="file"
        multiple
        accept="image/*"
        @change="e => handleFileChange(e, field.name, true)"
        class="w-full"
      />
    </div>

    <div class="flex justify-between mt-6">
      <router-link to="/" class="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600">Отмена</router-link>
      <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">Сохранить</button>
    </div>
  </form>
</template>
