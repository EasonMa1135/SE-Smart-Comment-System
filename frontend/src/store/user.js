import router from '../router'

export default{
    state:{ // 获取当前存储的数据，若无相关存储则为 null
        name:window.sessionStorage.getItem('name')?window.sessionStorage.getItem('name'):null,
        email:window.sessionStorage.getItem('email')?window.sessionStorage.getItem('email'):null,
        token:window.sessionStorage.getItem('token')?window.sessionStorage.getItem('token'):null,
    },
    mutations:{
        setToken(state, token){ // 设置 token 的接口
            sessionStorage.setItem("token",token)
            state.token=token
        },
        setEmail(state, email){ // 设置 Email 的接口
            sessionStorage.setItem("email",email)
            state.email=email
        },
        setUser(state, name){ // 设置用户名的接口
            sessionStorage.setItem("name",name)
            state.name=name
        },
        logout(state){ // 登出后清理当前存储的接口
            state.name=null
            state.token=null
            state.email=null
            sessionStorage.removeItem("token")
            sessionStorage.removeItem("name")
            sessionStorage.removeItem("email")
            router.push({
                name: "Itro"
            })
        }
    },
}