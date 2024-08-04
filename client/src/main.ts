import "./assets/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import vuetify from "./plugins/vuetify";

import App from "./App.vue";
import router from "./router";

const app = createApp(App);

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faAlipay, faWeixin } from '@fortawesome/free-brands-svg-icons';

library.add(faAlipay, faWeixin);

app.use(vuetify);
app.component('font-awesome-icon', FontAwesomeIcon);

app.use(createPinia());
app.use(router);

app.mount("#app");
