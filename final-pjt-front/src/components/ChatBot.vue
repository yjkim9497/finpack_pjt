<template>
  <div >
      <!-- 채팅창 화면 -->
      <section class="container">
          <!-- 프로필 영역 -->
          <div class="top-area">
              <div class="profile-area">
                  <span class="mt-3" style="font-size: 25px; font-weight: bold; color: rgb(0,36,66);">-ˋˏ  </span>
                  <span class="mt-3" style="font-size: 25px; font-weight: bold; color: #005AA7;">&nbsp;FINTACK BOT&nbsp;</span>
                  <span class="mt-3" style="font-size: 25px; font-weight: bold; color: rgb(0,36,66);">ˎˊ- </span>
              </div>
          </div>
          <!-- 채팅 영역 -->
          <div class="chat-area">
            <div id="defaultChat">안녕하세요 FinPick 챗봇입니다.<br>무엇을 도와 드릴까요?</div>
              <div class="mt-3">
                <button class="btn me-2 mb-2 py-1 px-2" style="color: rgb(0,36,66); border:2px solid rgb(0,36,66);" @click="goRecommend">금융상품 추천</button>
                <button class="btn me-2 mb-2 py-1 px-2" style="color: rgb(0,36,66); border:2px solid rgb(0,36,66);" @click="goProducts">금융상품 전체 보기</button>
                <button class="btn me-2 mb-2 py-1 px-2" style="color: rgb(0,36,66); border:2px solid rgb(0,36,66);" @click="goMap">은행 찾기</button>
              </div>
              <div>
                <button v-if="userStore.isLogin" class="btn mt-1 me-3 mb-2 py-1 px-2" style="color: rgb(0,36,66); border:2px solid rgb(0,36,66);" @click="goBoard">소통하기</button>
              </div>
              <div v-if="userStore.isLogin">
                <button class="btn mt-1 me-3 mb-2 py-1 px-2" style="color: rgb(0,36,66); border:2px solid rgb(0,36,66);" @click="goProfileEdit">회원정보 수정하기</button>
              </div>
          </div>

          <!-- 채팅창 하단 영역 -->
          <div class="bottom-area mt-4 mb-2">
              <input class="chat-input p-2" style="text-align: right; background-color: #f8f8f886; border-radius: 10px;" type="text" placeholder="채팅을 입력해주세요 . . .   " />
          </div>
      </section>
  </div>
</template>


<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useFinStore } from '@/stores/fin';
import { useUserStore } from '@/stores/user';

const finStore = useFinStore()
const userStore = useUserStore()
userStore.getUsers()
const chatInput = ref(null)
const chatContainer = ref(null)
const router = useRouter()
const goRecommend = function () {
  addChat('send', '금융 상품 추천')
  chatReceive('금융상품 추천')
  
}
const goMap = function () {
  router.push({name : 'map'})
}
const goProducts = function () {
  router.push({name : 'products'})
}
const goBoard = function () {
  router.push({name : 'board'})
}
const goProfileEdit = function () {
  router.push(`/userUpdate/${userStore.user_pk.id}/`)
}
onMounted(() => {
  chatInput.value = document.querySelector('.chat-input')
  chatContainer.value = document.querySelector('.chat-area')
  
  chatInput.value.addEventListener('keyup', (e) => {
      e.key === 'Enter' && chatSubmit()
  })
})

const addChat = (type, value) => {
  if (!chatContainer.value) return
  const chat = document.createElement('div')
  chat.classList.add('chat')
  chat.innerText = value
  chat.style.cssText = 'border-radius: 10px; padding: 5px 15px;box-sizing: border-box;color: #f9fbff;width: fit-content;max-width: 70%;height: fit-content;word-break: break-all;margin: 5px 0;'
  if (type === 'send' ) {
    chat.style.alignSelf= 'flex-end'
    chat.style.backgroundColor='skyblue';

  } else {
    chat.style.justifyContent= 'end'
    chat.style.backgroundColor='#aab5b5';
  }
  chat.classList.add(`${type}-chat`)
  chatContainer.value.appendChild(chat)
  chatContainer.value.scrollTop = chatContainer.value.scrollHeight
}

