<template>
  <div class="p-d-flex p-jc-between">
    <h2>Home</h2>
  </div>
  <TabView v-model:activeIndex="activeIndex" class="tabview">
    <TabPanel header="Quotes">
      <div class="p-d-flex p-jc-end">
        <span class="p-input-icon-left">
          <i class="pi pi-search"/>
          <InputText type="text" v-model="searchText" placeholder="Search for quote/quoter"/>
        </span>
      </div>
      <SelectButton class="p-mb-2" v-model="selectedOptionValue" :options="selectOptions" optionLabel="name"
                    optionValue="value"></SelectButton>
      <ProgressSpinner v-if="quotesLoading"/>
      <template v-else>
        <QuoteList :quotes="quotes"></QuoteList>
      </template>
    </TabPanel>
    <TabPanel header="Quoters">
      <ProgressSpinner v-if="quotersLoading"/>
      <div v-else>
        <div class="p-d-flex">
          {{selectedQuoter}}
          <DataTable :value="quoters" :paginator="true" :rows="10"
                     selectionMode="single"
                     v-model:selection="selectedQuoter"
                     paginatorTemplate="CurrentPageReport FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink RowsPerPageDropdown"
                     currentPageReportTemplate="Showing {first} to {last} of {totalRecords}"
                     :rowsPerPageOptions="[10,20,50]" >
            <Column field="name" header="Quoter"></Column>
            <Column field="quote_count" header="Number of Quotes"></Column>
            <Column field="likes" header="Number of Likes"></Column>
          </DataTable>
        </div>
        <Card>
          <template #title>

          </template>
        </Card>
      </div>
    </TabPanel>
  </TabView>
</template>

<script>

import {onMounted, watch} from "vue";
import {ref} from "@vue/reactivity";
import QuoteList from "@/quotes/QuoteList";
import debounce from "lodash/debounce"
import useQuotes, {QuoteType} from "@/composables/useQuotes";
import useQuoters, {QuoterType} from "@/composables/useQuoters";
import QuoterCard from "@/quoters/QuoterCard";

export default {
  name: "HomePage",
  components: {QuoteList, QuoterCard},
  setup() {
    const quotes = ref([])
    const quoters = ref([])
    const activeIndex = ref(0);
    const selectOptions = [
      {name: 'All', value: QuoteType.ALL},
      {name: 'Most Liked', value: QuoteType.TOP},
    ]

    const selectedQuoter = ref(null);
    const searchText = ref('');
    const selectedOptionValue = ref(QuoteType.ALL);
    const {getQuotes, quotesLoading} = useQuotes();
    const {getQuoters, quotersLoading} = useQuoters();

    const loadQuotes = async (searchText) => {
      try {
        const response = await getQuotes(selectedOptionValue.value, searchText);
        quotes.value = response.data
      } catch (e) {
        console.log('error', e);
      }
    }

    const loadQuoters = async () => {
      try {
        const response = await getQuoters(QuoterType.TOP)
        quoters.value = response.data
      } catch(e) {
        console.log('quoter error', e)
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

    watch(activeIndex, async() => {
      if (activeIndex.value === 1) {
        await loadQuoters();
      }
    })

    return {
      quotesLoading,
      quotes,
      quotersLoading,
      quoters,
      selectedOptionValue,
      selectedQuoter,
      selectOptions,
      searchText,
      activeIndex
    }
  }
};
</script>
<style lang="scss" scoped>
.tabview :deep(.p-tabview-nav) {
  background: none;
  border: none;
}

.tabview :deep(.p-tabview-panels) {
  background: none;
  padding: 1rem 0;
}

.quoter-card {
  min-width: 20rem;
}

</style>
