<script setup lang="ts">
import { ref, watch } from 'vue'

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

/*
  Title
*/
async function loadTitle() {
  const title_response = await fetch('/settings/title')
  var loadedTitle = await title_response.json()
  console.log('Loaded title: ', loadedTitle, documentTitle)
  documentTitle.value = loadedTitle
}

async function updateTitle() {
  const response = await fetch('/settings/title', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: documentTitle.value })
  })
}

watch(documentTitle, updateTitle)

/*
  Subtitle
*/
async function loadSubtitle() {
  const subtitle_response = await fetch('/settings/subtitle')
  var loadedSubtitle = await subtitle_response.json()
  console.log('Loaded subtitle: ', loadedSubtitle, documentSubtitle)
  documentSubtitle.value = loadedSubtitle
}

async function updateSubtitle() {
  const response = await fetch('/settings/subtitle', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ subtitle: documentSubtitle.value })
  })
}

watch(documentSubtitle, updateSubtitle)

/*
  Author
*/
async function loadAuthor() {
  const author_response = await fetch('/settings/author')
  var loadedAuthor = await author_response.json()
  console.log('Loaded author: ', loadedAuthor, author)
  author.value = loadedAuthor
}

async function updateAuthor() {
  console.log(author.value)
  const response = await fetch('/settings/author', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ author: author.value })
  })
  console.log(response)
  console.log(response.body)
}

watch(author, updateAuthor)

/*
  Date
*/
async function loadDocumentDate() {
  const documentdate_response = await fetch('/settings/date')
  var loadedDocumentDate = await documentdate_response.json()
  console.log('Loaded doucment date: ', loadedDocumentDate, documentDate)
  documentDate.value = loadedDocumentDate
}

async function updateDocumentDate() {
  console.log(documentDate.value)
  const response = await fetch('/settings/date', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ date: documentDate.value })
  })
  console.log(response)
  console.log(response.body)
}

watch(documentDate, updateDocumentDate)

/*
  Model
*/
async function loadModelData() {
  const availableModels_response = await fetch('/settings/available_models')
  var loadedAvailableModels = await availableModels_response.json()
  console.log('Loaded available models: ', loadedAvailableModels)
  availableModels.value = loadedAvailableModels

  const selectedModel_response = await fetch('/settings/selected_model')
  var loadedSelectedModel = await selectedModel_response.json()
  console.log('Loaded selected model: ', loadedSelectedModel)
  selectedModel.value = loadedSelectedModel
}

async function updateSelectedModel() {
  const response = await fetch('/settings/selected_model', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ modelName: selectedModel.value })
  })
}

watch(selectedModel, updateSelectedModel)

/*
  Template
*/
async function loadTemplateData() {
  const availableTemplates_response = await fetch('/settings/available_templates')
  var loadedAvailableTemplates = await availableTemplates_response.json()
  console.log('Loaded available templates: ', loadedAvailableTemplates)
  availableTemplates.value = loadedAvailableTemplates

  const selectedTemplate_response = await fetch('/settings/selected_template')
  var loadedSelectedTemplate = await selectedTemplate_response.json()
  console.log('Loaded selected template: ', loadedSelectedTemplate)
  selectedTemplate.value = loadedSelectedTemplate
}

async function updateSelectedTemplate() {
  const response = await fetch('/settings/selected_template', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ templateName: selectedTemplate.value })
  })
}

watch(selectedTemplate, updateSelectedTemplate)

/*
  Load Settings
*/
const vLoadSettings = {
  beforeMount: (el: any) => {
    console.log('Loading settings from backend...')
    loadTitle()
    loadSubtitle()
    loadAuthor()
    loadDocumentDate()
    loadModelData()
    loadTemplateData()
    // const available_models_response = await fetch('/settings/available_models')
    // var availableModels = await available_models_response.json()
    // console.log(availableModels)
  }
}
</script>

<template>
  <div v-load-settings class="documentSettings flex flex-row h-fit mb-3 mr-3">
    <div class="basis-1/2 flex flex-col pl-4 pt-4">
      <div>
        <TextSetting
          settingName="Title"
          placeholderText="Romeo & Juliet"
          v-model:content="documentTitle"
        />
      </div>
      <div>
        <TextSetting
          settingName="Subtitle"
          placeholderText="A rigorous inquiry of feudes"
          v-model:content="documentSubtitle"
        />
      </div>
      <div>
        <TextSetting
          settingName="Author"
          placeholderText="William Shakespare"
          v-model:content="author"
        />
      </div>
      <div>
        <TextSetting
          settingName="Date"
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
          :dropdownOptions="availableTemplates"
          v-model:selection="selectedTemplate"
        />
      </div>
    </div>
  </div>
</template>