const OPEN_API_URL = 'https://api.openai.com/v1/chat/completions'
const API_KEY = 'sk-proj-7NAfHvYObNjxuyGN4UHAT3BlbkFJVDaJmbzbGFE302qIi4QN'

const headers = {
  Authorization: `Bearer ${API_KEY}`,
  'Content-Type': 'application/json'
}

let oldMsg = ''
let preference = { type: null, bank: null, trm: null }

const responsePattern = function (preference) {
  if (!preference.type) {
    const response = '원하시는 상품의 유형을 입력해주세요'
    addChat('receive', response)
    oldMsg = response
  } else if (!preference.bank) {
    const response = '선호하는 은행이 있으신가요?'
    addChat('receive', response)
    oldMsg = response
  } else if (!preference.trm) {
    const response = '저축 기간은 1, 3, 6, 12, 24, 36 개월 중 선택해주세요.'
    addChat('receive', response)
    oldMsg = response
  } else {
    const recommendList = finStore.getRecommend(preference)
    if (recommendList) {
      const response = `상품을 추천드립니다. \n ${recommendList}`
      addChat('receive', response)
      oldMsg = response
    } else {
      const response = '조건에 맞는 상품이 없습니다'
      addChat('receive', response)
    oldMsg = response
    }
    preference = { type: null, bank: null, trm: null }
  }

}
const chatReceive = (userMsg) => {
  if (userMsg.includes('적금' || '예금')) {
      userMsg.replace('적금', 'saving').replace('예금', 'deposit')
      preference['type'] = userMsg
      responsePattern(preference)
  } else if (userMsg.includes('예금')) {
      preference['type'] = 'deposit'
      responsePattern(preference)
  } else if (userMsg.includes('은행') || userMsg.includes('없어' || '아니')) {
      preference['bank'] = userMsg
      responsePattern(preference)
  } else if ([1, 3, 6, 12, 24, 36].includes(Number(userMsg)) || userMsg.includes('개월')) {
    
      preference['trm'] = userMsg.replace(/[^0-9]/g, "")
      console.log(preference)
      responsePattern(preference)

  } else if (userMsg.includes('추천')) {
      const response = '원하시는 금융 상품 유형과 선호하는 은행 및 저축 기간을 입력해주세요.'
      addChat('receive', response)
      oldMsg = response
  } else {
      const messages = [
        { role: 'user', content: userMsg },
        { role: 'system', content: oldMsg },
        { role: 'user', content: '금융 상품 추천' },
        { role: 'system', content: '원하시는 상품의 유형이 있으신가요?' },
        { role: 'user', content: '적금' },
        { role: 'system', content: '선호하는 은행이 있으신가요?' },
        { role: 'user', content: "예금" },
        { role: 'system', content: "선호하는 은행이 있으신가요?" },
        { role: 'user', content: '적ㅡㅁ' },
        { role: 'system', content: '적금이 맞으시면 "적금" 이라고 다시 전송해주세요' },
        { role: 'user', content: 'ㅇㅖ금' },
        { role: 'system', content: '예금이 맞으시면 "예금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '저금' },
        { role: 'system', content: '적금이 맞으시면 "적금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '옉금' },
        { role: 'system', content: '예금이 맞으시면 "예금" 이라고 다시 전송해주세요' },
        { role: 'user', content: 'wjrrma' },
        { role: 'system', content: '적금이 맞으시면 "적금" 이라고 다시 전송해주세요' },
        { role: 'user', content: 'dPrma' },
        { role: 'system', content: '예금이 맞으시면 "예금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '져금' },
        { role: 'system', content: '적금이 맞으시면 "적금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '에금' },
        { role: 'system', content: '예금이 맞으시면 "예금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '적ㅡㅁ' },
        { role: 'system', content: '적금이 맞으시면 "적금" 이라고 다시 전송해주세요' },
        { role: 'user', content: 'ㅇㅖ금' },
        { role: 'system', content: '예금이 맞으시면 "예금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '저금' },
        { role: 'system', content: '적금이 맞으시면 "적금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '옉금' },
        { role: 'system', content: '예금이 맞으시면 "예금" 이라고 다시 전송해주세요' },
        { role: 'user', content: 'wjrrma' },
        { role: 'system', content: '적금이 맞으시면 "적금" 이라고 다시 전송해주세요' },
        { role: 'user', content: 'dPrma' },
        { role: 'system', content: '예금이 맞으시면 "예금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '져금' },
        { role: 'system', content: '적금이 맞으시면 "적금" 이라고 다시 전송해주세요' },
        { role: 'user', content: '에금' },
        { role: 'system', content: '예금이 맞으시면 "예금" 이라고 다시 전송해주세요' },
        { role: 'user', content: "은행" },
        { role: 'system', content: '저축 기간은 1, 3, 6, 12, 24, 36 개월 중 선택해주세요.' },
        { role: 'user', content: "dmsgod" },
        { role: 'system', content: '다시 입력해주세요' },
        { role: 'user', content: "으냉" },
        { role: 'system', content: '다시 입력해주세요' },
      ]

      axios.post(OPEN_API_URL, { model: 'gpt-3.5-turbo', messages }, { headers })
          .then(res => {
              console.log(res.data)
              const response = res.data.choices[0].message.content
              addChat('receive', response)
              oldMsg = response
          })
          .catch(err => {
              console.log(err.response.data)
              console.log(err.response.status)
          })
  }
}

const chatSubmit = () => {
  if (!chatInput.value) return
  const value = chatInput.value.value
  if (!value) return
  addChat('send', value)
  chatReceive(value)
  chatInput.value.value = ''
}

</script>

<style scoped>
div {
  bottom: 0;
  right: 0;
}
/* 채팅 영역 */
.chat-area {
  width: 100%;
  display: flex;
  flex: 1;
  padding: 10px;
  box-sizing: border-box;
  flex-direction: column;
  overflow-y: scroll;

}

.chat-area::-webkit-scrollbar {
  width: 10px;
}

.chat-area::-webkit-scrollbar-thumb {
  border-radius: 10px;
}

/* 전송, 수신 채팅 공통 */
#defaultChat {
  border-radius: 10px;
  padding: 5px 15px;
  box-sizing: border-box;
  width: fit-content;
  max-width: 70%;
  height: fit-content;
  word-break: break-all;
  margin: 5px 0;
  justify-content: end;
  background-color: #aab5b5;
}
.chat {
  border-radius: 30px;
  padding: 5px 15px;
  box-sizing: border-box;
  width: fit-content;
  max-width: 70%;
  height: fit-content;
  word-break: break-all;
  margin: 5px 0;
}

/* 전송한 채팅 */
.send-chat {
  align-self: flex-end;
}

/* 수신한 채팅 */
.receive-chat {
  justify-content: end;
}

/* 채팅 입력 iuput */
.chat-input {
  width: 100%;
  border: none;
  font-size: 16px;
}

.chat-input:focus {
  outline: none;
}

.chat-input::placeholder {
}

/** 
  그 외
*/
body {
  width: 100vw;
  height: 100vh;
  background: linear-gradient(180deg,
      skyblue 100%,
      #f9fbff 100%);
  display: flex;
  justify-content: center;
  align-items: center;
  margin: auto;
  max-width: 1280px;
  min-height: 576px;
}

/* 프로필, 채팅, 입력창을 담는 컨테이너 */
.container {
  width: 80%;
  height: 70%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 30px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25);
  position: relative;
  border: 3px solid rgb(0,36,66);
  background-color:#0059a72d;

}


.profile-area {
  display: flex;
  align-items: center;
}


.profile-area>span {
  margin-left: 10px;
  font-size: 20px;
  font-weight: semi-bold;
}

/* 입력창, 툴 */
.bottom-area {
  width: 100%;
  height: 13%;
  display: flex;
  padding: 10px 20px;
  box-sizing: border-box;
}

/* 프로필, 입력창의 툴 */
.tool-area {
  display: flex;
  align-items: center;
}


</style>
