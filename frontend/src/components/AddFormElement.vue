<script setup>
import { reactive, watch } from 'vue';
import ky from 'ky';
import router from '@/router.js';

const props = defineProps({
  fields: Array,
  apiRoute: String,
  successRedirect: String,
});

const values = reactive({});
const files = reactive({});

watch(() => props.fields, (newFields) => {
  Object.keys(values).forEach(key => delete values[key]);
  Object.keys(files).forEach(key => delete files[key]);

  newFields.forEach(field => {
    const isMultipleImage = field.type === 'images';

    if (field.type === 'select') {
      if (field.default !== undefined) {
        values[field.name] = field.default;
      } else if (field.options && field.options.length > 0) {
        values[field.name] = field.options[0].id;
      } else {
        values[field.name] = '';
      }
    } else if (field.type === 'checkbox') {
      values[field.name] = field.default ?? false;
    } else if (['image', 'images'].includes(field.type)) {
      files[field.name] = null;
      values[field.name] = field.default ?? (isMultipleImage ? [] : '');
    } else {
      values[field.name] = field.default ?? '';
    }
  });
}, {immediate: true});

const handleFileChange = (e, name, multiple) => {
  files[name] = multiple ? Array.from(e.target.files) : e.target.files[0];
};

const handleSubmit = async () => {
  const formData = new FormData();

  for (const field of props.fields) {
    if (['image', 'images'].includes(field.type)) {
      const file = files[field.name];
      if (file) {
        if (Array.isArray(file)) {
          file.forEach(f => formData.append(field.name, f));
        } else {
          formData.append(field.name, file);
        }
      }
    } else {
      let value = values[field.name];
      if (typeof value === 'boolean') {
        value = value ? 'true' : 'false';
      }
      formData.append(field.name, value);
    }
  }

  try {
    const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
    await ky.post(`${apiBaseUrl}${props.apiRoute}`, {body: formData}).json();
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
      <label
          v-if="field.type !== 'checkbox' && !field.hidden"
          class="block mb-1 font-semibold"
      >
        {{ field.label }}
      </label>

      <input
          v-if="field.type === 'text' || field.type === 'number'"
          :type="field.type"
          v-model="values[field.name]"
          :required="field.required"
          class="w-full p-2 border border-gray-300 rounded-md"
      />

      <textarea
          v-if="field.type === 'textarea'"
          v-model="values[field.name]"
          class="w-full min-h-[100px] p-2 border border-gray-300 rounded-md"
      ></textarea>

      <input
          v-else-if="field.type === 'image'"
          type="file"
          accept="image/*"
          @change="e => handleFileChange(e, field.name, false)"
          class="w-full"
      />

      <input
          v-else-if="field.type === 'images'"
          type="file"
          multiple
          accept="image/*"
          @change="e => handleFileChange(e, field.name, true)"
          class="w-full"
      />

      <select
        v-else-if="field.type === 'select'"
        v-model="values[field.name]"
        :required="field.required"
        class="w-full p-2 border border-gray-300 rounded-md"
      >
        <option :value="null">—</option>
        <option
          v-for="option in field.options"
          :key="option.id"
          :value="option.id"
        >
          {{ option.name }}
        </option>
      </select>

      <label
          v-else-if="field.type === 'checkbox'"
          class="inline-flex items-center gap-2 cursor-pointer"
      >
        <input
            type="checkbox"
            v-model="values[field.name]"
            class="w-5 h-5 text-blue-600 border-gray-300 rounded"
        />
        {{ field.label }}
      </label>
    </div>

    <div class="flex justify-between mt-6">
      <button
          @click="router.back()"
          type="button"
          class="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600"
      >
        Назад
      </button>
      <button
          type="submit"
          class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
      >
        Сохранить
      </button>
    </div>
  </form>
</template>
