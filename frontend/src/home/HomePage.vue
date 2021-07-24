<template>
  <Button @click="toggleShowForm()">Add Quote</Button>
  <AddQuoteForm v-if="showForm"></AddQuoteForm>
</template>

<script>
import AddQuoteForm from "./AddQuoteForm.vue";
import {onMounted, ref} from "vue";
import http from "../utils/http";

export default {
  name: "HomePage",
  components: {AddQuoteForm},
  setup() {
    const showForm = ref(false);
    const toggleShowForm = () => showForm.value = !showForm.value

    onMounted(async () => {
      const quotes = await http.get('quote')
      console.log({quotes})
    })

    return {
      toggleShowForm,
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
