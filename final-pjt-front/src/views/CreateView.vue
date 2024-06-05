<template>
  <div class="card">
    <div class="card-body">
      <h1>Create Article</h1>
      <form @submit.prevent="createBoard">
        <div>
          <label for="title">제목</label>
          <textarea class="form-control" row="100" v-model.trim="title" id="title" style="width: 470px;"></textarea>
        </div>
        <div>
          <label for="content">내용</label>
          <textarea class="form-control" row="100" v-model.trim="content" id="content"  style="width: 470px;"></textarea>
        </div>
        <input type="submit" class="btn" value="게시글작성">
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useBoardStore } from '@/stores/board'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const store = useBoardStore()
const user = useUserStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createBoard = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/boards/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${user.token}`
    }
  })
    .then((response) => {
      // console.log(response.data)
      router.push({ name: 'board' })
    })
    .catch((error) => {
      console.log(error)
    })
}

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
/* .card-body{
  width: 100%;
} */
</style>