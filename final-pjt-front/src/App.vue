<template>
  <div id="appDiv">
    <nav id="navbar" class="navbar navbar-expand-lg d-flex" style="background-color: rgb(0,36,66);" data-bs-theme="dark">
    <div class="container-fluid">
      <RouterLink :to="{ name: 'main' }" class="navbar-brand"><img id="logo" src="@/image/FINTACK.png" alt="logo" ></RouterLink>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon" style="color: white"></span>
      </button>
        <div class="collapse navbar-collapse justify-content-between" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink :to="{ name: 'products' }" style="color: white" class="nav-link active" aria-current="page">금융상품리스트</RouterLink>
            </li>
            <!-- <li class="nav-item">
              <RouterLink :to="{ name: 'exchange' }" class="nav-link active">환전</RouterLink>
            </li> -->
            <li class="nav-item">
              <RouterLink :to="{ name: 'map' }" style="color: white" class="nav-link active">지도</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'board' }" style="color: white" class="nav-link active">커뮤니티</RouterLink>
            </li>
          </ul>
            <ul class="navbar-nav">
              <li class="nav-item">
                <RouterLink :to="{ name: 'profile' }" style="color: white" class="nav-link active">회원정보</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'signup' }" v-if="!user.isLogin" style="color: white" class="nav-link active">회원가입</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'login' }" v-if="!user.isLogin" style="color: white" class="nav-link active">로그인</RouterLink>
              </li>
              <li class="nav-item">
                <button @click="logout" v-if="user.isLogin" style="color: white" class="nav-link active">로그아웃</button>
              </li>
              <!-- <li class="nav-item justify-content-end">
                <RouterLink :to="{ name: 'profile' }" style="color: white" class="nav-link active" v-if="user.token!=null && user.users.length!=0">{{ user.users.username }}</RouterLink>
              </li> -->
          </ul>
        </div>
    </div>
    </nav>

    <div class="m-4">
      <RouterView />
    </div>


  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import axios from 'axios';
import { useUserStore } from './stores/user';
import { useFinStore } from './stores/fin';
import { onMounted } from 'vue';

const user = useUserStore()
const finStore = useFinStore()
const router = useRouter()
onMounted(() => {
  finStore.getProduct()
  finStore.getAllOptionList()
  user.getUsers()
  console.log(user.users.username)
})


const logout = function(){
  axios({
    method : 'post',
    url : 'http://127.0.0.1:8000/accounts/logout/',
    headers: {
        Authorization: `Token ${user.token}`
      }
  })
  .then((res)=>{
    console.log('로그아웃')
    router.push({name:'main'})
    user.token = null
  })
}

</script>

<style scoped>
nav > * {
  margin-right: 10px;
}
#logo {
  width: 150px !important;
}
img{
  width:1000px;
}
li > * {
  color: white
}

nav{
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}

/* #appDiv{
  height: auto;
  min-height: 100%;
  padding-bottom: 100px;
} */


</style>
