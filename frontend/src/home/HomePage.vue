<template>
  <Button @click="toggleShowForm()">Add Quote</Button>
  <AddQuoteForm v-if="showForm"></AddQuoteForm>
</template>

<script>
import AddQuoteForm from "./AddQuoteForm.vue";
import {ref} from "vue";

export default {
  name: "HomePage",
  components: {AddQuoteForm},
  setup() {
    const showForm = ref(false);
    const toggleShowForm = () => showForm.value = !showForm.value
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
