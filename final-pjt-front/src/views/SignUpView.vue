<template>
    <div class="card">
        <div class="card-body">
            <h1>SignUp</h1>
            <form ref="form" @submit.prevent="signup">
                <div class="mb-3">
                    <label for="username" class="form-label">ID</label>
                    <input type="text" id="username" name="username" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="password1" class="form-label">PW</label>
                    <input type="password" name="password" id="password" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="email" class="form-label">EMAIL</label>
                    <input type="text" name="email" id="email" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="age" class="form-label">AGE</label>
                    <input type="text" name="age" id="age" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="asset" class="form-label">자산</label>
                    <input type="text" name="asset" id="asset" class="form-control">
                </div>
                <!-- <div>
                    <label for="password2">PW 확인</label>
                    <input type="password" name="password2" id="password2">
                </div> -->
                <button type="submit" class="btn">회원가입</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';

const form = ref(null)
const router = useRouter()

const store = useUserStore()

const signup = function() {
    const data = new FormData(form.value)

    store.signup(data)
    form.value.reset()
    router.push({name : "login"})
}

</script>

<style scoped>
/* .card{
    width: 500px;
    margin-left: 600px;
    margin-top: 50px;
} */

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