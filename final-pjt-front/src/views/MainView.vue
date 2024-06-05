<template>
  <div>
    <div v-if="!isModalViewed" class="main" style="text-align: center; margin-right: 100px; font-weight: 800;">
      <p>내게 맞는 금융상품, 비교하기 힘드시죠?</p>
      <h3 style="font-weight:800;"><span id="fin">FINTACK</span>은 쉽고 정확하게 비교합니다.</h3>
    </div>
    <div class="cards" v-if="!isModalViewed">
      <div class="col">
        <div class="card" style="width: 18rem;">
          <img src="@/image/폴더.png" class="card-img" alt="...">
          <div class="card-body">
            <p class="card-text1">
              국내 최대 금융상품 데이터<br>
              금융 상품 데이터뿐만 아니라, 전원 실적,<br>
              한도 조건 등 복잡하고 어려운 금융상품의<br>
              각종 조건 데이터까지 모두 챙겼습니다.
            </p>
          </div>
        </div>
      </div>
      <div class="col">
      <div class="card" style="width: 18rem;">
        <img src="@/image/알고리즘.png" class="card-img" alt="...">
        <div class="card-body">
          <p class="card-text1">
            나만을 위한 금융매칭<br>
            수백만가지 경우의 수를 계산하는 추천<br>
            알고리즘이 나를 위한 맞춤 상품을<br>
            찾아드립니다.
          </p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card" style="width: 18rem;">
        <img src="@/image/차트.png" class="card-img" alt="...">
        <div class="card-body">
          <p class="card-text1">
            광고나 홍보 없음<br>
            팬팩의 추천에는 광고도, 홍보도<br>
            없습니다. 오직 객관적인 데이터만을<br> 
            활용합니다.
          </p>
        </div>
      </div>
    </div>
    </div>



    <!-- Button trigger modal -->
    <div v-if="!isModalViewed">
      <button id="exchange" class="btn" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" >환율 계산기</button>
  
      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasRightLabel">환율 계산기</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
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
                <br>
                <span>&emsp;&emsp;&emsp;&emsp;↓</span>
                <br>
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
      </div>

    </div>
    
    <!-- <button type="button" class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvasTop" aria-controls="offcanvasTop">
      환율계산기
    </button> -->

    <!-- Modal -->
    <!-- <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"> -->
      <!-- <div class="modal-dialog"> -->
        <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
          <div class="offcanvas-header">
            <h5 class="modal-title" id="exampleModalLabel">환율 계산기</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <div>
              <p>sssdfsdfsfd</p>
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
        </div>
      <!-- </div> -->
    <!-- </div> -->


    <div class="banner-container botAlertX">
      <div class="banner botAlert">
          <img id="bannerImg" style="width: 80px;transform: scaleX(-1); " src="@/image/botAlert.png" alt=""></img>
          <div class="banner-txt">hi</div>
      </div>
      
    </div>
      <button id="chatbot" v-if="!isModalViewed" @click="isModalViewed = !isModalViewed">
        
        <img class="shaking" src="@/image/bot.png" alt="">
      </button>
        
      <button id="chatbotX"  v-if="isModalViewed" @click="isModalViewed = !isModalViewed">X</button>
      <ChatBot class="m-0 p-0" v-if="isModalViewed"/>


            <div v-if="!isModalViewed" class=" p-4 pb-5 my-1 mt-1 mb-2" style="background-color: rgb(246, 244, 235);border-radius: 10px;margin-top: 50px;">
        <h1 class="pick mb-4">FINTACK's&nbsp;&nbsp;<span style="color: orangered;">Pick!</span>&nbsp;&nbsp;</h1>
        <div class="d-flex justify-content-around">
          <div class="card p-1 pt-3 mx-1" style="width: 20rem;" @click="getDetail(30)">
            <div class="d-flex">

              <img src="http://wiki.hash.kr/images/4/46/%EB%86%8D%ED%98%91_%EB%A1%9C%EA%B3%A0.png" style="width: 5rem;" class="card-img-top" alt="...">
              <p class="card-title fw-bold" style="font-size: 17px;line-height: 300%;">NH 고향사랑 기부 예금</p>
            </div>
            <div class="card-body mt-1">
              <p><span class="badge text-white" style="background-color: #005AA7;">저축금리</span>&emsp;3.1% (6개월)</p>
              <p><span class="badge text-white"style="background-color: rgb(0,36,66)">최고금리</span>&emsp;3.9% (6개월)</p>
            </div>
          </div>
          <div class="card p-1 pt-3 mx-1" style="width: 20rem;" @click="getDetail(77)">
            <div class="d-flex">

              <img src="http://wiki.hash.kr/images/6/6c/%EA%B5%AD%EB%AF%BC%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" style="width: 5rem;" class="card-img-top" alt="...">
              <p class="card-title fw-bold" style="font-size: 17px;line-height: 300%;">&nbsp;&nbsp;KB 차차차 적금</p>
            </div>
            <div class="card-body mt-1">
              <p><span class="badge text-white" style="background-color: #005AA7;">저축금리</span>&emsp;2.5% (12개월)</p>
              <p><span class="badge text-white"style="background-color: rgb(0,36,66)">최고금리</span>&emsp;8.0% (12개월)</p>
            </div>
          </div>
          <div class="card p-1 pt-3 mx-1" style="width: 20rem;" @click="getDetail(69)">
            <div class="d-flex">

              <img src="http://wiki.hash.kr/images/d/dd/%EA%B8%B0%EC%97%85%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" style="width: 5rem;" class="card-img-top" alt="...">
              <div>
                <p class="card-title fw-bold" style="font-size: 17px;line-height: 300%;">&nbsp;&nbsp;IBK 탄소제로 적금</p>
                <p style="text-align: end; font-size: 10px;line-height: 1%;">(자유적립식)</p>
              </div>
            </div>
            <div class="card-body mt-1">
              <p><span class="badge text-white" style="background-color: #005AA7;">저축금리</span>&emsp;3.0% (12개월)</p>
              <p><span class="badge text-white"style="background-color: rgb(0,36,66)">최고금리</span>&emsp;7.0% (12개월)</p>
            </div>
          </div>
        </div>
        
      </div>
      <footer v-if="!isModalViewed">
      <p>김연지 | 번호 : 010-6340-1824 | Email : yj009977@gmail.con | 주소 : 광주광역시 광산구 하남산단6번로 107 <br>
      정하림 | 번호 : 010-2515-3190 | Email : souffle1903@gmail.con | 주소 : 광주광역시 광산구 하남산단6번로 107</p>
      팬팩은 국내 100여개의 예적금 상품을 비교하여 누구나 유리한 상품을 선택하도록 돕습니다.
      <br>
      <p>FanPack Co., Ltd. All rights reserved.</p>
    </footer>
  </div>
