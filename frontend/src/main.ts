import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";
import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "../src/home/HomePage.vue";
import SettingsPage from "../src/settings/SettingsPage.vue";

import Button from "primevue/button";

import "primevue/resources/themes/saga-purple/theme.css"; //theme
import "primevue/resources/primevue.min.css"; //core css
import "primeicons/primeicons.css"; //icons
import "primeflex/primeflex.css";

const routes = [
  { path: "/home", component: HomePage },
  {
    path: "/settings",
    component: SettingsPage,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

const app = createApp(App);
app.use(router);
app.use(PrimeVue);
app.component("Button", Button);

app.mount("#app");
