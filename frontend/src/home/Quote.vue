<template>
  <Card class="quote-card">
    <template #content>
      <div class="p-d-flex p-jc-between">
        <span>"{{quote}}"</span>
        <i class="pi pi-trash" @click="deleteQuote()"></i>
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
import http from "../utils/http";

export default {
  name: "Quote",
  props: {
    id: {
      type: String,
      required: true,
    },
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
    const { quote, quoter, id } = toRefs(props)
    const deleteQuote = async () => {
      console.log('deleting quote with id', id.value);
      try {
        await http.delete(`quote/${id.value}`)
      } catch(e) {
        console.log('error deleting', e);
      }

    }
    return {
      quote, quoter, deleteQuote
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
