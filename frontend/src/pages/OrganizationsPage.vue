<script setup>
import {onMounted, ref, watch} from 'vue';
import {useRoute, useRouter} from 'vue-router';
import ky from 'ky';
import NewCardAdd from "@/components/NewCardAdd.vue";
import MiniCard from "@/components/MiniCard.vue";

const organizations = ref([]);
const route = useRoute();
const router = useRouter();
const worldId = route.params.id;
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const fetchOrganizations = async () => {
  try {
    const params = new URLSearchParams(route.query).toString();
    const url = `${apiBaseUrl}/api/worlds/${worldId}/organizations${params ? '?' + params : ''}`;
    organizations.value = await ky.get(url).json();
  } catch (err) {
    console.error('Error fetching locations:', err);
  }
};

const selectedType = ref(route.query.type || '');
const selectedTags = ref(route.query.tags || '');

watch(() => route.query, () => {
  fetchOrganizations();
  selectedType.value = route.query.type || '';
  selectedTags.value = route.query.tags || '';
}, { deep: true });

watch(selectedType, (newType) => {
  const newQuery = { ...route.query };
  if (newType) {
    newQuery.type = newType;
  } else {
    delete newQuery.type;
  }
  router.push({ path: route.path, query: newQuery });
});

onMounted(() => {
  fetchOrganizations();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">
    <div class="w-full max-w-7xl px-2 py-6 mx-auto">
      <div class="grid grid-cols-5 gap-3">
        <div v-for="organization in organizations">
          <MiniCard
            :to="`organizations/${organization.id}`"
            :cover="organization.cover"
            :name="organization.name"
            :type="organization.type"
          />
        </div>
        <NewCardAdd :to="`/${worldId}/organizations/organizations-add`"/>
      </div>
    </div>
  </div>
</template>
