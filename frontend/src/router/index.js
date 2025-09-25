// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomeView.vue'), // 主页面为 HomeView 对应 URL 为 /
    redirect: '',
    children: [
      {
        path: '/',
        name: 'Itro',
        component: () => import('../views/IntroView.vue') // 页面 IntroView 对应 URL 为 /
        // 实际上可以认为 IntroView 是主页面， HomeView 作为背景
      },
      {
        path: '/login',
        name: 'Login',
        component: () => import('../views/LoginView.vue') // 页面 LoginView 对应 URL 为 /login
      },
      {
        path: '/register',
        name: 'Register',
        component: () => import('../views/RegisterView.vue')
      },
      {
        path: '/course-evaluation',
        name: 'CourseEvaluation',
        component: () => import('../views/CourseEvaluation.vue') // 新增的课程评价页面
      },
      {
        path: '/teacher-evaluation',
        name: 'TeacherEvaluation',
        component: () => import('../views/TeacherEvaluation.vue') // 新增的教师评价页面
      },
      {
        path: '/course-recommend',
        name: 'CourseRecommend',
        component: () => import('../views/CourseRecommend.vue') // 新增的教师评价页面
      }
    ]
  },
  {
    path: '/user',
    name: 'Userhome',
    component: () => import('@/views/UserView.vue'), // 主页面为 UserView 对应 URL 为 /user
    redirect: '/user/info', // 会重定向至 /user/info ，即进入 /user 后会自动跳转至 /user/info
    children: [
      {
        path: '/user/info',
        name: 'Info',
        component: () => import('../views/InfoView.vue')
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

// TODO: 若开发时需要查看 /user/* 页面，可以注释下方代码
router.beforeEach((to, from, next) => {
  if (to.path.includes("/user")) { // 若访问路径为 /user/* 则需检查是否有 token (是否已登录)
      if (sessionStorage.getItem("token")) {
          return next()
      } else {
          return router.push({ // 若未登录，会强制跳转到 /login 页面
            name: "Login"
          })
      }
  }
  else {
    if (sessionStorage.getItem("token")) { // 若访问路径为 /* 且已登录，会自动跳转至用户界面
      return router.push({
        name: "Userhome"
      })
    } else {
        return next()
    }
  }
})

export default router
