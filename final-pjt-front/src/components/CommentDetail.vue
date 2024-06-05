<template>
  <div class="ps-3 pt-2">
    <span>- {{ comment.content }} &emsp;</span>
    <button class="btn text-white p-0 px-1" style="font-size:12px;background-color: rgb(0,36,66);" @click="deleteComment(comment)">삭제</button>
  </div>
</template>

<script setup>
defineprops({
  comment : Object,
})

const emit = defineEmits(['deleteComment'])

const deleteCom = function(com){
  emit('deleteComment', com)
}
</script>

<style scoped>

</style>