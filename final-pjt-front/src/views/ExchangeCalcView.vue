<template>
  <div>
    <h1>Exchange</h1>
    <div>
      <select v-model="select1" >
        <option value="" selected>통화</option>
        <option v-for="cur in rateList" :value="cur.cur_unit">{{ cur.cur_unit }}</option>
      </select>
      <span>&nbsp;{{ cur1 }}&nbsp;</span>
      <input type="text" 
        v-model="inputValue1"
        placeholder="금액"
        style="text-align: end; width: 50px;">
      <span>&nbsp;{{ unit1 }}&nbsp;</span>
      <span>&emsp;→&emsp;</span>
      <select v-model="select2" >
        <option value="" selected>통화</option>
        <option v-for="cur in rateList" :value="cur.cur_unit">{{ cur.cur_unit }}</option>
      </select>
      <span>&nbsp;{{ cur2 }}&nbsp;</span>
      <span v-if="isNaN(result)">&emsp;</span>
      <span v-else >{{ result }}</span>
      <span>&nbsp;{{ unit2 }}&nbsp;</span>
    </div>
  </div>
</template>
  
<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios';
const rateList = ref([]) 
onMounted(() => {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/exchange/'
    })
    .then(res => {
      // console.log(res.data)
      rateList.value = res.data
    })
    .catch((error) => {
      console.log(error)
    });
})
const select1 = ref("")
const select2 = ref("")
let rate1 = 0
let rate2 = 0
let cur1 = ""
let cur2 = ""
let unit1 = ""
let unit2 = ""
const inputValue1 = ref("")
const result = ref('')
watch([select1, select2, inputValue1], ([newS1, newS2, newInput1]) => {
  const v1 = rateList.value[rateList.value.findIndex(cur => cur.cur_unit == newS1)]
  const v2 = rateList.value[rateList.value.findIndex(cur => cur.cur_unit == newS2)]
  if (v1 !== undefined && v2 !== undefined) {
    rate1 = v1['tts']
    rate2 = v2['tts']
    cur1 = v1['cur_nm'].split(" ")[0]
    unit1 = v1['cur_nm'].split(" ")[1] 
    cur2 = v2['cur_nm'].split(" ")[0]
    unit2 = v2['cur_nm'].split(" ")[1] 
  } else {
    rate1 = 0
    rate2 = 0
    cur1 = ""
    cur2 = ""
    unit1 = ""
    unit2 = ""
  }
  result.value = (rate1 / rate2 * newInput1).toFixed(2)
})

</script>

<style scoped>
</style>