<template>
  <!-- <tr> -->
    <tbody>
      <BoardListItem
      v-for="board in boardStore.boards"
      :key="board.id"
      :board="board"
      />
    </tbody>
  <!-- </tr> -->
</template>

<script setup>
import BoardListItem from '@/components/BoardListItem.vue'
import { useBoardStore } from '@/stores/board'

const boardStore = useBoardStore()
</script>

<style scoped>
a {
text-decoration: none;
color : black;
}
</style>