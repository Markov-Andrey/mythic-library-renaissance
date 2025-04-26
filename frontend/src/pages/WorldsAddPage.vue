<script setup>
import { ref } from 'vue';
import ky from 'ky';
import router from "@/router.js";

const name = ref('');
const description = ref('');
const visualStyle = ref('');
const tags = ref('');
const coverImageFile = ref(null);

const handleFileChange = (e) => {
  coverImageFile.value = e.target.files[0];
};

const handleSubmit = async () => {
  const formData = new FormData();
  formData.append('name', name.value);
  formData.append('description', description.value);
  formData.append('visual_style', visualStyle.value);
  formData.append('tags', tags.value);
  if (coverImageFile.value) formData.append('cover_image_path', coverImageFile.value);

  try {
    const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
    await ky.post(`${apiBaseUrl}/worlds_add`, {
      body: formData,
    }).json();
    await router.push('/');
  } catch (err) {
    console.error('Error:', err);
  }
};
</script>

<template>
  <div class="p-6 bg-gray-100 rounded-xl shadow-md">
    <h2 class="text-xl font-bold mb-4">Добавить мир</h2>

    <form @submit.prevent="handleSubmit">
      <div class="mb-3">
        <input type="text" v-model="name" placeholder="Имя мира" class="p-2 w-full border border-gray-300 rounded-md"
               required/>
      </div>
      <div class="mb-3">
        <textarea v-model="description" placeholder="Описание мира" class="p-2 w-full border border-gray-300 rounded-md"
                  rows="3" required></textarea>
      </div>
      <div class="mb-3">
        <input type="text" v-model="visualStyle" placeholder="Визуальный стиль"
               class="p-2 w-full border border-gray-300 rounded-md" required/>
      </div>
      <div class="mb-3">
        <input type="text" v-model="tags" placeholder="Теги (через запятую)"
               class="p-2 w-full border border-gray-300 rounded-md" required/>
      </div>
      <div class="mb-4">
        <input type="file" @change="handleFileChange" class="p-2"/>
      </div>

      <div class="flex justify-between">
        <router-link to="/" class="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600">Отмена</router-link>
        <button @click="handleSubmit" type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">Добавить</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
</style>
