<template>
  <div v-show="shouldShowForm">
    <AddQuoteForm @onQuoteAdded="quoteAdded()" @onCancel="onCancel()"></AddQuoteForm>
  </div>
  <QuoteList :quotes="quotes" :allow-delete="true"></QuoteList>
  <div class="p-d-flex p-jc-end">
    <Button label="Add Quote" icon="pi pi-plus" class="p-mb-2 p-button-rounded" @click="toggleShowForm()"></Button>
  </div>
</template>

<script>
import {onMounted, provide, ref} from "vue";
import http from "@utils/http";
import {computed} from "@vue/reactivity";
import AddQuoteForm from "@quote/AddQuoteForm.vue";
import Quote from "@quote/Quote.vue";
import QuoteList from "@quote/QuoteList.vue";

export default {
  name: "UserQuotePage",
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
}
</script>

<style scoped>
Button {
  height: 50px;
}
</style>
