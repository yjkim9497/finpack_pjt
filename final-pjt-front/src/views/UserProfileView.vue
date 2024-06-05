<template>
    <div>
      <h1 style="margin-bottom: 10px;">&nbsp;{{ profile.username }} 's &nbsp;&nbsp;Profile&nbsp;</h1>
      <div class="profile">
        <!-- {{ imgurl }} -->
        <div class="name">
          <!-- <div class="h1"> -->
            <!-- <h1 class="h11">11</h1> -->
            <!-- {{ index }} -->
            <img v-if="index==0" src="@/image/people/per1.png" alt="">
            <img v-if="index==1" src="@/image/people/per2.png" alt="">
            <img v-if="index==2" src="@/image/people/per3.png" alt="">
            <img v-if="index==3" src="@/image/people/per4.png" alt="">
          <!-- </div> -->
        </div>
        <!-- <div>
          {{ userStore.user_pk.pk}}
        </div> -->
        <!-- <p>ID : {{ profile.username }}</p> -->
        <div class="detail">
          <RouterLink :to="{name : 'userUpdate',params: { id :userStore.user_pk.pk}}" class="btn" id="btn1">회원정보수정</RouterLink>
          <button class="btn" id="btn1" @click="userStore.deleteUser">회원탈퇴</button>
          <p><span class="badge rounded-pill text-bg-secondary">EMAIL</span>&emsp;{{ profile.email }}</p>
          <hr>
          <p><span class="badge rounded-pill text-bg-secondary">AGE</span>&emsp;{{ profile.age }}</p>
          <hr>
          <p v-if="profile.asset"> <span class="badge rounded-pill text-bg-secondary">ASSET</span>&emsp;{{ profile.asset }}</p>
          <p v-else> <span class="badge rounded-pill text-bg-secondary">ASSET</span><span>&emsp;자산을 등록해주세요</span> <RouterLink :to="{name : 'userUpdate',params: { id :userStore.user_pk.pk}}" class="badge rounded-pill text-bg-dark">자산등록 </RouterLink></p>
        </div>
      </div>
        <!-- 회원정보 수정으로 연결되면 좋을 듯 -->
        <hr>

        <div class="d-flex">
          <h4 style="line-height: 150%;">가입 금융상품 목록</h4>
          <button @click="showGraph" class="btn ms-4"> 가입상품비교</button>
        </div>
        <JoinListView v-if="show" class="chartView" />

          <div class="card" v-for="idx in finStore.label.length">
            <div class="card-body">
              <!-- {{ finStore.label[idx-1].slice(0,2) }} -->
              <h5 style="margin-bottom: 20px;">{{ finStore.label[idx-1] }}</h5>
              <!-- <br> -->
              <p><span class="badge text-white" style="background-color: #005AA7;">저축금리</span>&emsp;{{ finStore.data1[idx-1] }}%</p>
              <p><span class="badge text-white"style="background-color: rgb(0,36,66)">최고금리</span>&emsp;{{ finStore.data2[idx-1] }}%</p>
            </div>
            <div class="card-body">
              <img v-if="finStore.label[idx-1].slice(0,2)=='경남'" src="@/image/경남은행.jpg" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='신한'" src="@/image/신한뱅크.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='광주'" src="@/image/광주은행.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='한국'" src="@/image/한국스탠.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='우리'" src="@/image/우리은행.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='수협'" src="@/image/수협.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='신협'" src="@/image/신협.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='토스'" src="@/image/토스.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='중소'" src="@/image/기업은행.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='하나'" src="@/image/하나은행.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='국민'" src="@/image/국민은행.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='대구'" src="@/image/대구은행.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='부산'" src="@/image/부산은행.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='농협'" src="@/image/농협.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='전북'" src="https://i.namu.wiki/i/oGAAXkiOqr5a13DxcNnv8NEpc1gPP7S6MiNrLHOMJrl6R1svYMJcQ6ovLzrZjMQTbuFduIR_QbtQTc-ej2dBVSQ-La6C5lFl_q-2twvrrlo2LKwZUc57Hs3bIMN47oH3rw5bwa5n5PYTtmG8-CnrSw.svg" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='제주'" src="https://i.namu.wiki/i/aJt5aqqslK0U-2vUh-SkCilLQxwy9pUWKIBY9NctXuJmLi0GiVZFtKN56tGsxZFyHlehsY4zhDYag_5afkJ0NouVeOv3tqXCg6B9lcMRdCTp9Y_svQ1E5gJZcW2YDILyJhqMzXW4hFVb6SoSODvocw.svg" alt="">
              <img v-if="finStore.label[idx-1].slice(0,7)=='주식회사 케이'" src="https://i.namu.wiki/i/-lISqW1c6Uw8a9hjE-s7JVBem6Yav3hSZyOwbKB4qNJyWn-xXe3x29Gh7ddAcaNBgLhAwblZRw2Tty4Jl9aXEV3Or-WNyUAHsq73JIv_uUmS6uA6E3MS4Q-5-BZAjG6w5WhxOgKQPSrzeeCPk_hb9A.svg" alt="">
              <!-- <img v-if="finStore.label[idx-1].slice(0,2)=='우리'" src="@/image/우리은행.png" alt="">
              <img v-if="finStore.label[idx-1].slice(0,2)=='우리'" src="@/image/우리은행.png" alt=""> -->
            </div>
            <!-- <hr> -->
          </div>
        
      
    </div>

