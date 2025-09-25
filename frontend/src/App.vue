<template>
  <div id="app">
    <nav>
      <div class="card-container">
        <div class="card">
          <router-link to="/abc">
            <div class="card-content">返回</div>
          </router-link>
        </div>

        <div class="card">
          <router-link to="/">
            <div class="card-content">首页</div>
          </router-link>
        </div>

        <div class="card">
          <router-link to="/course-evaluation">
            <div class="card-content">课程评价</div>
          </router-link>
        </div>

        <div class="card">
          <router-link to="/teacher-evaluation">
            <div class="card-content">教师评价</div>
          </router-link>
        </div>

        <div class="card">
          <router-link to="/course-recommend">
            <div class="card-content">选课推荐</div>
          </router-link>
        </div>
      </div>
    </nav>
    <div class="content-area">
      <router-view />
    </div>
  </div>
</template>

<script setup>
  //
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 20px;
}

nav {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 20px;
  height: 50px; /* Adjustthe height as needed */
}

router-link {
  text-decoration: none;
  color: #42b983;
}

router-link-active {
  font-weight: bold;
}

.content-area {
  /* Add any necessary styles for the content area */
}
</style>

<style scoped>
.card-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 20px;
}

.card {
  background-color: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 120px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: background-color 0.2s;
}

.card:hover {
  background-color: #588157;
}

.card a {
  color: #333;
  text-decoration: none;
  font-size: 1.2rem;
}

.card a.router-link-exact-active {
  color: #A3B18A;
  font-weight: bold;
}

.card-content {
  text-align: center;
}
</style>
