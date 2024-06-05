<template>
  <div>
    <div v-for="prdt in prdt_lst">
      <!-- {{ prdt }} -->
    </div>
    <canvas id="myChart"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';
import { useUserStore } from '@/stores/user'
import { useFinStore } from '@/stores/fin'
import axios from 'axios';
const userStore = useUserStore()
userStore.getUsers()
const finStore = useFinStore()
// finStore.getProduct()
const prdt_lst = ref([])

const plst = ref([])
const rate1 = ref([])
const rate2 = ref([])
onMounted(()=>{
  plst.value = finStore.label
  rate1.value = finStore.data1
  rate2.value = finStore.data2
  console.log(plst)
  console.log(rate1)
  console.log(rate2)
  // axios({
  //       method : 'get',
  //       url : `http://127.0.0.1:8000/api/v1/join/`,
  //       headers:{
  //         Authorization:`Token ${userStore.token}`
  //       },
  //     })
  //     .then((res)=>{
  //       for(let i = 0; i < res.data.length; i++){
  //         for(let j = 0; j < finStore.productList.length; j++){
  //           if(finStore.productList[j].id == res.data[i].product_id){
  //             console.log(finStore.productList[j])
  //             finStore.getOption(res.data[i].product_id)
  //             const data = {
  //               product : finStore.productList[j],
  //               options : finStore.optionList
  //             }
  //             // console.log(finStore.productList[j].fin_prdt_nm)
  //             prdt_lst.value.push(data)
  //             // plst.value.push(finStore.productList[j].fin_prdt_nm)
  //             // rate1.value.push(finStore.optionList[0].intr_rate)
  //             // rate2.value.push(finStore.optionList[0].intr_rate2)
  //           }
  //         }
  
  //       }

  //       for(let i = 0; i < prdt_lst.value.length; i++){
  //         // console.log(prdt_lst.value[i].product.fin_prdt_nm)
  //           plst.value.push(prdt_lst.value[i].product.fin_prdt_nm)
  //           // rate1.value.push(prdt_lst.value[i].options[0] .intr_rate)
  //           // rate2.value.push(prdt_lst.value[i].options[0] .intr_rate2)
  //       }
  //       for(let i = 0; i < prdt_lst.value.length; i++){
  //         // console.log(prdt_lst.value[i].product.fin_prdt_nm)
  //           // plst.value.push(prdt_lst.value[i].product.fin_prdt_nm)
  //           rate1.value.push(prdt_lst.value[i].options[0].intr_rate)
  //           // rate2.value.push(prdt_lst.value[i].options[0] .intr_rate2)
  //       }
  //       for(let i = 0; i < prdt_lst.value.length; i++){
  //         console.log( prdt_lst.value[i])
  //           rate2.value.push(prdt_lst.value[i].options[0].intr_rate2)
  //       }


  //     })

      
    })

    
  //   console.log(plst.value)




// Chart.js의 모든 구성 요소를 등록합니다.
Chart.register(...registerables);

const labels = plst.value
// console.log(labels)
// const labels = ['우리', '신한', '하나', '국민', '농협', '수협', 'IBK'];

const data = {
  labels: finStore.label,
  datasets: [
    {
      label: '저축 금리',
      data : finStore.data1,
      // data: [1, 2, 3, 4, 5, 6, 7],
      borderColor: '#005AA7',
      backgroundColor: 'rgba(0, 55, 104, 0.2)',
      borderWidth: 2
    },
    {
      label: '최고 금리',
      data : finStore.data2,
      // data: [4, 5, 6, 7, 8, 9, 10],
      borderColor: 'rgb(0,36,66)',
      backgroundColor: 'rgb(0,36,66,0.5)',
      borderWidth: 2
    },
  ]
};

const config = {
  type: 'bar',
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
        labels: {
                  font: { size: 20 }
                },
      },
      title: {
        display: true,
        text: '나의 가입현황',
        font: { size: 20 }
      }
    }
  },
};

onMounted(() => {
  var myChart = new Chart(
    document.getElementById('myChart'),
    config
  );
});
</script>

<style scoped>
</style>
