<template>
  <div class="p-d-flex p-jc-between">
    <h2>Home</h2>
    <span class="p-input-icon-left p-d-flex p-align-center">
      <i class="pi pi-search"/>
      <InputText type="text" v-model="searchText" placeholder="Search for quote/quoter"/>
    </span>
  </div>
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
import debounce from "lodash/debounce"
import useQuotes, {QuoteType} from "@/composables/useQuotes";

export default {
  name: "HomePage",
  components: {QuoteList},
  setup() {
    const quotes = ref([])
    const selectOptions = [
      {name: 'All', value: 'all'},
      {name: 'Most Liked', value: 'top'},
      {name: 'Most Quoted', value: 'quoted'}
    ]
    const searchText = ref('');
    const selectedOptionValue = ref(QuoteType.ALL);
    const {getQuotes, loading} = useQuotes();

    const loadQuotes = async (searchText) => {
      try {
        const response = await getQuotes(selectedOptionValue.value, searchText);
        quotes.value = response.data
      } catch (e) {
        console.log('error', e);
      }
    }

    const filterQuotes = debounce(async () => {
      await loadQuotes(searchText.value)
    }, 400)

    watch(searchText, async () => {
      await filterQuotes()
    })

    onMounted(async () => {
      await loadQuotes();
    })

    watch(selectedOptionValue, async () => {
      await loadQuotes(searchText.value);
    })

    return {
      loading,
      quotes,
      selectedOptionValue,
      selectOptions,
      searchText
    }
  }
};
</script>
