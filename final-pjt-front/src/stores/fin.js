import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useFinStore = defineStore('fin', () => {
  const productList = ref([])
  const optionList = ref([])
  const lst = ref([])
  const allOptionList = ref([])
  const getProduct = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/products/'
    })
    .then(res => {
      // console.log(res.data)
      productList.value = res.data
      
    })
    .catch(error => {
      console.log(error)
    })
  }

  const getAllOptionList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/options/'
    })
    .then(res => {
      allOptionList.value = res.data
      
    })
    .catch(error => {
      console.log(error)
    })
  }
  const getOption = function (prdt_pk) {
    axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/products/${prdt_pk}/`
  })
  .then(res => {
    console.log(res.data)
    optionList.value = res.data
    // lst.value = res.data.filter(p => p.save_trm=='6')
    // console.log(lst.value)
    // console.log(optionList.value)
  })
  .catch(error => {
    console.log(error)
  })

  }
  const joinedProductList = ref([])
  const joinProduct = function(prodcuctId, op){
    // getProduct()
    console.log(productList)
    const idx = productList.value.findIndex(prdt => prdt.id == prodcuctId)
    const product = productList.value[idx]
    console.log(product)
    const data = {
      'kor_co_nm': product.kor_co_nm,
      'fin_prdt_nm': product.fin_prdt_nm,
      'save_trm': op.save_trm,
      'intr_rate': op.intr_rate,
      'intr_rate2': op.intr_rate2
    }
    joinedProductList.value.push(data)
    console.log(joinedProductList.value)
  } 
  const label = ref([])
  const data1 = ref([])
  const data2 = ref([])
  // const searchdate = ref('')
  // const getSearchdate = function () {
  //   axios({
  //     method: 'get',
  //     url: 'http://127.0.0.1:8000/api/v1/exchange/'
  //   })
  //   .then(res => {
  //     console.log(res.data)
  //     searchdate.value = res.data
  //   })
  //   .catch((error) => {
  //     console.log('errorSearchdate')
  //     console.log(error)
  //   });
  // }
  // const rateList = ref([])
  // const getRateList = function () {
  //   const RATE_API_KEY=import.meta.env.VITE_SOME_EXCHANGE_API_KEY
  //   console.log(searchdate.value)
  //   axios({
  //     method: 'get',
  //     url: 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON',
  //     params: {
  //       'authkey': RATE_API_KEY,
  //       'data': 'AP01',
  //       'searchdate': searchdate.value
  //     }
  //   })
  //   .then(res => {
  //     console.log(res.data)
  //     rateList.value = res.data
  //   })
  //   .catch((error) => {
  //     console.log('errorRate')
  //     console.log(error)
  //   });
  // }
  const recommendList = ref([])
  const getRecommend = function (preference) {
    console.log(preference)
    recommendList.value = []
    const save_trm = allOptionList.value.filter(o => o.save_trm == preference['trm'])
    console.log("savetrmsavetrmsavetrmsavetrmsavetrmsavetrmsavetrm")
    console.log(save_trm)
    for (let i = 0; i < save_trm.length; i++) {
      productList.value.filter( p => {
        console.log(p.prdt_type == preference.type)
        if (p.id == save_trm[i].product) {
          console.log("기간 통과")
          if (p.kor_co_nm == preference.bank) {
            console.log("은행통과")
            if (p.prdt_type == preference.type) {
              console.log("타입 통과")
              console.log(p)
              recommendList.value.push(p.fin_prdt_nm)
              return true
            }
          }
        }
        return false
      })
    }
    console.log(recommendList.value.length)
    if (recommendList.value.length < 1) {
      return false
    } else {
      return recommendList.value
    }
  }

  return { productList, getProduct, allOptionList, getAllOptionList, optionList, getOption, joinedProductList, joinProduct, label, data1, data2, getRecommend, recommendList }
})
