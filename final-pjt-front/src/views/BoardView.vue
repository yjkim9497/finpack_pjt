<template>
  <div>
    <div>
        <h1>&nbsp;Community&nbsp;</h1>
      <div class="d-flex justify-content-end">
        <RouterLink :to="{ name: 'create' }" class="btn">
          게시글 작성
        </RouterLink>
      </div>
    </div>
    <table width="100%" class="table table-hover">
      <thead>
        <tr class="item">
          <th>번호</th>
          <th>제목</th>
          <th>작성자</th>
        </tr>
      </thead>
        <BoardList />
    </table>

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'
import { RouterLink } from 'vue-router'
import BoardList from '@/components/BoardList.vue'

const store = useBoardStore()

onMounted(() => {
  store.getBoards()
})

</script>

<style scoped>
table {
border-top: 1px solid black;
border-collapse: collapse;
}

th {
text-align: start;
border-bottom: 1px solid black;
padding: 10px;
background-color: rgb(246, 244, 235);
}

a {
  text-decoration: none;
  color : white;
}
.item {
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}
.btn{
  background-color: rgb(0,36,66);
  margin-bottom: 15px;
  color: white;
}
h1 {
  color: rgb(0, 55, 104);  
  text-align: center;
  text-decoration: underline;
  text-underline-offset: 10px;
}
</style>