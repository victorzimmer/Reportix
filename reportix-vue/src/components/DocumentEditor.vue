<script setup lang="ts">
import TextFieldEditor from './editor/TextFieldEditor.vue'
</script>

<template>
  <div class="documentEditor">
    <TextFieldEditor
      textFieldName="Introduction"
      endpoint="/textfields/introduction"
      propertyName="content"
    />
    <TextFieldEditor
      textFieldName="Methods"
      endpoint="/textfields/methods"
      propertyName="content"
    />
    <TextFieldEditor
      textFieldName="Results"
      endpoint="/textfields/results"
      propertyName="content"
    />
    <TextFieldEditor
      textFieldName="Discussion"
      endpoint="/textfields/discussion"
      propertyName="content"
    />
    <TextFieldEditor
      textFieldName="Conclusion"
      endpoint="/textfields/conclusion"
      propertyName="content"
    />
  </div>
</template>