</template>

<script setup>
import JoinListView from './JoinListView.vue';
import { ref, onMounted } from 'vue'
// import { useRouter } from 'vue-router'
// const router = useRouter()
import { useUserStore } from '@/stores/user';
import { useFinStore } from '@/stores/fin'
import axios from 'axios';
const show = ref(false)
const finStore = useFinStore()
finStore.getProduct()

const imgurl = ref('')
const index = ref(0)

// const numbers = [];

// for(let i = 0; i <4 ; i++) {
// 	numbers.push(i + 1)
// }
onMounted(()=>{
  index.value = Math.floor(Math.random() * 3)
  imgurl.value = `@/image/people/per${index+1}.png`
})

const showGraph = function () {
  show.value = !show.value
}

// console.log(router)

// router.go(0)
const userStore = useUserStore()
userStore.getUsers()
const profile = ref([])
const prdt_lst = ref([])
const op_lst = ref([])
const join_lst = ref([])
const bank = ref([])
const prdt = ref([])
// const label = ref([])
const idx = ref('')
console.log("##################")
console.log(finStore.label)
onMounted(() => {
    finStore.label = []
    finStore.data1 = []
    finStore.data2 = []
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/profile/${userStore.users.pk}`
    })
    .then(res => {
      console.log(res.data)
      profile.value = res.data
    })
    .catch((error) => {
      console.log(error)
    });

    // console.log(finStore.productList)
    axios({
      method : 'get',
      url : `http://127.0.0.1:8000/api/v1/join/`,
      headers:{
        Authorization:`Token ${userStore.token}`
      },
    })
    .then((response)=>{
      console.log(finStore.allOptionList)
      console.log('*************')
      for (let i = 0; i < response.data.length; i++) {
        const product = finStore.productList.find(p => p.id == response.data[i].product_id)
        const option = finStore.allOptionList.find(o => o.id == response.data[i].option_id)
        console.log(product)
        console.log(option)
        const label = product.kor_co_nm + "\n" + product.fin_prdt_nm + "\n"+ "(" + option.save_trm + "개월)"
        console.log(label)
        prdt.value.push("("+product.prdt_type + ")"+ product.fin_prdt_nm)
        bank.value.push(product.kor_co_nm)
        finStore.label.push(label)
        finStore.data1.push(option.intr_rate)
        finStore.data2.push(option.intr_rate2)
      }
      // // console.log(finStore.productList)
      // for(let i = 0; i < response.data.length; i++){
      //   for(let j = 0; j < finStore.productList.length; j++){
      //     const op_id = ref('')
      //     if(finStore.productList[j].id == response.data[i].product_id){
      //       idx.value = response.data[i].product_id
      //       op_id.value = response.data[i].option_id

      //       axios({
      //         method: 'get',
      //         url: `http://127.0.0.1:8000/api/v1/products/${idx.value}/`
      //       })
      //       .then(res => {
      //         op_lst.value = res.data
      //         const op = ref('')
      //         for(let i = 0; i < res.data; i++){
      //           console.log(res.data[i])
      //           if(res.data[i].id ==op){
      //             console.log(res.data[i])
      //           }
      //         }
      //         const data = {
      //           product : finStore.productList[j],
      //           options : res.data,
      //           opId : op_id.value
      //         }
      //         prdt_lst.value.push(data)
      //       })
      //       .catch(error => {
      //         console.log(error)
      //       })
      //     }
      //   }
      // }
    console.log(finStore.label.length)
    })
})



</script>

<style scoped>
h1 {
  color: rgb(0, 55, 104);  
  text-decoration: underline;
  text-underline-offset: 10px;
}
.card{
  background-color: rgb(252, 251, 248);
  margin-bottom: 30px;
  width: 80%;
  display: block;
  /* font-size: 0; */
  padding: 10px;
}

img{
  width: 200px;
  margin-bottom: 50px;
  /* margin-right: 10px; */
  /* margin-left: -20px; */
}

.card-body{
  background-color: rgb(252, 251, 248);
  width: 50%;
  display: inline-block;
  padding: 5 5 5 5;
}

.profile{
  display: block;
  width: 70%;
  display: flex;
}

.name{
  width:320px;
  height: 100%;
  display: inline-block;
  text-align: center;
  /* display: flex; */
  /* align-items: center; */
  justify-content: center;
}
.detail{
  width:50%;
  display: inline-block;
}

a{
  text-decoration: none;
  color: black;
}

.badge{
  width: 65px;
}

.h1{
  /* margin-bottom: 5; */
  /* padding-bottom: -200px; */
  align-items: center;
  /* display: table-cell; */
  vertical-align: middle;
}

.h11{
  color: rgb(246, 244, 235);
}

.badge{
  padding: 6 6 6 26px;
  text-align: center;
}

div{
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

#btn1{
  margin-left: 500px;
  width: 120px;
}


@media screen and (min-width: 1800px) {
  .chartView {
    width: 50%;
    margin-left: 25%;
  
  }
}
@media screen and (min-width: 1500px) and (max-width: 1800px) {
  .chartView {
    width: 80%;
    margin-left: 20%;

  }
}
@media screen and (max-width: 1499px) {
  .chartView {
    width: 100%;
  }
}
</style>
