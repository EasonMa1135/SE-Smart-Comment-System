/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App
 */

// Vue 和 Vuetify 的引入
import { createApp } from 'vue';
import App from './App.vue';

// 引入 Vuetify
import { createVuetify } from 'vuetify';
import 'vuetify/styles'; // 引入 Vuetify 的基本样式
import '@mdi/font/css/materialdesignicons.css'; // 如果使用 Material Design Icons

// 引入 Vuetify 插件
import { registerPlugins } from '@/plugins';

// 引入路由和状态管理
import router from './router';
import store from './store';

// 创建 Vuetify 实例
const vuetify = createVuetify({
  // 你可以在这里配置 Vuetify
  // 例如：theme, components, directives 等
});

// 创建 Vue 应用实例
const app = createApp(App);

// 注册 Vuetify 和其他插件
app.use(vuetify);
registerPlugins(app);

// 添加路由和状态管理
app.use(router);
app.use(store);

// 挂载应用到 DOM
app.mount('#app');
