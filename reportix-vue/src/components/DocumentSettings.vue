<script setup lang="ts">
import { ref } from 'vue'

import BrowseSetting from './settings/BrowseSetting.vue'
import DropdownSetting from './settings/DropdownSetting.vue'
import TextSetting from './settings/TextSetting.vue'

const documentTitle = ref('')
const documentSubtitle = ref('')
const author = ref('')
const documentDate = ref('')
const availableModels = ref(['TestModel 1', 'TestModel 2'])
const selectedModel = ref('')
const availableTemplates = ref(['TestTemplate 1', 'TestTemplate 2'])
const selectedTemplate = ref('')

defineExpose({
  author,
  documentDate,
  documentTitle,
  documentSubtitle,
  availableModels,
  selectedModel,
  availableTemplates,
  selectedTemplate
})
</script>

<template>
  <div v-load-settings class="documentSettings flex flex-row h-fit mb-3 mr-3">
    <div class="basis-1/2 flex flex-col pl-4 pt-4">
      <div>
        <TextSetting
          settingName="Title"
          placeholderText="Romeo & Juliet"
          endpoint="/settings/title"
          propertyName="title"
          v-model:content="documentTitle"
        />
      </div>
      <div>
        <TextSetting
          settingName="Subtitle"
          placeholderText="A rigorous inquiry of feudes"
          endpoint="/settings/subtitle"
          propertyName="subtitle"
          v-model:content="documentSubtitle"
        />
      </div>
      <div>
        <TextSetting
          settingName="Author"
          placeholderText="William Shakespare"
          endpoint="/settings/author"
          propertyName="author"
          v-model:content="author"
        />
      </div>
      <div>
        <TextSetting
          settingName="Date"
          endpoint="/settings/date"
          propertyName="date"
          v-model:content="documentDate"
          placeholderText="Spring 1597"
        />
      </div>
    </div>
    <div class="basis-1/2 flex flex-col pt-4">
      <div>
        <DropdownSetting
          settingName="Model"
          promptOption="Select Model"
          endpointOptions="/settings/available_models"
          endpointSelected="/settings/selected_model"
          propertyName="modelName"
          :dropdownOptions="availableModels"
          v-model:selection="selectedModel"
        />
      </div>
      <div>
        <BrowseSetting settingName="Code Directory" />
      </div>
      <div>
        <DropdownSetting
          settingName="LaTeX template"
          promptOption="Select Template"
          endpointOptions="/settings/available_templates"
          endpointSelected="/settings/selected_template"
          propertyName="templateName"
          :dropdownOptions="availableTemplates"
          v-model:selection="selectedTemplate"
        />
      </div>
    </div>
  </div>
</template>
