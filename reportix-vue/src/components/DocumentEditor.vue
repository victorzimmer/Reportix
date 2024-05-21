<script setup lang="ts">
import TextFieldComponent from './TextFieldComponent.vue';
</script>

<template>
  <div class="documentEditor overflow-y-scroll">
    <h1 class="green">Document editor</h1>
    <h3>This area will contain editor.</h3>
    <div class="">
      <div class="">
        <TextFieldComponent msg="Introduction"/>
      </div>
      <div class="">
        <TextFieldComponent msg="Method"/>
      </div>
      <div class="">
        <TextFieldComponent msg="Result"/>
      </div>
      <div class="">
        <TextFieldComponent msg="Discussion"/>
      </div>
    </div>
  </div>
</template>
