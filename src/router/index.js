import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/home.vue';
import AboutView from '../views/about.vue';
import CatalogView from '../views/catalogue.vue';
import ContactView from '../views/contacts.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/about', name: 'About', component: AboutView },
  { path: '/catalog', name: 'Catalog', component: CatalogView },
  { path: '/contacts', name: 'Contact', component: ContactView },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
