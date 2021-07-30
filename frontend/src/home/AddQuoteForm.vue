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
        <AutoComplete id="quoter" type="text" v-model="quoter"></AutoComplete>
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
import {ref} from "vue";
import {useToast} from "primevue/usetoast";

export default {
  name: "AddQuoteForm",
  setup(_, { emit }) {
    const toastService = useToast();

    const onSubmit = async () => {
      try {
        await http.post('quote/', {name: quoter.value, text: quote.value});
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
