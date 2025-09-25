<template>
    <div class="border-box">
      <h3>{{ course.name }}</h3>
      <p>{{ course.subject }}</p>
      <p>评分: {{ course.rating }}</p>
      <div v-if="course.reviews.length > 0">
        <h4>评论:</h4>
        <ul>
          <li v-for="review in course.reviews" :key="review.id">{{ review.text }}</li>
        </ul>
      </div>
      <div v-else>
        <p>暂无评论</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      course: {
        type: Object,
        required: true
      }
    }
  }
  </script>