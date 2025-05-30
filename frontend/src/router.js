import { createRouter, createWebHistory } from 'vue-router';

import WorldsPage from '@/pages/WorldsPage.vue';
import WorldsAddPage from '@/pages/WorldsAddPage.vue';
import WorldPage from '@/pages/WorldPage.vue';
import LocationPage from '@/pages/LocationPage.vue';
import TestPage from '@/pages/TestPage.vue';
import OrganizationPage from "@/pages/OrganizationPage.vue";
import CharacterPage from "@/pages/CharacterPage.vue";
import ItemsPage from "@/pages/ItemsPage.vue";
import LocationsAddPage from "@/pages/LocationsAddPage.vue";
import OrganisationsAddPage from "@/pages/OrganisationsAddPage.vue";
import CharactersAddPage from "@/pages/CharactersAddPage.vue";
import ItemsAddPage from "@/pages/ItemsAddPage.vue";
import ItemPage from "@/pages/ItemPage.vue";
import LocationsEditPage from "@/pages/LocationsEditPage.vue";
import OrganisationsEditPage from "@/pages/OrganisationsEditPage.vue";
import EntitiesPage from "@/pages/EntitiesPage.vue";

const entities = ['locations', 'organizations', 'characters', 'items'];
const entityRoutes = entities.map(entity => ({
  path: `/:id/${entity}`,
  name: entity,
  component: EntitiesPage,
}));

const routes = [
  ...entityRoutes,
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
    path: '/:worldId/organizations/:organizationId',
    name: 'organization',
    component: OrganizationPage,
  },
  {
    path: '/:worldId/organizations/organizations/add',
    name: 'organizations-add',
    component: OrganisationsAddPage,
  },
  {
    path: '/:worldId/organizations/:organizationId/edit',
    name: 'organizations-edit',
    component: OrganisationsEditPage,
  },
  {
    path: '/:worldId/characters/:characterId',
    name: 'character',
    component: CharacterPage,
  },
  {
    path: '/:worldId/characters/characters/add',
    name: 'characters-add',
    component: CharactersAddPage,
  },
  {
    path: '/:worldId/items/:itemId',
    name: 'item',
    component: ItemPage,
  },
  {
    path: '/:worldId/items/items/add',
    name: 'items-add',
    component: ItemsAddPage,
  },
  {
    path: '/:worldId/locations/:locationId',
    name: 'location',
    component: LocationPage,
  },
  {
    path: '/:worldId/locations/locations/add',
    name: 'locations-add',
    component: LocationsAddPage,
  },
  {
    path: '/:worldId/locations/:locationId/edit',
    name: 'locations-edit',
    component: LocationsEditPage,
  },
  {
    path: '/test',
    name: 'test',
    component: TestPage,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
