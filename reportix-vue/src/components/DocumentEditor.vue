<script setup lang="ts">
import TextFieldEditor from './editor/TextFieldEditor.vue'
</script>

<template>
  <div class="documentEditor">
    <TextFieldEditor textFieldName="Introduction" />
    <TextFieldEditor textFieldName="Methods" />
    <TextFieldEditor textFieldName="Results" />
    <TextFieldEditor textFieldName="Discussion" />
    <TextFieldEditor textFieldName="Conclusion" />
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
