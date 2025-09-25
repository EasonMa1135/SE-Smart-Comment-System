<template>
    <v-card class="mx-auto" max-width="800">
      <v-card-item class="bg-blue">
        <v-card-title>
          <span class="text-h5">用户信息</span>
        </v-card-title>
      </v-card-item>
  
      <v-list>
        <v-list-item
        prepend-icon="mdi-account"
        title="用户名"
        v-model="username"
        >
        {{ username }}

        <template v-slot:append>
          <v-dialog v-model="dialogName" max-width="500px">
            <template v-slot:activator="{ props }">
              <v-btn
              icon="mdi-pencil"
              variant="text"
              density="comfortable"
              color="primary" dark class="mb-2" v-bind="props"
              ></v-btn>
            </template>
            <v-form ref="form_name">
              <v-card>
                <v-card-title>
                  <span class="text-h5">修改用户名</span>
                </v-card-title>
    
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="6" md="12">
                        <v-text-field
                          v-model="editedName"
                          label="新用户名"
                          :rules="[rules.required, rules.length(6)]"
                          counter="6"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
    
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue-darken-1" variant="text" @click="closeName">
                    取消
                  </v-btn>
                  <v-btn color="blue-darken-1" variant="text" @click="saveName">
                    保存
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-form>
          </v-dialog>
        </template>

        </v-list-item>
        <v-divider inset></v-divider>

        <v-list-item
        prepend-icon="mdi-email"
        title="电子邮箱"
        v-model="email"
        >
        {{ email }}

        <template v-slot:append>
          <v-dialog v-model="dialogEmail" max-width="500px">
            <template v-slot:activator="{ props }">
              <v-btn
              icon="mdi-pencil"
              variant="text"
              density="comfortable"
              color="primary" dark class="mb-2" v-bind="props"
              ></v-btn>
            </template>
            <v-form ref="form_email">
              <v-card>
                <v-card-title>
                  <span class="text-h5">修改电子邮箱</span>
                </v-card-title>
    
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="6" md="12">
                        <v-text-field
                          v-model="editedEmail"
                          label="新电子邮箱"
                          :rules="[rules.email]"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
    
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue-darken-1" variant="text" @click="closeEmail">
                    取消
                  </v-btn>
                  <v-btn color="blue-darken-1" variant="text" @click="saveEmail">
                    保存
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-form>
          </v-dialog>
        </template>

        </v-list-item>
        <v-divider inset></v-divider>

        <v-list-item
        prepend-icon="mdi-lock"
        title="密码"
        type="password"
        >

        <template v-slot:append>
          <v-dialog v-model="dialogPswd" max-width="500px">
            <template v-slot:activator="{ props }">
              <v-btn
              icon="mdi-pencil"
              variant="text"
              density="comfortable"
              color="primary" dark class="mb-2" v-bind="props"
              ></v-btn>
            </template>
            <v-form ref="form_pswd">
              <v-card>
                <v-card-title>
                  <span class="text-h5">修改密码</span>
                </v-card-title>
    
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="6" md="6">
                        <v-text-field
                          :append-inner-icon="visible1 ? 'mdi-eye' : 'mdi-eye-off'"
                          :type="visible1 ? 'text' : 'password'"
                          v-model="oldPswd"
                          label="原密码"
                          :rules="[rules.required, rules.length(6)]"
                          counter="6"
                          @click:append-inner="visible1 = !visible1"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="6">
                        <v-text-field
                          :append-inner-icon="visible2 ? 'mdi-eye' : 'mdi-eye-off'"
                          :type="visible2 ? 'text' : 'password'"
                          v-model="editedPswd"
                          label="新密码"
                          :rules="[rules.password, rules.length(6)]"
                          counter="6"
                          @click:append-inner="visible2 = !visible2"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
    
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue-darken-1" variant="text" @click="closePswd">
                    取消
                  </v-btn>
                  <v-btn color="blue-darken-1" variant="text" @click="savePswd">
                    保存
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-form>
          </v-dialog>
        </template>

        </v-list-item>

      </v-list>
    </v-card>
  </template>
  
  <script>
    import { getapi, postapi } from "../utils/http.js";
    export default {
      data: () => ({
        visible1: false,
        visible2: false,
        username: '',
        email: '',
        dialogName: false,
        dialogEmail: false,
        dialogPswd: false,
        editedName: '',
        editedEmail: '',
        oldPswd: '',
        editedPswd: '',
        rules: {
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
        },
      }),

      watch: {
        dialogName(val) {
          val || this.closeName()
        },
        dialogEmail(val) {
          val || this.closeEmail()
        },
        dialogPswd(val) {
          val || this.closePswd()
        },
      },

      methods: {
        initialize () {
          getapi('/api/user/getUserInfo')
          .then( (response) => {
            if (response.data.status == 0) {
              this.$store.commit('setUser',response.data.username)
              this.$store.commit('setEmail',response.data.email)
              this.username = this.$store.state.user.name
              this.email = this.$store.state.user.email
            }
            else {
              alert('获取用户信息失败')
            }
          })
          .catch( (error) => {
            console.log(error)
            alert('获取用户信息失败')
          });
        },

        closeName () {
          this.dialogName = false
          this.$nextTick(() => {
            this.editedName = ''
          })
        },

        async saveName () {
          const { valid } = await this.$refs.form_name.validate()
          if (valid) {
            var sName = this.editedName
            postapi('/api/user/modifyName', {
              newname: this.editedName,
            })
            .then( (response)=> {
              if(response.data.status == 0) {
                // 保存更改信息
                this.$store.commit('setUser', sName)
                this.username = sName
              }
              alert(response.data.resp)
            })
            .catch( (error) => {
              console.log(error)
            });

            this.closeName()
          }
        },

        closeEmail () {
          this.dialogEmail = false
          this.$nextTick(() => {
            this.editedEmail = ''
          })
        },

        async saveEmail () {
          const { valid } = await this.$refs.form_email.validate()
          if (valid) {
            var sEmail = this.editedEmail
            postapi('/api/user/modifyEmail', {
              newemail: this.editedEmail,
            })
            .then( (response)=> {
              if(response.data.status == 0) {
                // 保存更改信息
                this.$store.commit('setEmail', sEmail)
                this.email = sEmail
              }
              alert(response.data.resp)
            })
            .catch( (error) => {
              console.log(error)
            });

            this.closeEmail()
          }
        },

        closePswd () {
          this.dialogPswd = false
          this.$nextTick(() => {
            this.oldPswd = ''
            this.editedPswd = ''
          })
        },

        async savePswd () {
          const { valid } = await this.$refs.form_pswd.validate()
          if (valid) {
            postapi('/api/user/modifyPassword', {
              oldpassword: this.oldPswd,
              newpassword: this.editedPswd,
            })
            .then( (response)=> {
              alert(response.data.resp)
            })
            .catch( (error) => {
              console.log(error)
            });

            this.closePswd()
          }
        },
      },

      mounted () {
        this.initialize()
      },
    }
  </script>
  