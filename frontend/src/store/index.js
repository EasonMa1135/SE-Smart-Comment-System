import { createStore } from 'vuex'
import user from './user'

export default createStore({
    modules: {
      user:user // 暴露 user.js 提供的接口
    }
})