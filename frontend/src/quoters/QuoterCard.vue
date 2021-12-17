<template>
  <Card>
    <template #title>
      {{quoter.name}}
    </template>
    <template #content>
      <h3>
        {{quoter.quote_count}}
      </h3>
    </template>
  </Card>
</template>

<script>

export default {
  name: "QuoterCard",
  props: {
    quoter: {
      type: Object,
      required: true,
      default: () => {}
    }
  }
}
</script>

<style scoped>

</style>
