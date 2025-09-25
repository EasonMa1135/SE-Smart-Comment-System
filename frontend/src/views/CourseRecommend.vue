<template>
  <div>
    <div style="display: flex; justify-content: center;">
      <textarea v-model="requirement" rows="3" cols="40" placeholder="输入你的选课请求" style="margin-right: 10px; border-color: #A3B18A; color: #000000;"></textarea>
      <button @click="foo" style="background-color: #A3B18A; color: white; border: none; padding: 10px 20px; border-radius: 5px;">智能推荐</button>
    </div>
    <div style="display: flex; justify-content: center; margin-top: 1rem;">
      <div class="result-card">
        <div class="card-header">
          推荐结果
        </div>
        <div class="card-body">
          <p>{{ result }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getapi, postapi } from "../utils/http.js";
export default {
  name: 'CourseRecommend',
  data() {
    return {
      default_res: '',
      requirement: '',
      result: ''
    }
  },
  methods: {
    foo() {
      this.result = '请稍候';
      const data = {
        req: this.requirement
      };
      // console.log('ho');

      // console.log(data);

      // call backend
      postapi('/api/user/get_recommend', data)
      .then(response => {
        console.log(response)
          this.result = this.default_res + response.data.result;
      })
      .catch(error => {
          this.result = '';
      // console.log('error');
      });
    }
  }
};
</script>

<style scoped>
.result-box {
  margin-top: 1rem;
  padding: 1rem;
  border: 1px solid #ccc;
  background-color: #ffffff;
  font-family: monospace;
  white-space: pre-wrap;
}


.result-card {
  width: 485px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.card-header {
  background-color: #f5f5f5;
  padding: 10px;
  font-weight: bold;
}

.card-body {
  padding: 20px;
}
</style>
