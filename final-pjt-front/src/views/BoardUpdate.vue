<template>
  <div class="card">
    <div class="card-body">
      <h1>Article Edit</h1>
      <form ref="form" @submit.prevent="updateBoard">
        <div>
            <label for="title">제목</label>
            <textarea class="form-control" row="100" type="text" name="title" id="title" v-model="title" :placeholder="tit"  style="width: 470px;"></textarea>
            <!-- <div class="form-text">{{ store.board.title }}</div> -->
        </div>
        <div>
            <label for="content">내용</label>
            <textarea class="form-control" row="100" type="text" name="content" v-model="content" id="content" :placeholder="con"  style="width: 470px;"></textarea>
            <!-- <div class="form-text">{{ store.board.content }}</div> -->
        </div>
        <input type="submit" value="게시글수정" class="btn">
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
const title = ref('')
const content = ref('')
const router = useRouter()
const board = ref(null)
const tit = ref('')
const con = ref('')

onMounted(()=>{
  axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/boards/${route.params.id}/`
    })
      .then((response) => {
        console.log(response.data)
        board.value = response.data
        console.log(board.value.title)
        tit.value = board.value.title
        con.value = board.value.content
      })
      .catch((error) => {
        console.log(error)
      })
  console.log(board)
})

const updateBoard = function(){
  console.log()
  const data = {
    title : title.value,
    content : content.value
  }
  axios({
    method : 'put',
    url : `${store.API_URL}/api/v1/boards/${route.params.id}/`,
    data
  })
  .then((res)=>{
    router.push({name:'detail',params:{id:route.params.id}})
  })
  .catch((err)=>{
    console.log(data)
  })
}


// onMounted(() => {
//   axios({
//     method: 'get',
//     url: `${store.API_URL}/api/v1/boards/${route.params.id}/`
//   })
//     .then((response) => {
//       // console.log(response.data)
//       board.value = response.data
//       console.log(board.value)
//     })
//     .catch((error) => {
//       console.log(error)
//     })
// })
</script>

<style scoped>
#title{
  width: 80%;
  height: 50px;
  /* border: none; */
  resize: none;
}


  #content {
    width: 80%;
    height: 500px;
    /* border: none; */
    resize: none;
  }

  .btn{
  background-color: rgb(0,36,66);
  margin-top: 15px;
  margin-bottom: 15px;
  color: white;
}
.card{
    width: 500px;
    margin-left: 30%;
    margin-top: 5%;
    background-color: rgb(252, 251, 248);
}
</style>