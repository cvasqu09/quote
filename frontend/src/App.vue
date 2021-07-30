<template>
  <the-header></the-header>
  <router-view></router-view>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TheHeader from './ui/components/TheHeader.vue';

export default defineComponent({
  name: 'App',
  components: {
    TheHeader
  }
})
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

html {
  background-color: $gray-2;
}

body {
  color: $gray-7;
}

</style>
