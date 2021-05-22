<template>
  <section class="p-d-flex p-jc-between">
    <h2>Quote</h2>
    <div class="p-d-flex p-ai-center">
      <router-link to="/home">
        <Button label="Home" class="p-button-text"></Button>
      </router-link>
      <router-link to="/settings">
        <Button label="Settings" class="p-button-text"></Button>
      </router-link>
    </div>
  </section>
</template>

<script>
export default {
name: "TheHeader"
}
</script>

<style scoped>

</style>
