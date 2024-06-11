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
      endpointGenerating="/currently_generating_textfield_suggestions/"
    />
    <TextFieldEditor
      textFieldName="Methods"
      endpoint="/textfields/methods"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/methods"
      endpointGenerating="/currently_generating_textfield_suggestions/"
    />
    <TextFieldEditor
      textFieldName="Results"
      endpoint="/textfields/results"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/results"
      endpointGenerating="/currently_generating_textfield_suggestions/"
    />
    <TextFieldEditor
      textFieldName="Discussion"
      endpoint="/textfields/discussion"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/discussion"
      endpointGenerating="/currently_generating_textfield_suggestions/"
    />
    <TextFieldEditor
      textFieldName="Conclusion"
      endpoint="/textfields/conclusion"
      propertyName="content"
      endpointSuggestions="/textfield_suggestions/conclusion"
      endpointGenerating="/currently_generating_textfield_suggestions/"
    />
  </div>
</template>