</template>
  
<script setup>
import ChatBot from '@/components/ChatBot.vue'
import { ref, onMounted, watch } from 'vue'
import axios from 'axios';
const isModalViewed = ref(false)
import { useFinStore } from '@/stores/fin'
const store = useFinStore()

import { useRouter } from 'vue-router';
const router = useRouter()
const getDetail = function (prdt_id) {
router.push({ name: 'productsDetail', params: { id: prdt_id } })
}

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
.carousel{
  padding-left: 300px;
}

.btn{
  background-color: rgb(0,36,66);
  margin-bottom: 15px;
  color: white;
}
#chatbot {
  position: absolute;
  bottom: 30px;
  right: 20px;
  background-color: transparent;
  border: 0;
}
#chatbotX{
  font-size: 30px;
  font-weight: bold;
  border: 0;
  background-color: transparent;
  margin-left: 87%;
  margin-bottom: 0;
  color: rgb(0,36,66);
}

.shaking {
  width: 70px;
  height: 70px;
  animation-duration: 0.5s;
  animation-name: shake ;
  animation-iteration-count:8;
}

@keyframes shake {
  0% {
    transform: rotate(0deg)
    }
  25% {
      transform: rotate(-10deg);
    }
  50% {
      transform: rotate(0deg);
    }
  75% {
      transform: rotate(10deg);
    }
  100% {
      transform: rotate(0deg);
    }
}

.botAlert {
  animation: fadeout 5s; 
  animation-fill-mode: forwards;
  
}


@keyframes fadeout {
	from {
		opacity: 1;
	}
	to{
		opacity: 0;
	}
}

.banner {
  background-image: url(/src/bgimg/banner.png);
  background-size: cover; /* 핵심코드 */
  position: relative; /* 핵심코드 */
  display : inline-block;
  max-width: 100%;
  background-repeat :no-repeat;
}

.banner-txt {
  position: absolute; /* 핵심코드 */
  top: 45%; /* 핵심코드 */
  left: 50%; /* 핵심코드 */
  transform: translate( -50%, -50%); /* 핵심코드 */
  font-size: 30px;
  color: #FFFDE4;
}
.banner-container {
  position: absolute;
  bottom: 110px;
  right: 50px;
}
.pick {
  color: rgb(0, 55, 104);  
  text-decoration: underline;
  text-underline-offset: 10px;
}

.cards{
  display: flex;
  margin-left: 50px;
}
.card-img{
  margin-left: 120px;
  width: 200px;
}

#fin{
  font-family: "Freeman", sans-serif;
        font-weight: 400;
        font-style: normal;
}
.card{
  border: none;
  background-color: rgb(252, 251, 248);
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
  text-align: center;
  margin-bottom: 30px
}
.card-body{
  width: 400px;
}

.card-text1{
  margin-left: 25px;
}
.pick {
  color: rgb(0, 55, 104);  
  text-decoration: underline;
  text-underline-offset: 10px;
}

#exchange{
  position: absolute;
  top : 80px;
  right: 8px;
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}

footer{
  height: 70px;
  margin-left: 20px;
  font-size: small;
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
  /* top : 8px; */
  /* right: 8px; */
  /* position : relative;
  transform : translateY(-100%); */
  /* background-color: rgb(0,36,66); */
}

.main{
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-style: normal;
}
select {
  font-family: "Noto Serif KR", serif;
}
</style>
  
