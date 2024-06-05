<template>
    <div class="card d-flex justify-content-center" style="position: relative;">
        <div class="card-body">
        <h1>Login</h1>

        <form ref="form" @submit.prevent="login">
            <div class="mb-3">
                <label for="username" class="form-label">아이디</label>
                <input type="text" name="username" id="username"  class="form-control">
            </div>
            <div class="mb-3">
                <label for="password">비밀번호</label>
                <input type="password" name="password" id="password"  class="form-control">
            </div>
            <button type="submit" class="btn">로그인</button>
        </form>
    </div>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios';
import {useRouter} from'vue-router'
import { useUserStore } from '@/stores/user';

const router = useRouter()
const form = ref(null)
const store = useUserStore()

const login = function() {
    const data = new FormData(form.value)
    store.login(data)
    form.value.reset()
    router.push({name:'main'})
}
    
</script>

<style scoped>
.card{
    width: 500px;
    margin-left: 30%;
    margin-top: 5%;
    background-color: rgb(252, 251, 248);
}

.btn{
  background-color: rgb(0,36,66);
  margin-bottom: 15px;
  color: white;
}
</style>