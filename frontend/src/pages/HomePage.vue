<template>
  <h2>Home</h2>
  <SelectButton class="p-mb-2" v-model="selectedOptionValue" :options="selectOptions" optionLabel="name"
                optionValue="value"></SelectButton>
  <ProgressSpinner v-if="loading"/>
  <template v-else>
    <QuoteList :quotes="quotes"></QuoteList>
  </template>
</template>

<script>

import {onMounted, watch} from "vue";
import {ref} from "@vue/reactivity";
import QuoteList from "@/quotes/QuoteList";
import useQuotes, {QuoteType} from "@/composables/useQuotes";

export default {
  name: "HomePage",
  components: {QuoteList},
  setup() {
    const quotes = ref([])
    const selectOptions = [
      {name: 'All', value: 'all'},
      {name: 'Top', value: 'top'},
    ]
    const selectedOptionValue = ref(QuoteType.ALL);
    const {getQuotes, loading} = useQuotes();

    const loadQuotes = async () => {
      try {
        const response = await getQuotes(selectedOptionValue.value);
        quotes.value = response.data
      } catch (e) {
        console.log('error', e);
      }
    }

    onMounted(async () => {
      await loadQuotes();
    })

    watch(selectedOptionValue, async () => {
      await loadQuotes();
    })

    return {
      loading,
      quotes,
      selectedOptionValue,
      selectOptions
    }
  }
};
</script>
