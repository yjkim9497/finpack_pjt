import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

export const useBoardStore = defineStore('board', () => {
  const user = useUserStore()
  const boards = ref([])
  const board = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  // const token = ref(null)

  const router = useRouter()

  const getBoards = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/boards/`,
      headers: {
        Authorization: `Token ${user.token}`
      }
    })
      .then(response => {
        console.log(response)
        boards.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const getBoard = function(pk){
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/boards/${pk}/`
    })
      .then((response) => {
        // console.log(response.data)
        board.value = response.data
        console.log(board.value)
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const commentList = ref([])

  const getComments = function(pk){
    axios({
      method : 'get',
      url:`${API_URL}/api/v1/boards/${pk}/comment_list/`
    })
    .then((res)=>{
      console.log(res.data)
      commentList.value = res.data
      // console.log(commentList.value)
    })
  }

  // const deleteComment = function(board_pk,comment_pk){

  //   axios({
  //     method : 'delete',
  //     url : `${API_URL}/api/v1/boards/${board_pk}/${comment_pk}/delete/`
  //   })
  //   .then((res)=>{
  //     console.log(res.data)
  //   })

  //   const index = commentList.value.findIndex((com)=> com.pk === comment_pk)
  //   commentList.value.splice(index,1)
  // }


  return { boards, API_URL, getBoards, getComments, commentList, getBoard, board }
})
