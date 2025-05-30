import { createRouter, createWebHistory } from 'vue-router';

import WorldsPage from '@/pages/WorldsPage.vue';
import WorldsAddPage from '@/pages/WorldsAddPage.vue';
import WorldPage from '@/pages/WorldPage.vue';
import LocationPage from '@/pages/LocationPage.vue';
import TestPage from '@/pages/TestPage.vue';
import OrganizationPage from "@/pages/OrganizationPage.vue";
import CharacterPage from "@/pages/CharacterPage.vue";
import LocationsAddPage from "@/pages/LocationsAddPage.vue";
import OrganisationsAddPage from "@/pages/OrganisationsAddPage.vue";
import CharactersAddPage from "@/pages/CharactersAddPage.vue";
import ItemsAddPage from "@/pages/ItemsAddPage.vue";
import ItemPage from "@/pages/ItemPage.vue";
import LocationsEditPage from "@/pages/LocationsEditPage.vue";
import OrganisationsEditPage from "@/pages/OrganisationsEditPage.vue";
import EntitiesPage from "@/pages/EntitiesPage.vue";
import AbilitiesAddPage from "@/pages/AbilitiesAddPage.vue";
import AbilityPage from "@/pages/AbilityPage.vue";
import CharactersEditPage from "@/pages/CharactersEditPage.vue";

const entities = ['locations', 'organizations', 'characters', 'items', 'abilities'];
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
    path: '/:worldId/add/organizations',
    name: 'organizations-add',
    component: OrganisationsAddPage,
  },
  {
    path: '/:worldId/organizations/:organizationId/edit',
    name: 'organizations-edit',
    component: OrganisationsEditPage,
  },
  {
    path: '/:worldId/characters/:id',
    name: 'character',
    component: CharacterPage,
  },
  {
    path: '/:worldId/characters/:id/edit',
    name: 'characters-edit',
    component: CharactersEditPage,
  },
  {
    path: '/:worldId/abilities/:id',
    name: 'ability',
    component: AbilityPage,
  },
  {
    path: '/:worldId/add/characters',
    name: 'characters-add',
    component: CharactersAddPage,
  },
  {
    path: '/:worldId/add/abilities',
    name: 'abilities-add',
    component: AbilitiesAddPage,
  },
  {
    path: '/:worldId/items/:itemId',
    name: 'item',
    component: ItemPage,
  },
  {
    path: '/:worldId/add/items',
    name: 'items-add',
    component: ItemsAddPage,
  },
  {
    path: '/:worldId/locations/:locationId',
    name: 'location',
    component: LocationPage,
  },
  {
    path: '/:worldId/add/locations',
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
