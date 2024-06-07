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
