<template>
  <div class="search-bar">
    <v-col cols="12">
      <v-text-field v-model="searchTerm" label="搜索教师名字" single-line hide-details @input="onInput"></v-text-field> 
      <!-- 搜索框键入时，备选选项卡组件；当searchCourses方法被触发时，选项卡组件会被重新渲染 -->
      <v-tabs v-model="activeTab" background-color="blue-grey lighten-5" fixed-tabs @change="searchCourses">
        <!-- 使用v-for指令遍历categories数组，为每个选项卡绑定点击事件；当用户点击一个标签时，它会更新 activeTab 的值为被点击的标签的索引 -->
        <v-tab v-for="(category, index) in categories" :key="index" :class="{ 'active-tab': activeTab === index }"
          @click="activeTab = index">
          {{ category }}
        </v-tab>
      </v-tabs>
    </v-col>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: ''
    };
  },
  methods: {
    onInput() {
      this.$emit('search', this.query);
    }
  }
};
</script>

<style scoped>
.search-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 1200px;
  max-width: 1200px;
  margin: 0 auto;
}

input {
  padding: 10px;
  min-width: 800px;
  width: 100%;
  font-size: 16px;
  border: 1px solid #007BFF;
  border-radius: 10px;
}
</style>
  
