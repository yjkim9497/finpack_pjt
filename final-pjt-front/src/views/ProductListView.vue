<template>
  <div>
    <h1 class="mb-4">&nbsp;Fin Product List&nbsp;</h1>
    <table width="100%" class="table table-hover item">
      <thead>
        <tr class="align-middle">
          <!-- <th>id</th> -->
          <th ></th>
          <th>공시 제출월</th>
          <th>상품명</th>
          <th>금융회사명</th>
          <!-- <th>우대조건</th> -->
          <th>상품 타입</th>
        </tr>
      </thead>
      <tbody>
        <tr @click="getDetail(prdt.id)" v-for="prdt in store.productList" :key="prdt.prdt_id">
          <td style="padding-left: 25px;">
            <img v-if="prdt.kor_co_nm.slice(0,2)=='경남'" src="http://wiki.hash.kr/images/e/ea/%EA%B2%BD%EB%82%A8%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='신한'" src="http://wiki.hash.kr/images/6/6e/%EC%8B%A0%ED%95%9C%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='제주'" src="http://wiki.hash.kr/images/6/6e/%EC%8B%A0%ED%95%9C%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='광주'" src="http://wiki.hash.kr/images/5/51/%EC%A0%84%EB%B6%81%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='전북'" src="http://wiki.hash.kr/images/5/51/%EC%A0%84%EB%B6%81%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='한국'" src="http://wiki.hash.kr/images/8/8b/%EC%A0%9C%EC%9D%BC%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='우리'" src="http://wiki.hash.kr/images/9/9a/%EC%9A%B0%EB%A6%AC%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='수협'" src="http://wiki.hash.kr/images/1/18/%EC%88%98%ED%98%91%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='신협'" src="http://wiki.hash.kr/images/1/15/%EC%8B%A0%EC%9A%A9%ED%98%91%EB%8F%99%EC%A1%B0%ED%95%A9_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='토스'" src="@/image/토스.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='중소'" src="http://wiki.hash.kr/images/d/dd/%EA%B8%B0%EC%97%85%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='하나'" src="http://wiki.hash.kr/images/d/d7/%ED%95%98%EB%82%98%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='국민'" src="http://wiki.hash.kr/images/6/6c/%EA%B5%AD%EB%AF%BC%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='대구'" src="http://wiki.hash.kr/images/7/7a/%EB%8C%80%EA%B5%AC%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='부산'" src="http://wiki.hash.kr/images/e/ea/%EA%B2%BD%EB%82%A8%EC%9D%80%ED%96%89_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,2)=='농협'" src="http://wiki.hash.kr/images/4/46/%EB%86%8D%ED%98%91_%EB%A1%9C%EA%B3%A0.png" alt="">
              <img v-if="prdt.kor_co_nm.slice(0,7)=='주식회사 카카'" src="@/image/카카오뱅크.png" alt="#">
              <img v-if="prdt.kor_co_nm.slice(0,7)=='주식회사 케이'" src="http://wiki.hash.kr/images/7/72/%EC%BC%80%EC%9D%B4%EB%B1%85%ED%81%AC_%EB%A1%9C%EA%B3%A0.png" alt="#">

          </td>
          <td style="line-height: 40px;">&emsp;{{ prdt.dcls_month }}</td>

          <td style="line-height: 40px;" >{{ prdt.fin_prdt_nm }}</td>
          <td style="line-height: 40px;" >
            {{ prdt.kor_co_nm }}
          </td>
          <td style="line-height: 40px;"  v-if="prdt.prdt_type == 'deposit'">예금</td>
          <td style="line-height: 40px;"  v-else>적금</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useFinStore } from '@/stores/fin'
const store = useFinStore()
onMounted(() => {
store.getProduct()
})

import { useRouter } from 'vue-router';
const router = useRouter()
const getDetail = function (prdt_id) {
router.push({ name: 'productsDetail', params: { id: prdt_id } })
}


</script>

<style scoped>
h1 {
  color: rgb(0, 55, 104);  
  text-align: center;
  text-decoration: underline;
  text-underline-offset: 10px;
}
table {
border-top: 1px solid black;
border-collapse: collapse;
}
/* table, th, td {
border: 1px solid black;
border-radius: 10px;
} */
th, td {
text-align: start;
border-bottom: 1px solid black;
padding: 10px;
vertical-align: center;
}

th{
  background-color: rgb(246, 244, 235);
}

td{
  background-color: rgb(252, 251, 248);
  align-items: center;
}

/* tr, th, td {
border-style: outset;
border-style: ridge;
border-style: inset;
} */
img{
  height: 40px;

}

.item {
  font-family: "Noto Serif KR", serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}

br {
  line-height: 1px;
}

</style>
