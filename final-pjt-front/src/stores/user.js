import { defineStore } from "pinia"
import { ref, computed } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"


export const useUserStore = defineStore("user" , () => {
    const token = ref(null)
    const API_URL = "http://127.0.0.1:8000"
    const users = ref([])
    const user_pk = ref(0)
    const user_id = ref(null)
    const router = useRouter()

    const signup = function(data) {
        axios({
            method : "post",
            url : `${API_URL}/accounts/signup/`,
            data
        }).then((response) => {
            console.log(response)
            // const password = password
            // login({username,password})
        })
    }

    const login = function(data) {
        axios({
            method : "post",
            url : `${API_URL}/accounts/login/`,
            data
        }).then((response) => {
            console.log(response.data)
            token.value = response.data.key
            console.log(token.value)
        }).catch((err)=>{
            alert('아이디 또는 비밀번호가 틀렸습니다.')
            router.push({name:'login'})
            console.log(err)
        })
    }

    const update = function(data){
        axios({
            method : "put",
            url : `${API_URL}/accounts/update/${users.value.pk}/`,
            data,
            headers:{
                Authorization:`Token ${token.value}`
            },
        }).then((response) => {
            console.log(response.data)
            console.log(users.value)
            // users.value = response.data
        })
    }

    const getUsers = function(){
        axios({
            method : 'get',
            url : `${API_URL}/accounts/user/`,
            headers:{
                Authorization:`Token ${token.value}`
            }
        }).then((res)=>{
            users.value = res.data
            user_pk.value=res.data
            user_id.value = res.data.id
            console.log(res.data)
        })
    }

    const logout = function(){
        axios({
          method : 'post',
          url : 'http://127.0.0.1:8000/accounts/logout/',
          headers: {
              Authorization: `Token ${token.value}`
            }
        })
        .then((res)=>{
          console.log('로그아웃')
          user.token = null
          router.push({name:'main'})
        })
      }

    const deleteUser = function(){
        axios({
            method : 'delete',
            url : `${API_URL}/accounts/delete/${users.value.pk}/`,
            headers:{
                Authorization:`Token ${token.value}`
            }
        }).then((res)=>{
            token.value = null
            users.value = []
            logout()
            console.log('회원탈퇴성공')
            router.push({name:'main'})
        })
    }

    // const isLogin = true

    const isLogin = computed(()=> {
        if(token.value === null){
            return false
        } else{
            return true
        }
    })

    return { token , API_URL , signup, login, users, getUsers, update, user_pk, isLogin, deleteUser }
}, {persist : true})
