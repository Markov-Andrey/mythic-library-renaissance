import { createRouter, createWebHistory } from 'vue-router';

import WorldsPage from '@/pages/WorldsPage.vue';
import WorldsAddPage from '@/pages/WorldsAddPage.vue';
import WorldPage from '@/pages/WorldPage.vue';
import LocationsPage from '@/pages/LocationsPage.vue';
import TestPage from '@/pages/TestPage.vue';

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
