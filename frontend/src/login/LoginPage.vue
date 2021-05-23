<template>
  <div class="p-d-flex p-flex-column p-ai-center">
    <div class="p-col-12 p-md-4">
      <div class="p-inputgroup">
          <span class="p-inputgroup-addon">
              <i class="pi pi-user"></i>
          </span>
        <InputText v-model="username" placeholder="Username"/>
      </div>
    </div>

    <div class="p-col-12 p-md-4 p-d-flex p-flex-column">
      <div class="p-inputgroup p-mb-3">
          <span class="p-inputgroup-addon">
              <i class="pi pi-lock"></i>
          </span>
        <Password v-model="password" placeholder="Password" :feedback="false" :promptLabel="'test'"></Password>
      </div>
      <Button class="p-as-end p-sm-12" label="Submit" @click="submit"></Button>
    </div>
  </div>
</template>

<script>
import {inject, ref} from "vue";
import {useRouter} from "vue-router"

export default {
  name: "LoginPage",
  setup() {
    const router = useRouter();
    const http = inject('http');
    const username = ref('');
    const password = ref('');

    const submit = async () => {
      const res = await http.post('auth/', {
        username: username.value,
        password: password.value
      })

      const token = res?.data.token;
      localStorage.setItem('token', token);
      router.push({
        name: 'home'
      })
    }

    return {
      username, password, submit
    }
  }
}
</script>

<style scoped>

</style>
