<template>
  <div class="background-image">
    <v-layout align-center align-content-center>
      <div class="blank-block"></div>
      <v-container>
        <v-row class="text-center fill-height">
          <v-sheet
            class="d-flex align-center justify-center flex-wrap text-center mx-auto px-4"
            elevation="4"
            height="250"
            rounded
            max-width="800"
            width="100%"
          >
            <div>
              <h2 class="text-h4 font-weight-black" :style="{ color: `rgb(0,0,0)` }">
                智能课程评价系统
              </h2>
              <div class="blank-block-1"></div>
              <div class="text-h5 font-weight-mediums mb-2" :style="{ color: `rgb(163, 177, 138)` }">
                欢迎，何同学
              </div>

              <!-- 
              <v-btn href="/register" variant="text" color="orange">Go to Signup</v-btn>
              <v-btn href="/login" variant="text" color="orange">Go to Login</v-btn>
              -->
            </div>

          </v-sheet>
          <div class="blank-block-2"></div>
        </v-row>
      </v-container>
    </v-layout>
  </div>
</template>

<style scoped>
.background-image {
  background-image: url('../assets/bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.blank-block {
  height: 20px;
}

.blank-block-1 {
  height: 20px;
}

.blank-block-2 {
  height: 500px;
}

</style>