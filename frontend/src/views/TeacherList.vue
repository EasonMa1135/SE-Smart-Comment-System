<template>
  <div class="teacher-list">
    <ul>
      <li v-for="teacher in teachers" :key="teacher.id" @click="selectTeacher(teacher)">
        {{ teacher.name }} - {{ teacher.subject }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['teachers'],
  methods: {
    selectTeacher(teacher) {
      this.$emit('select', teacher);
    }
  }
};
</script>

<style scoped>
.teacher-list {
  display: inline-block;
  width: 100%;
  max-width: 1200px;
  min-width: 1200px;
  margin: 0 auto;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  border: 1px solid #f9f9f9;
  margin: 10px 0; /* Added spacing between list items */
  cursor: pointer;
  background-color: #f9f9f9;
  transition: background-color 0.3s;
}

li:hover {
  background-color: #e9e9e9;
}
</style>

  
  
  