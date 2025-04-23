<script setup>
import { ref } from 'vue';
import ky from 'ky';

const showModal = ref(false);

// Форма
const name = ref('');
const shortDescription = ref('');
const fullDescription = ref('');
const visualStyle = ref('');
const genre = ref('');
const tags = ref('');
const coverImageFile = ref(null);

const openModal = () => showModal.value = true;
const closeModal = () => showModal.value = false;

const handleFileChange = (e) => {
  coverImageFile.value = e.target.files[0];
};

const handleSubmit = async () => {
  const formData = new FormData();
  formData.append('name', name.value);
  formData.append('short_description', shortDescription.value);
  formData.append('full_description', fullDescription.value);
  formData.append('visual_style', visualStyle.value);
  formData.append('genre', genre.value);
  formData.append('tags', tags.value);
  formData.append('cover_image_path', coverImageFile.value);

  try {
    const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
    await ky.post(`${apiBaseUrl}/worlds_add`, {
      body: formData,
    }).json();
    closeModal();
  } catch (err) {
    console.error('Error:', err);
  }
};
</script>

<template>
  <div class="bg-gray-100 p-6 rounded-xl shadow-md hover:shadow-lg transition-all flex items-center justify-center cursor-pointer hover:brightness-125 group" @click="openModal">
    <div class="rounded-full bg-blue-300 w-20 h-20 flex items-center justify-center group-hover:bg-blue-400 transition-colors">
      <svg class="w-12 h-12 text-white group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 5v14M5 12h14"></path>
      </svg>
    </div>
  </div>

  <div v-if="showModal" @click="closeModal" class="fixed inset-0 flex justify-center items-center z-50 backdrop-blur-sm bg-white/30">
    <div @click.stop class="bg-white p-6 rounded-lg w-1/3 backdrop-blur-lg max-h-[90vh] overflow-y-auto">
      <h2 class="text-xl font-bold mb-4">Добавить мир</h2>

      <div class="mb-3">
        <input type="text" v-model="name" placeholder="Имя мира" class="mt-1 p-2 w-full border border-gray-300 rounded-md" />
      </div>
      <div class="mb-3">
        <input type="text" v-model="shortDescription" placeholder="Краткое описание" class="mt-1 p-2 w-full border border-gray-300 rounded-md" />
      </div>
      <div class="mb-3">
        <textarea v-model="fullDescription" placeholder="Полное описание" class="mt-1 p-2 w-full border border-gray-300 rounded-md" rows="3" />
      </div>
      <div class="mb-3">
        <input type="text" v-model="visualStyle" placeholder="Визуальный стиль" class="mt-1 p-2 w-full border border-gray-300 rounded-md" />
      </div>
      <div class="mb-3">
        <input type="text" v-model="genre" placeholder="Жанр" class="mt-1 p-2 w-full border border-gray-300 rounded-md" />
      </div>
      <div class="mb-3">
        <input type="text" v-model="tags" placeholder="Теги (через запятую)" class="mt-1 p-2 w-full border border-gray-300 rounded-md" />
      </div>
      <div class="mb-4">
        <input type="file" @change="handleFileChange" />
      </div>

      <div class="flex justify-between">
        <button @click="closeModal" class="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600">Отмена</button>
        <button @click="handleSubmit" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">Добавить</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.backdrop-blur-sm {
  backdrop-filter: blur(5px);
}
.backdrop-blur-lg {
  backdrop-filter: blur(10px);
}
</style>
