import axios from "axios";
import store from "../store";

// 创建一个新的请求实例instance,instance.的用法和axios.的用法一致，可以使用instance({})、instance.get（）、instance.post()
const instace = axios.create({
  baseURL: import.meta.env.VITE_API_URL, // 默认配置(这里不要用process.env,个人百度这个在vite中被废弃掉了,属性名必须以VITE_API_开头,否则 import.meta.env检测不到)
  timeout: 50000, // 发送 http 请求的超时时间
});

// 配置请求拦截器,在请求之前的数据处理,比如在请求头添加token,所有的请求都会经过拦截器
instace.interceptors.request.use(
  //config:该参数表示当前请求的配置对象
  (config) => {
    console.log(config)
    if (sessionStorage.getItem("token")) {
      const jwtToken = sessionStorage.getItem("token")
      config.headers.Authorization = `Bearer ${jwtToken}`
    }
    return config;
  },
  (err) => {
    return Promise.reject(err); // 将错误消息挂到promise的失败函数上
  }
);

// 配置响应拦截器
instace.interceptors.response.use(
  (response) => {
    return response; // 这里的response就是请求成功后的res , response.data即是请求成功后回调函数内的参数res.data
  },
  (err) => {
    console.log(err)
    if (err.response.status == 401) {
      // alert('登录信息过期')
      // store.commit('logout')
    }
    return Promise.reject(err); //将错误消息挂到promise的失败函数上
  }
);

// 封装请求的api
const callapi = (method = "GET", url, data = {}) => {
  return instace({
    method,
    url,
    params: method === "GET" ? data : {},
    data: method === "POST" ? data : {},
  });
};
// 封装 GET 和 POST 请求函数
export const getapi = (url, data) => callapi("GET", url, data);
export const postapi = (url, data) => callapi("POST", url, data);