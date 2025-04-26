import { createRouter, createWebHistory } from 'vue-router';

import WorldsPage from '@/pages/WorldsPage.vue';
import TestPage from '@/pages/TestPage.vue';

const routes = [
  {
    path: '/',
    name: 'worlds',
    component: WorldsPage,
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
