import { createApp } from "vue";
import PrimeVue from "primevue/config";
import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "../src/pages/HomePage.vue";
import UserQuotePage from "../src/pages/UserQuotePage.vue";
import SettingsPage from "../src/settings/SettingsPage.vue";
import LoginPage from "../src/login/LoginPage.vue";

import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import SelectButton from "primevue/selectbutton";
import InputText from "primevue/inputtext";
import Textarea from "primevue/textarea";
import Password from "primevue/password";
import Card from "primevue/card";
import ToastService from "primevue/toastservice";
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";
import Toast from "primevue/toast";
import AutoComplete from "primevue/autocomplete";
import ProgressSpinner from "primevue/progressspinner";
import ConfirmPopup from "primevue/confirmpopup";
import ConfirmationService from "primevue/confirmationservice";

import App from "./App.vue";

import "primevue/resources/themes/md-light-deeppurple/theme.css"; //theme
import "primevue/resources/primevue.min.css"; //core css
import "primeicons/primeicons.css"; //icons
import "primeflex/primeflex.css";
import http from "./utils/http";

const routes = [
  { path: "/home", component: HomePage, name: "home" },
  { path: "/quotes", component: UserQuotePage, name: "user-quotes" },
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
app.use(ConfirmationService);
app.component("Button", Button);
app.component("InputText", InputText);
app.component("Password", Password);
app.component("TextArea", Textarea);
app.component("Card", Card);
app.component("Toast", Toast);
app.component("AutoComplete", AutoComplete);
app.component("SelectButton", SelectButton);
app.component("ProgressSpinner", ProgressSpinner);
app.component("TabView", TabView);
app.component("TabPanel", TabPanel);
app.component("DataTable", DataTable);
app.component("Column", Column);
app.component("ConfirmPopup", ConfirmPopup);
app.use(ToastService);

app.provide("http", http);

app.mount("#app");
