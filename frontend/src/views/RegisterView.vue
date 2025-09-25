<template>
    <div>
      <v-form ref="form">
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
          <v-card-title class="text-h6 font-weight-regular"> Sign up </v-card-title>
          </v-toolbar>

          <div class="text-subtitle-1 text-medium-emphasis">Name</div>
    
          <v-text-field
            density="compact"
            placeholder="User name"
            prepend-inner-icon="mdi-account"
            variant="filled"
            v-model="name"
            :rules="[rules.required, rules.length(6)]"
            counter="6"
          ></v-text-field>
    
          <div class="text-subtitle-1 text-medium-emphasis">Email</div>
    
          <v-text-field
            density="compact"
            placeholder="Email address"
            prepend-inner-icon="mdi-email-outline"
            variant="filled"
            v-model="email"
            :rules="[rules.email]"
            type="email"
          ></v-text-field>

          <div
            class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
          >
            Password
          </div>
    
          <v-text-field
            v-model="pswd"
            type='password'
            density="compact"
            placeholder="Enter your password"
            prepend-inner-icon="mdi-lock-outline"
            @click:append-inner="visible = !visible"
            :rules="[rules.password, rules.length(6)]"
            variant="filled"
            counter="6"
          ></v-text-field>

          <div
            class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
          >
            Confirm Password
          </div>
    
          <v-text-field
            type='password'
            density="compact"
            placeholder="Confirm above password"
            prepend-inner-icon="mdi-lock-outline"
            @click:append-inner="visible = !visible"
            :rules="[rules.confirm, rules.length(6)]"
            variant="filled"
            counter="6"
          ></v-text-field>
    
          <v-btn block class="mb-8" color="blue" size="large" variant="tonal" @click="validate">
            Sign Up
          </v-btn>

        </v-card>
      </v-form>
    </div>
  </template>


<script>
  import { postapi } from "../utils/http.js";
  export default {
    data () {
    return {
      name: null,
      email: null,
      pswd: null,

      rules: { // 匹配规则，需满足才能提交
        email: v => !!(v || '').match(/@/) || 'Please enter a valid email',
        length: len => v =>
          (v || '').length >= len ||
          `Invalid character length, required ${len}`,
        password: v =>
          !!(v || '').match(
            /^(?=.*[a-zA-Z])(?=.*\d).+$/
          ) ||
          'Letter and numeric character must be contained',
        required: v => !!v || 'This field is required',
        confirm: v => (v === this.pswd) || 'This field should match the password'
      },
    }
    },
    methods: {
        backHistory () {
            this.$router.go(-1); // 返回路由的上一层
        },
        async validate() {
          // 验证表单
          const { valid } = await this.$refs.form.validate()
          if (valid) {
            postapi('/api/user/register', {
              email: this.email,
              password: this.pswd,
              username: this.name,
            })
            .then((response)=> {
              alert(response.data.resp)
              if(response.data.status == 0){
                  location.reload()
              }
            })
            .catch(function (error) {
              console.log(error);
            });
          }
        },
    }
  }
</script>