<template>
  <v-card>
    <v-card-title>
      <v-row class="align-center">
        <!-- 返回按钮的列 -->
        <v-col cols="auto">
          <v-btn icon @click="$emit('back')">
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
        </v-col>
        <!-- 课程名称的列，使用居中对齐 -->
        <v-col class="d-flex justify-center text-center">
          <span class="headline" style="margin-left: -4.0rem;">{{ course.name }}</span>
        </v-col>
      </v-row>
    </v-card-title>
    <v-card-text>
      <!-- 课程信息 -->
      <div style="background: linear-gradient(to left, #cce5ff, #edc3c7); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */; padding: 10px;">
        <v-subheader style="font-size: 20px; font-weight: bold;">【基本信息】</v-subheader>
        <p>课程代码: {{ course.code }}</p>
        <p>学分: {{ course.credits }}</p>
        <p>所属学院: {{ course.department }}</p>
        <p v-if="averageRating !== undefined">平均评分: {{ averageRating.toFixed(1) }} / 5.0</p>
        <p v-else>评分: 暂无</p>
      </div>
      <br>
      <v-divider></v-divider>

      <br>

      <!-- 新增展示所有评论的部分 -->
      <v-subheader style="font-weight: bold;font-size: 20px;">【所有评论】</v-subheader>
      <v-list dense style="background: linear-gradient(to right, #E9E4F0, #D3CCE3); ">
        <v-list-item v-for="(review, index) in course.reviews" :key="index">
          <v-list-item-content>
            <v-list-item-title>{{ '匿名评论 ' + (index + 1) }}</v-list-item-title>
            <v-list-item><strong>{{ review[1] }}</strong></v-list-item>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <br>
      <v-divider></v-divider>
      <br>

        <div style="background: linear-gradient(to right, #cce5ff, #edc3c7);">

      <br>

      <v-subheader style="font-weight: bold;font-size: 20px;">【评论AI总结】</v-subheader>
      <br>
      <!-- AI评论总结按钮 -->
      <v-btn @click="fetchCourseReviewSummary">点击查看最新总结</v-btn>
      <!-- AI评论总结文本显示区域 -->
      <v-textarea
        v-model="reviewSummary"
        label="AI评论总结"
        rows="5"
        auto-grow
      ></v-textarea>
      <v-divider></v-divider>
      <br>
     </div >
     <div style="font-weight: bold;font-size: 20px;">
      <v-subheader style="font-weight: bold;font-size: 20px;">【添加评论】</v-subheader>
      <v-text-field v-model="newComment" label="输入评价" outlined></v-text-field>
      <v-rating v-model="newRating" max="5" half-increments></v-rating>
      <v-btn color="primary" @click="submitReview">提交</v-btn>
    </div>
    </v-card-text>
  </v-card>
</template>

<script>
import { getapi, postapi } from "../utils/http.js";

export default {
  name: 'CourseDetail',
  props: {
    course: Object
  },
  data() {
    return {
      newComment: '',
      newRating: 0 ,
      reviewSummary: '' // 用于存储和显示评论总结
    };
  },
  methods: {
    fetchCourseReviewSummary() {
      // 暂时替代

      postapi('/api/user/get_summary', {course_name: this.course.id})
      .then(response => {
        // console.log(response)
        this.reviewSummary = response.data.summary;
      })
      .catch(error => {
        this.reviewSummary = 'Backend error.';

      // console.log('error');
      });

      // this.reviewSummary = 'THIS IS THE SUMMARY OF THE REVIEWS TO THIS COURSE.';

      // 从后端API请求数据(暂时不可用)
      // fetch('http://localhost:5000/api/course/' + this.course.id + '/reviews')
      //   .then(response => response.json())
      //   .then(data => {
      //     this.reviewSummary = data.summary;
      //   });

      // return this.reviewSummary;
        //call openai api to analyse the reviews in this.course.reviews
        //return the summary of the reviews
    },

    submitReview() {
      if (this.newComment && this.newRating) {
        // this.$emit('add-review', this.course.id, {
        //   rating: this.newRating,
        //   comment: this.newComment
        // });

        postapi('/api/user/add_course_comment', 
        {
          course: this.course.id,
          review: this.newComment,
          rating: this.newRating
        })
        .then( (response) => {
            this.newComment = '';
            this.newRating = 0;
            if (response.data.status == 0) {
              alert('评论提交成功！');
            } else {
              alert('评论提交失败，请用好听点的口吻！');
            }
        })
        .catch(error => {
            // this.result = '';
        // console.log('error');
        });
      } else {
        alert("请填写完整的评论和评分！");
      }
      // initialize();
    }
  },
  computed: {
    averageRating() {
      if (!this.course.reviews || this.course.reviews.length === 0) {
        return undefined;
      }
      const totalRating = this.course.reviews.reduce((sum, review) => sum + review[0], 0);
      return totalRating / this.course.reviews.length;
    }
  }
};
</script>
