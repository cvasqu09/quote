<template>
  <div class="p-d-flex p-flex-wrap">
    <Quote v-for="(quote, index) in quotes" :key="quote.id.toString()" :quote="quote.text" :quoter="quote.quoter"
           :allow-delete="allowDelete"
           :id="quote.id.toString()" class="p-mr-2 p-mb-2"
           :style="generateRandomColorStyle()" @delete="removeQuoteFromList(index)"></Quote>
  </div>
</template>

<script>
import Quote from "./Quote.vue";
import rc from "randomcolor";
import {inject} from "@vue/runtime-core";

export default {
  name: "QuoteList",
  components: {Quote},
  props: {
    quotes: {
      type: Array,
      required: true,
      default: () => []
    },
    allowDelete: {
      type: Boolean,
      required: false,
      default: () => false
    }
  },
  setup() {
    const removeQuoteFromList = inject('removeQuote')
    const generateRandomColorStyle = () => {
      const color = rc.randomColor({
        luminosity: 'light'
      })
      return {
        'background-color': color,
      }
    }

    return {
      generateRandomColorStyle,
      removeQuoteFromList
    }
  }
}
</script>

<style scoped>

</style>
