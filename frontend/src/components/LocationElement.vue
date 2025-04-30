<script setup>
defineProps({
  location: Object,
  worldId: [String, Number],
});
</script>

<template>
  <div class="pl-4 mt-2">
    <router-link
      :to="`/${worldId}/locations/${location.id}`"
      class="block w-full bg-white text-left text-sm font-semibold hover:bg-blue-50 px-3 py-2 rounded shadow-sm transition"
    >
      {{ location.name }}
    </router-link>

    <div v-if="location.children && location.children.length" class="mt-1">
      <LocationElement
        v-for="child in location.children"
        :key="child.id"
        :location="child"
        :worldId="worldId"
      />
    </div>
  </div>
</template>
