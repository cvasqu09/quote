<template>
  <Button class="p-mb-2" @click="toggleShowForm()">Add Quote</Button>
  <AddQuoteForm v-if="showForm"></AddQuoteForm>
  <div class="p-d-flex p-flex-wrap">
    <Quote v-for="quote of quotes" :quote="quote.text" :quoter="quote.quoter" class="p-mr-2 p-mb-2"
           :style="generateRandomColorStyle()"></Quote>
  </div>
</template>

<script>
import AddQuoteForm from "./AddQuoteForm.vue";
import {onMounted, ref} from "vue";
import http from "../utils/http";
import Quote from "./Quote.vue";
import rc from "randomcolor";

export default {
  name: "HomePage",
  components: {Quote, AddQuoteForm},
  setup() {
    const showForm = ref(false);
    const quotes = ref([]);
    const toggleShowForm = () => showForm.value = !showForm.value

    onMounted(async () => {
      try {
        const response = await http.get('quote');
        quotes.value = response.data
      } catch (e) {
        console.log('error', e);
      }
      console.log(quotes.value)
    })

    const generateRandomColorStyle = () => {
      const color = rc.randomColor({
        luminosity: 'light'
      })
      return {
        'background-color': color,
      }
    }

    return {
      quotes,
      toggleShowForm,
      generateRandomColorStyle,
      showForm
    }
  }
};
</script>

<style scoped>
Button {
  height: 50px;
}
</style>
