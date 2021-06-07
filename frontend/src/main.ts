import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";
import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "../src/home/HomePage.vue";
import SettingsPage from "../src/settings/SettingsPage.vue";
import LoginPage from "../src/login/LoginPage.vue";

import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Textarea from "primevue/textarea";
import Password from "primevue/password";

import "primevue/resources/themes/saga-purple/theme.css"; //theme
import "primevue/resources/primevue.min.css"; //core css
import "primeicons/primeicons.css"; //icons
import "primeflex/primeflex.css";
import http from "./utils/http";

const routes = [
  { path: "/home", component: HomePage, name: "home" },
  {
    path: "/settings",
    component: SettingsPage,
    name: "settings",
  },
  {
    path: "/login",
    component: LoginPage,
    name: "login",
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
app.component("InputText", InputText);
app.component("Password", Password);
app.component("TextArea", Textarea);

app.provide("http", http);

app.mount("#app");
