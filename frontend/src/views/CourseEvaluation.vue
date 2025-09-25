<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <!-- 搜索课程和选项卡部分 -->
        <v-text-field v-model="searchTerm" label="搜索课程" single-line hide-details @input="searchCourses"></v-text-field> 
        
        <!-- 只有在没有选择特定课程时，才显示选项卡和课程列表 -->
        <template v-if="!selectedCourse">
          <v-tabs v-model="activeTab" background-color="blue-grey lighten-5" fixed-tabs @change="searchCourses">
            <v-tab v-for="(category, index) in categories" :key="index" :class="{ 'active-tab': activeTab === index }"
              @click="activeTab = index">
              {{ category }}
            </v-tab>
          </v-tabs>

          <v-tabs-items v-model="activeTab">
            <v-card flat>
              <v-card-text>
                <v-list>
                  <v-list-item-group>
                    <v-list-item v-for="course in filteredCourses" :key="course.id"
                      :class="{ 'selected-item': selectedCourse && selectedCourse.id === course.id }" outlined
                      @click="selectCourse(course)">
                      <v-list-item-content>
                        <v-list-item-title>{{ course.name }}</v-list-item-title>
                        <v-list-item-subtitle>{{ course.department }} - {{ course.credits }} 学分</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-card-text>
            </v-card>
          </v-tabs-items>
        </template>
      
        <!-- 选择了课程后，显示课程详情 -->
        <v-row v-if="selectedCourse">
          <v-col>
            <CourseDetail :course="selectedCourse" @add-review="addReview" @back="clearSelection" />
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import CourseDetail from './CourseDetail.vue';
import { getapi, postapi } from "../utils/http.js";

export default {
  name: 'CourseEvaluation',
  components: {
    CourseDetail
  },
  data() {
    return {
      activeTab: 0,
      searchTerm: '',
      categories: ['专业课', '通识必修课程', '体育课程', '跨类(专业)', '专业基础课程', '认定型课程', '国际化课程', '实验课程', '荣誉课程'],
      courses: [],
      filteredCourses: [],
      selectedCourse: null
    };
  },
  methods: {
    startFetchCommentsInterval() {
      this.initialize()
      this.intervalId = setInterval(this.initialize(), 5000)
    },
    stopFetchCommentsInterval() {
      clearInterval(this.intervalId)
    },
    initialize () {
      console.log('hikasjhdfkjn');
      // this.courses = [
      //   {
      //     id: 1,
      //     code: '2110721',
      //     name: '工程实践',
      //     credits: '3.0',
      //     category: '专业课',
      //     department: '计算机科学与技术学院',
      //     reviews: [
      //       [5, "Engaging discussions on the intricacies of human behavior enhance understanding."],
      //       [3, "Overlapping content in lectures and readings can lead to redundancy."],
      //       [4, "Practical applications of psychological theories enrich the learning experience."]
      //     ]
      //   },
      // ]
      postapi('/api/user/get_course', {})
      .then( (response) => {
          this.courses = response.data
      })
      .catch(error => {
          // this.result = '';
      // console.log('error');
      });
    },
    searchCourses() {
      // console.log('hello')
      this.filteredCourses = [];
      if (this.searchTerm) {
        this.filteredCourses = this.courses.filter(course =>
          course.name.toLowerCase().includes(this.searchTerm.toLowerCase()) &&
          course.category === this.categories[this.activeTab]
        );
      } else {
        this.filteredCourses = this.courses.filter(course =>
          course.category === this.categories[this.activeTab]
        );
      }
    },

    selectCourse(course) {
      this.selectedCourse = course;
    },

    clearSelection() {
      this.selectedCourse = null;
    },

    addReview(courseId, review) {
      const course = this.courses.find(c => c.id === courseId);
      if (course) {
        course.reviews.push(review);
        // Update the course rating based on the new review
        course.rating = (course.rating * (course.reviews.length - 1) + review.rating) / course.reviews.length;
      }
    }
  },
  mounted() {
    this.startFetchCommentsInterval();
    this.searchCourses();
  },
  beforeUnmount() {
    this.stopFetchCommentsInterval()
  },

  watch: {
    activeTab() {
      this.searchCourses();
    },
    searchTerm() {
      this.searchCourses();
    }
  },

};
</script>

<style scoped>
.selected-item {
  transition: background-color 0.3s ease;
  /* 添加平滑的过渡效果 */
  background-color: rgb(255, 255, 255);
}
.active-tab {
  background-color: rgb(88, 129, 87) !important; /* 确保此样式优先级更高 */
  color: white; /* 设置文字颜色 */
}
.v-card {

  transition: background-color 0.3s ease;
}
</style>
