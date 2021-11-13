<template>
  <h2>Home</h2>
  <SelectButton class="p-mb-2" v-model="selectedOptionValue" :options="selectOptions" optionLabel="name"
                optionValue="value"></SelectButton>
  <QuoteList :quotes="quotes"></QuoteList>
</template>

<script>

import {onMounted, watch} from "vue";
import {ref} from "@vue/reactivity";
import http from "@utils/http";
import QuoteList from "@quote/QuoteList.vue";

export default {
  name: "HomePage",
  components: {QuoteList},
  setup() {
    const quotes = ref([])
    const selectOptions = [
      {name: 'All', value: 'all'},
      {name: 'Top', value: 'top'},
    ]
    const selectedOptionValue = ref('all');

    const loadQuotes = async () => {
      try {
        const response = await http.get(`quote?type=${selectedOptionValue.value}`);
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
      quotes,
      selectedOptionValue,
      selectOptions
    }
  }
};
</script>

<style scoped>
</style>
