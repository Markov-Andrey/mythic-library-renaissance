<script setup>
import { ref, watch, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ky from 'ky'

import MiniCard from '@/components/MiniCard.vue'
import NewCardAdd from '@/components/NewCardAdd.vue'
import SelectElement from '@/components/SelectElement.vue'
import SearchElement from '@/components/SearchElement.vue'

const route = useRoute()
const router = useRouter()

const api = import.meta.env.VITE_API_BASE_URL
const entities = ref([])
const entityTypes = ref([])
const entityTags = ref([])

const selectedType = ref('')
const selectedTags = ref('')
const searchQuery = ref('')

const syncFilters = () => {
  selectedType.value = route.query.type || ''
  selectedTags.value = route.query.tags || ''
  searchQuery.value = route.query.search || ''
}

const fetchAll = async () => {
  const { id } = route.params
  const name = route.name
  const q = new URLSearchParams(route.query).toString()
  const base = `${api}/api/worlds/${id}/${name}`

  const [types, tags, data] = await Promise.all([
    ky.get(`${base}/types`).json(),
    ky.get(`${base}/tags`).json(),
    ky.get(`${base}${q ? '?' + q : ''}`).json()
  ])

  entityTypes.value = types
  entityTags.value = tags
  entities.value = data
}

watch(
  [() => route.name, () => route.params.id],
  async () => {
    syncFilters()
    await fetchAll()
  },
  { immediate: true }
)

watch(() => route.query, () => {
  syncFilters()
  fetchAll()
})

watch([selectedType, selectedTags, searchQuery], () => {
  router.push({
    path: route.path,
    query: {
      ...(selectedType.value && { type: selectedType.value }),
      ...(selectedTags.value && { tags: selectedTags.value }),
      ...(searchQuery.value && { search: searchQuery.value })
    }
  })
})
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-7xl px-2 py-6 mx-auto">
      <div class="flex gap-2">
        <SelectElement
          id="type-select"
          label="Filter by Type:"
          :options="entityTypes"
          v-model="selectedType"
          placeholder="All types"
          class="w-48"
        />
        <SelectElement
          id="tags-select"
          label="Filter by Tag:"
          :options="entityTags"
          v-model="selectedTags"
          placeholder="All tags"
          class="w-48"
        />
        <SearchElement
          v-model="searchQuery"
          id="search-input"
          label="Search:"
          placeholder="Search entities..."
          class="w-64"
        />
      </div>

      <div class="grid grid-cols-5 gap-3 mt-4">
        <div v-for="obj in entities" :key="obj.id">
          <MiniCard
            :to="`${route.name}/${obj.id}`"
            :cover="obj.cover"
            :name="obj.name"
            :type="obj.type"
            :tags="obj.tags"
          />
        </div>
        <NewCardAdd :to="`/${route.params.id}/${route.name}/${route.name}/add`" />
      </div>
    </div>
  </div>
</template>
