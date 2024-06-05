<template>
  <tr class="item">
    <td>{{ board.id }}</td>
    <td><RouterLink :to="{name:'detail',params:{id:board.id}}">{{ board.title }}</RouterLink></td>
    <td>{{ board.user.username }}</td>
  </tr>
</template>

<script setup>
import { RouterLink} from 'vue-router'

defineProps({
  board : Object
})
</script>

<style scoped>
td {
text-align: start;
border-bottom: 1px solid black;
padding: 10px;
background-color: rgb(252, 251, 248);
}
a {
  color : black;
  text-decoration: none;
}

.item {
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}
.item > * {
  height: 55px;
  line-height: 40px;
}

</style>