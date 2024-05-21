<script setup lang="ts">
import TextFieldComponent from './TextFieldComponent.vue';
</script>

<template>
  <div class="documentEditor">
    <h1 class="green">Document editor</h1>
    <h3>This area will contain editor.</h3>
    <div class="align-center">
      <div class="text-field-container">
        <TextFieldComponent msg="Introduction"/>
      </div>
      <div class="text-field-container">
        <TextFieldComponent msg="Method"/>
      </div>
      <div class="text-field-container">
        <TextFieldComponent msg="Result"/>
      </div>
      <div class="text-field-container">
        <TextFieldComponent msg="Discussion"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
.documentEditor {
  text-align: center;
}

.align-center {
  display: contents;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.text-field-container {
  margin: 10px 0;
}
</style>
