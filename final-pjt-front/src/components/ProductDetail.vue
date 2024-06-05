<template>
    <div>
        <h1 id="goback" class="mb-3" @click="goback"> ⬅ back</h1>
        <h1 id="prdtName">&nbsp;{{ prdt.fin_prdt_nm }}</h1>
        <hr id="infoHr" class="px-4">
        <div id="info" class="row">
            <div class="col-xl-6 col-12 ps-4">
                <p>공시 제출월 : {{ prdt.dcls_month }}</p>
                <p>상품명: {{ prdt.fin_prdt_nm }}</p>
                <p>금융회사명: {{ prdt.kor_co_nm }}</p>
                <p>상품 타입: {{ prdt.prdt_type }}</p>
            </div>
            <div class="col-6 px-4">
                <table width="500px">
                    <tr>
                        <th>저축기간(월)</th>
                        <th v-for="op in store.optionList" :key="op.id">{{ op.save_trm }}</th>
                    </tr>
                    <tr>
                        <th>저축금리</th>
                        <td v-for="op in store.optionList" :key="op.id">{{ op.intr_rate }}</td>
                    </tr>
                    <tr>
                        <th>최대우대금리</th>
                        <td v-for="op in store.optionList" :key="op.id">{{ op.intr_rate2 }}</td>
                    </tr>
               </table>
            </div>
        </div>
        <br>
        <hr id="spclHr">
        <div id="info" class="ps-3">
            <p style="font-weight: 600;" v-if="prdt.spcl_cnd.includes('없음' || '해당무')">우대조건 없음</p>
            <div id="spcl_cnd" v-else style="width: 50%;padding-bottom:10px;">
                <p style="font-weight: 600;" >우대조건</p>
                <p class="ps-3"style="line-height:50px">{{ prdt.spcl_cnd }}</p>
            </div>
        </div>

        <hr id="spclHr">
        <div class="d-flex">
            <h4>가입하기&emsp;></h4>
            <button class="btn m-2 text-white" style="background-color:rgb(0,36,66);" v-for="op in store.optionList" :key="op.id"
            @click="joinProduct(op.id, op.product)">{{ op.save_trm }}개월</button>
        </div>
        
  
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useFinStore } from '@/stores/fin'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'

const store = useFinStore()
const user = useUserStore()
const route = useRoute()
const router = useRouter()
const goback = function () {
    router.go(-1)
}
onMounted(() => {
store.getOption(route.params.id)
})


const prdtId = route.params.id
const idx = store.productList.findIndex(prdt => prdt.id == prdtId)
const prdt = store.productList[idx]


const joinProduct = function (optionId, productId) {
    if (confirm("가입을 진행합니다") == true){ 
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/join/',
            data: {
                option_id: optionId,
                product_id: productId
            },
            headers: {
            Authorization: `Token ${user.token}`
            }
        })
            .then((response) => {
            console.log(response.data)
            })

            .catch((error) => {
            console.log(error)
            })
    }else {
        return false
    }
}

</script>

<style scoped>
#goback {
    font-size: 20px;
    color: rgb(0,36,66);
    padding-bottom: 10px;
}
#prdtName {
    color: rgb(0,36,66);
    margin-top: 5px;
    margin-bottom: 3px;
    font-family: "Noto Serif KR", serif;
    font-optical-sizing: auto;
    font-weight: bold;
    font-style: normal;

}
hr{
    margin-top: 10px;
    margin-bottom: 30px;
    border: 0;
}
#infoHr {
    background-color: rgb(0,36,66); opacity: 1;
    height: 3px;
}
#spclHr {
    background-color: rgb(0,36,66); opacity: 0.5;
        height: 1.5px;
}
table {
    border-top: 1px solid black;
    border-collapse: collapse;
}

th, td {
    text-align: center;
    border-bottom: 1px solid black;
    padding: 10px;
}
h4, #info > * {
    font-family: "Noto Serif KR", serif;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal;
}
h4 {
    font-weight: 600;
    padding-right: 20px;
    padding-top: 0.7rem;
}

</style>
