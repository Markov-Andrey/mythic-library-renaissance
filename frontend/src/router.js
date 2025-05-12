import { createRouter, createWebHistory } from 'vue-router';

import WorldsPage from '@/pages/WorldsPage.vue';
import WorldsAddPage from '@/pages/WorldsAddPage.vue';
import WorldPage from '@/pages/WorldPage.vue';
import LocationsPage from '@/pages/LocationsPage.vue';
import LocationPage from '@/pages/LocationPage.vue';
import OrganizationsPage from '@/pages/OrganizationsPage.vue';
import CharactersPage from '@/pages/CharactersPage.vue';
import TestPage from '@/pages/TestPage.vue';
import OrganizationPage from "@/pages/OrganizationPage.vue";
import CharacterPage from "@/pages/CharacterPage.vue";
import ItemsPage from "@/pages/ItemsPage.vue";
import WorldTestPage from "@/pages/WorldTestPage.vue";
import MapTestPage from "@/pages/MapTestPage.vue";

const routes = [
  {
    path: '/',
    name: 'worlds',
    component: WorldsPage,
  },
  {
    path: '/worlds-add',
    name: 'worlds-add',
    component: WorldsAddPage,
  },
  {
    path: '/:id',
    name: 'world',
    component: WorldPage,
  },
  {
    path: '/:id/locations',
    name: 'locations',
    component: LocationsPage,
  },
  {
    path: '/:id/organizations',
    name: 'organizations',
    component: OrganizationsPage,
  },
  {
    path: '/:worldId/organizations/:organizationId',
    name: 'organization',
    component: OrganizationPage,
  },
  {
    path: '/:id/characters',
    name: 'characters',
    component: CharactersPage,
  },
  {
    path: '/:worldId/characters/:characterId',
    name: 'character',
    component: CharacterPage,
  },
  {
    path: '/:id/items',
    name: 'items',
    component: ItemsPage,
  },
  {
    path: '/:worldId/locations/:locationId',
    name: 'location',
    component: LocationPage,
  },
  {
    path: '/test',
    name: 'test',
    component: TestPage,
  },
  {
    path: '/w-test',
    name: 'w-test',
    component: WorldTestPage,
  },
  {
    path: '/m-test',
    name: 'm-test',
    component: MapTestPage,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
