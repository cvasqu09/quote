<template>
  <div class="p-d-flex p-flex-column card p-mb-3">
    <Toast position="top-right"></Toast>
    <h2 class="title">Add a quote</h2>
    <div class="p-fluid">
      <div class="p-field">
        <label for="quote">Quote</label>
        <TextArea id="quote" rows="4" v-model="quote"></TextArea>
      </div>
      <div class="p-field p-d-flex p-flex-column">
        <label for="quoter">Quoter</label>
        <AutoComplete id="quoter.id" type="text" :suggestions="suggestedQuoters" @complete="getQuoters($event)"  v-model="quoter" field="name"></AutoComplete>
      </div>
    </div>
    <div class="p-d-flex p-jc-end">
      <Button class="p-button-outlined action-button p-mr-2" @click="onCancelSubmit()">Cancel</Button>
      <Button class="action-button" @click="onSubmit()">Submit</Button>
    </div>
  </div>
</template>

<script>
import http from "../utils/http";
import {onMounted, ref} from "vue";
import {useToast} from "primevue/usetoast";
import get from 'lodash/get';

export default {
  name: "AddQuoteForm",
  setup(_, {emit}) {
    const toastService = useToast();
    const suggestedQuoters = ref([]);

    const getQuoters = async (event) => {
      const quoters = await http.get('quoter/', {
        params: {search: event.query}
      })
      suggestedQuoters.value = quoters.data;
      console.log({quoters})
      console.log(suggestedQuoters.value)
    };

    const onSubmit = async () => {
      try {
        // Get existing user from auto complete or use as name
        const name = get(quoter.value, 'name', quoter.value)
        await http.post('quote/', {name: name, text: quote.value});
        toastService.add({severity: 'success', summary: 'Success!', detail: 'Quote added', life: 3000})
        emit('onQuoteAdded');
      } catch (e) {
        console.log('e', e)
      }
    }

    const onCancelSubmit = () => {
      emit('onCancel');
    }

    const quote = ref();
    const quoter = ref();

    return {
      quote,
      quoter,
      suggestedQuoters,
      getQuoters,
      onSubmit,
      onCancelSubmit,
    }
  }
}
</script>

<style scoped>
.title {
  width: fit-content;
}

.action-button {
  width: fit-content;
  align-self: flex-end;
}

label {
  float: left;
  width: fit-content;
}
</style>
