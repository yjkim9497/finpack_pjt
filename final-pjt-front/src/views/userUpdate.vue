<template>
  <div class="card">
    <div class="card-body">
      <h1>Update Profile</h1>
      <!-- {{ profile }} -->
      <form ref="form" @submit.prevent="update">
        <div class="mb-3">
          <label for="username" class="form-label">ID</label>
          <p>{{ profile.username }}</p>
          <!-- <input type="text" name="email" id="email" v-model="email" class="form-control" value=profile.username> -->
        </div>
        <div class="mb-3">
          <label for="age" class="form-label">나이  </label>
          <p>{{ profile.age }}</p>
          <!-- <input type="text" name="email" id="email" v-model="email" class="form-control"> -->
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">EMAIL</label>
          <input type="text" name="email" id="email" v-model="email" class="form-control" :placeholder="profile.email">
        </div>
        <div class="mb-3">
          <label for="asset" class="form-label">자산</label>
          <input type="text" name="asset" id="asset" v-model="asset" class="form-control" :placeholder="profile.asset">
        </div>
        <button type="submit" class="btn" id="btn">회원정보수정</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '@/stores/user';

const route = useRoute()

console.log(route.params.id)

const form = ref(null)
const email = ref('')
const asset = ref('')
const userStore = useUserStore()
const router = useRouter()
const profile = ref([])
userStore.getUsers()

onMounted(()=>{
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

    email.value = profile.email
    asset.value = profile.asset
})

const update = function(){
  const data2 = {
    email : email.value,
    asset : asset.value
  }
  userStore.update(data2)
  form.value.reset()
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

    email.value = profile.email
    asset.value = profile.asset

  router.replace({name:'profile'})
}



</script>

<style scoped>
.card{
    width: 500px;
    margin-left: 600px;
    margin-top:200px;
}

/* p{
  border: 1px solid ;
} */

#btn{
  background-color: rgb(0,36,66);
  margin-bottom: 15px;
  color: white;
}
</style>