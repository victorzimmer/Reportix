<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{
  textFieldName: string
  endpoint?: string
  endpointSuggestions?: string
  endpointGenerating?: string
  propertyName?: string
}>()

const internalContentValue = ref('')

async function loadContent() {
  if (props.endpoint) {
    const response = await fetch(props.endpoint)
    var loadedContent = await response.json()
    internalContentValue.value = loadedContent
  }
}

async function updateContent() {
  if (props.endpoint && props.propertyName) {
    var payload: any = {}
    payload[props.propertyName] = internalContentValue.value
    const response = await fetch(props.endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
  }
}

var contentTimer

async function resetUpdateContentTimer() {
  clearTimeout(contentTimer)
  contentTimer = setTimeout(updateContent, 2000)
}

watch(internalContentValue, resetUpdateContentTimer)

const internalSuggestionsValue = ref(['Suggestions not loaded'])

async function loadSuggestions() {
  if (props.endpointSuggestions) {
    console.log('Loading suggestions for ' + props.textFieldName)
    const response = await fetch(props.endpointSuggestions)
    var loadedContent = await response.json()
    internalSuggestionsValue.value = loadedContent
  }
}

const isGenerating = ref(false)

async function checkIfGenerating() {
  if (props.endpointGenerating) {
    const response = await fetch(props.endpointGenerating)
    var loadedContent = await response.json()
    console.log('Checked: ' + loadedContent)
    let prevValue = isGenerating.value
    isGenerating.value = loadedContent == props.textFieldName.toLowerCase()

    if (prevValue != isGenerating.value) {
      loadSuggestions()
    }
  }
}

/*
  Load content
*/
const vLoadContent = {
  beforeMount: (el: any) => {
    loadContent()
    loadSuggestions()
    setInterval(loadSuggestions, 5000)
    setInterval(checkIfGenerating, 500)
  }
}
</script>

<template>
  <div class="divider">{{ textFieldName }}</div>
  <div class="textFieldEditor flex flex-row">
    <div class="textFieldInput w-3/5">
      <div class="w-full p-3">
        <textarea
          v-load-content
          class="textarea textarea-bordered min-h-32 w-full"
          :placeholder="textFieldName"
          v-model="internalContentValue"
        ></textarea>
      </div>
    </div>
    <div class="textFieldSuggestions w-2/5 m-3 min-h-32">
      <div class="card bg-base-300 rounded-box place-items-start p-3 h-full w-full table">
        <span v-if="isGenerating" class="loading loading-spinner text-secondary"></span>
        <div v-if="!isGenerating" class="overflow-y-scroll h-full">
          <ul class="list-disc">
            <li v-for="suggestion in internalSuggestionsValue">{{ suggestion }}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <br />
</template>
