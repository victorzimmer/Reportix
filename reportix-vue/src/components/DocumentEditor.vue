<script setup lang="ts">
import TextFieldEditor from './editor/TextFieldEditor.vue'
</script>

<template>
  <div class="documentEditor">
    <TextFieldEditor
      textFieldName="Introduction"
      endpoint="/textfields/introduction"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/introduction"
    />
    <TextFieldEditor
      textFieldName="Methods"
      endpoint="/textfields/methods"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/methods"
    />
    <TextFieldEditor
      textFieldName="Results"
      endpoint="/textfields/results"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/results"
    />
    <TextFieldEditor
      textFieldName="Discussion"
      endpoint="/textfields/discussion"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/discussion"
    />
    <TextFieldEditor
      textFieldName="Conclusion"
      endpoint="/textfields/conclusion"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/conclusion"
    />
  </div>
</template>
