<template>
    <v-app>
    <v-app-bar
      color="primary"
      density="compact"
      collapse :elevation="2"
    >
      <template v-slot:prepend>
        <v-app-bar-nav-icon @click="navChange"></v-app-bar-nav-icon>
      </template>
      <v-app-bar-title>IOT-WEB</v-app-bar-title>
        <v-btn icon @click="logOut">
              <v-tooltip
              activator="parent"
              location="end"
              >Log out</v-tooltip>
              <v-icon>mdi-logout</v-icon>
          </v-btn>
    </v-app-bar>
        <v-navigation-drawer
        v-model="drawer"
        floating
        temporary
        rounded
        >
          <v-list-item
            prepend-icon="mdi-account"
            :title="username"
          ></v-list-item>
  
          <v-divider></v-divider>
  
          <v-list density="compact" nav>
            <v-list-item prepend-icon="mdi-home" href="/user/statistics" title="统计"></v-list-item>
            <v-list-item prepend-icon="mdi-home" href="/user/device" title="设备列表"></v-list-item>
            <v-list-item prepend-icon="mdi-home" href="/user/message" title="设备消息"></v-list-item>
            <v-list-item prepend-icon="mdi-home" href="/user/info" title="用户信息"></v-list-item>
          </v-list>
        </v-navigation-drawer>
    <v-main>
    <router-view></router-view>
    </v-main>
  </v-app>
  </template>
  
  <script>
  export default {
    data () {
      return {
        drawer: false,
        username: this.$store.state.user.name
      }
    },
    methods: {
      goTo (name) {
        this.$router.push({
          name: name
        })
      },
      logOut () {
        this.$store.commit('logout')
      },
      navChange () {
        this.drawer = !this.drawer
        this.username = this.$store.state.user.name
      }
    }
  }
  </script>
  