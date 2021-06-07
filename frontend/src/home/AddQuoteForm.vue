<template>
  <div class="p-d-flex p-flex-column card">
    <h2 class="title">Add a quote</h2>
    <div class="p-fluid">
      <div class="p-field">
        <label for="quote">Quote</label>
        <TextArea id="quote" rows="4"></TextArea>
      </div>
      <div class="p-field">
        <label for="quoter">Quoter</label>
        <InputText id="quoter" type="text"></InputText>
      </div>
    </div>
    <Button class="submit-button">Submit</Button>
  </div>
</template>

<script>
export default {
  name: "AddQuoteForm"
}
</script>

<style scoped>
.title {
  width: fit-content;
}

.submit-button {
  width: fit-content;
  align-self: flex-end;
 }

label {
  float: left;
  width: fit-content;
}
</style>
