<template>
  <div class="teacher-detail border-box">
    <h2>{{ teacher.name }} - {{ teacher.subject }}</h2>
    <p>评分: {{ averageRating.toFixed(1) }}</p>
    <div>
      <h3>评价</h3>
      <ul>
        <li v-for="review in reviews" :key="review.id">{{ review }}</li>
      </ul>
      <textarea v-model="review" placeholder="输入评价"></textarea>
      <br>
      <select v-model="rating">
        <option disabled value="">请选择评分</option>
        <option v-for="n in 5" :key="n" :value="n">{{ n }} 星</option>
      </select>
      <br>
      <button @click="submitReview">提交</button>
      <button @click="$emit('back')">返回</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['teacher'],
  data() {
    return {
      reviews: [],
      review: '',
      rating: ''
    };
  },
  created() {
    this.fetchReviews();
  },
  computed: {
    averageRating() {
      if (this.teacher.ratings.length === 0) return 0;
      const total = this.teacher.ratings.reduce((acc, curr) => acc + curr, 0);
      return total / this.teacher.ratings.length;
    }
  },
  methods: {
    fetchReviews() {
      axios.get(`/api/teachers/${this.teacher.id}/reviews`)
        .then(response => {
          this.reviews = response.data;
        })
        .catch(error => {
          console.error('Error fetching reviews:', error);
        });
    },
    submitReview() {
      if (this.review && this.rating) {
        axios.post(`/api/teachers/${this.teacher.id}/reviews`, {
          review: this.review,
          rating: parseInt(this.rating)
        })
        .then(() => {
          this.teacher.reviews.push(this.review);
          this.teacher.ratings.push(parseInt(this.rating));
          this.reviews.push(this.review);
          this.review = '';
          this.rating = '';
          alert('评价提交成功');
        })
        .catch(error => {
          console.error('Error submitting review:', error);
        });
      } else {
        alert('请填写完整的评价和评分');
      }
    }
  }
};
</script>

<style scoped>
textarea {
  width: 80%;
  height: 100px;
  margin: 10px auto;
  display: block;
  border: 1px solid #e9e9e9;
  border-radius: 5px;
}

select {
  width: 80%;
  padding: 10px;
  margin: 10px auto;
  display: block;
  border: 1px solid #e9e9e9;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  margin: 5px;
  border: 1px solid #007BFF;
  border-radius: 5px;
  background-color: #007BFF;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #0056b3;
}
</style>
