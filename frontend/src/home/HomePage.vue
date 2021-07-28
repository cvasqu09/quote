<template>
  <div v-show="shouldShowForm">
    <AddQuoteForm @onQuoteAdded="quoteAdded()" @onCancel="onCancel()"></AddQuoteForm>
  </div>
  <QuoteList :quotes="quotes"></QuoteList>
  <div class="p-d-flex p-jc-end">
    <Button label="Add Quote" icon="pi pi-plus" class="p-mb-2 p-button-rounded" @click="toggleShowForm()"></Button>
  </div>
</template>

<script>
import AddQuoteForm from "./AddQuoteForm.vue";
import {onMounted, provide, ref} from "vue";
import http from "../utils/http";
import Quote from "./Quote.vue";
import {computed} from "@vue/reactivity";
import QuoteList from "./QuoteList.vue";

export default {
  name: "HomePage",
  components: {Quote, AddQuoteForm, QuoteList},
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
    });

    const shouldShowForm = computed(() => showForm.value);

    const removeQuoteFromList = (index) => {
      quotes.value.splice(index, 1);
    }

    const quoteAdded = async () => {
      await loadQuotes();
      toggleShowForm();
    }

    const onCancel = () => {
      toggleShowForm();
    }

    provide('quotes', quotes);
    provide('removeQuote', removeQuoteFromList);

    return {
      quotes,
      quoteAdded,
      onCancel,
      toggleShowForm,
      removeQuoteFromList,
      shouldShowForm
    }
  }
};
</script>

<style scoped>
Button {
  height: 50px;
}
</style>
