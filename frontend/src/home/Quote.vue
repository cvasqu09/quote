<template>
  <Card class="quote-card">
    <template #content>
      <div class="p-d-flex p-jc-start">
        <span>"{{quote}}"</span>
      </div>
    </template>
    <template #footer>
      <div class="p-d-flex p-jc-end">
        <span class="quoter">{{quoter}}</span>
      </div>
    </template>
  </Card>
</template>

<script>
import {toRefs} from "@vue/reactivity";

export default {
  name: "Quote",
  props: {
    quote: {
      type: String,
      required: true
    },
    quoter: {
      type: String,
      required: true,
      default: 'Unknown'
    }
  },
  setup(props) {
    const { quote, quoter } = toRefs(props)
    return {
      quote, quoter
    }
  }
}
</script>

<style lang="scss" scoped>
.quote-card {
  min-width: 200px;
}

.quoter {
  font-style: italic;
}
</style>
