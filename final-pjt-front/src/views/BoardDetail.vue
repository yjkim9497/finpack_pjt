<template>
  <div>
    <h1 id="goback" class="mb-3" @click="goback"> ⬅ back </h1>
    <h1>Detail</h1>
    <div id ="item"v-if="board">
      <h1 id="prdtName">{{ board.title }}&emsp;&emsp;&emsp;</h1>
      <span class="pe-4">작성자 : {{ board.user.username }}</span>
      <span>작성일 : {{ board.created_at.slice(0,10) }}</span>
      <hr id="contentHr">
      <p  style="font-size: 20px; padding-left: 1.5rem; margin-bottom: 100px;">{{ board.content }}</p>

      <button @click="deleteBoard" v-if="board.user.username === userStore.users.username" class="btn btn-outline-secondary btn-sm" id="btn">게시글 삭제</button>
      <RouterLink :to="{name:'boardUpdate',params:{id:route.params.id}}" v-if="board.user.username === userStore.users.username" class="btn btn-outline-secondary btn-sm" id="btn">게시글 수정</RouterLink>
      <h3 class="mb-4">댓글 목록</h3>
      <div class="ps-3 pt-2"v-for="comment in store.commentList">
        <span v-if="comment.content">- {{ comment.content }} &emsp;</span>
        <button class="btn text-white p-0 px-1" style="font-size:12px;background-color: rgb(0,36,66);" @click="deleteComment(comment)">삭제</button>
        <hr class="mt-4"style="background-color: rgb(0,36,66); opacity: 0.5;">
      </div>
      <form class="ps-3"  @submit.prevent="createComment">
        <input style="height:30px;text-align:center;border:2px solid grey;border-radius: 10px; margin-right: 10px;" type="text" v-model.trim="content" id="content" placeholder="댓글을 입력해주세요." >
        
        <input class="text-white" style="font-size:12px;background-color: rgb(0,36,66);" type="submit" value="추가">
      </form>
    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useBoardStore } from '@/stores/board'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'

const store = useBoardStore()
const route = useRoute()
const board = ref(null)
const content = ref(null)
const router = useRouter()
const pk = ref(0)
const userStore = useUserStore()
const ck = ref(false)
const com_list = ref([])
console.log(route.params)

userStore.getUsers()
const goback = function () {
    router.go(-1)
}
// if(board.user.username === userStore.users.username){
//   ck.value = true
// }

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/boards/${route.params.id}/`
  })
    .then((response) => {
      // console.log(response.data)
      board.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })

  axios({
    method : 'get',
    url:`${store.API_URL}/api/v1/boards/${route.params.id}/comment_list/`
  })
  .then((res)=>{
    // store.commentList = res.data
    com_list.value = res.data
  })
})
store.getComments(route.params.id)

const createComment = function(){
    axios({
      method:'post',
      url:`${store.API_URL}/api/v1/boards/${route.params.id}/comment/`,
      data:{
        content : content.value
      },
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then((res) => {
      com_list.value.push(res.data)
      store.commentList.push(res.data)
      content.value = ''
    })
  }

  const deleteBoard = function(){
    axios({
      method : 'delete',
      url : `${store.API_URL}/api/v1/boards/${route.params.id}/delete/`
    })
    .then((res)=>{
      router.push({name:'board'})
    })
  }



  const deleteComment = function(comment){
    // const pk1 = comment_pk
    const index = com_list.value.findIndex((com)=> com.pk === comment.id)
    if(index!==-1){
      com_list.value.splice(index,1)
    }
    axios({
      method : 'delete',
      url : `${store.API_URL}/api/v1/boards/${route.params.id}/${comment.id}/delete/`
    })
    .then((res)=>{
      // for(let i = 0; i < com_list.value; i++){
      //   if(com_list[i].value.pk == comment_pk){
      //     com_list.value.splice(i,1)
      //   }
      // }
      console.log('댓글삭제')
      // router.go(0)
      // router.replace({name:'detail', params: {id : route.params.id}})
      console.log(com_list.value)
      store.getComments(route.params.id)
      
    })


  }

</script>

<style scoped>
#goback {
    font-size: 20px;
    color: rgb(0,36,66);
    padding-bottom: 10px;
}
#item {
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
  margin-left: 0.5rem;
  margin-top: 1.5rem;

}
#prdtName {
    color: rgb(0,36,66);
    margin-top: 5px;
    margin-bottom: 3px;
    font-family: "Noto Serif KR", serif;
    font-optical-sizing: auto;
    font-weight: bold;
    font-style: normal;
    text-decoration-thickness: 3px;
    margin-bottom: 20px;;
  

}
#contentHr {
  margin-top: 10px;
  margin-bottom: 10px;
  border: 0;
  background-color: rgb(0,36,66); opacity: 1;
  height: 2px;
}

#btn{
  background-color: rgb(0,36,66,0.6);
  margin-bottom: 15px;
  margin-right: 5px;
  color: white;
}

</style>
