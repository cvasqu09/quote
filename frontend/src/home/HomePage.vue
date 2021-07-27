<template>
  <AddQuoteForm v-if="showForm" @onQuoteAdded="quoteAdded()" @onCancel="onCancel()"></AddQuoteForm>
  <div class="p-d-flex p-flex-wrap">
    <Quote v-for="quote of quotes" :quote="quote.text" :quoter="quote.quoter" :id="quote.id.toString()" class="p-mr-2 p-mb-2"
           :style="generateRandomColorStyle()"></Quote>
  </div>
  <div class="p-d-flex p-jc-end">
    <Button label="Add Quote" icon="pi pi-plus" class="p-mb-2 p-button-rounded" @click="toggleShowForm()"></Button>
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
    const loadQuotes = async () => {
      try {
        const response = await http.get('quote');
        quotes.value = response.data
      } catch (e) {
        console.log('error', e);
      }
    }

    onMounted(async () => {
      await loadQuotes();
    })

    const quoteAdded = async () => {

      await loadQuotes();
    }

    const onCancel = () => {
      showForm.value = !showForm.value;
    }


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
      quoteAdded,
      onCancel,
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
