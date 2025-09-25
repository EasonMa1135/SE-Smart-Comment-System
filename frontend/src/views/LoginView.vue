<template>
    <div>
      <v-img
        class="mx-auto my-6"
        max-width="228"
        src="../assets/logo.png"
      ></v-img>
  
      <v-card
        class="mx-auto pa-12 pb-8"
        elevation="8"
        max-width="448"
        rounded="lg"
      >

        <v-toolbar color="blue" cards dark flat>
        <v-btn icon @click="backHistory">
            <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <v-card-title class="text-h6 font-weight-regular" > Login </v-card-title>
        </v-toolbar>

        <div class="text-subtitle-1 text-medium-emphasis">Name</div>
  
        <v-text-field
          density="compact"
          placeholder="User name"
          prepend-inner-icon="mdi-account"
          variant="outlined"
          v-model="name"
        ></v-text-field>

        <div
          class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
        >
          Password
        </div>
  
        <v-text-field
          :append-inner-icon="visible ? 'mdi-eye' : 'mdi-eye-off'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="Enter your password"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          v-model="pswd"
          @click:append-inner="visible = !visible"
        ></v-text-field>
  
        <v-btn block class="mb-8" color="blue" size="large" variant="tonal" @click="logIn">
          Log In
        </v-btn>
  
        <v-card-text class="text-right">
          <a
            class="text-blue text-decoration-none"
            href="/register"
            rel="noopener noreferrer"
            target="_self"
          >
            No account? Sign up now! <v-icon icon="mdi-chevron-right"></v-icon>
          </a>
        </v-card-text>
      </v-card>
    </div>
  </template>
  
  <script>
    import { postapi } from "../utils/http.js";
    export default {
      data: () => ({
        visible: false,
        name: null,
        pswd: null,
      }),
      methods: {
        backHistory () {
            this.$router.go(-1); // 返回路由的上一层
        },
        logIn () {
          postapi('/api/user/login', {
            username: this.name,
            password: this.pswd,
          })
          .then( (response)=> {
            alert(response.data.resp)
            if(response.data.status == 0) {
              // 保存登录信息
              this.$store.commit('setUser',this.name)
              this.$store.commit('setToken',response.data.token)
              this.$router.push({
                name: "Userhome"
              })
            }
          })
          .catch(function (error) {
            console.log(error)
          });
        }
      }
    }
  </script>
  