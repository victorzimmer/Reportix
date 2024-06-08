<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{
  textFieldName: string
  endpoint?: string
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

watch(internalContentValue, updateContent)

/*
  Load content
*/
const vLoadContent = {
  beforeMount: (el: any) => {
    loadContent()
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
      <div class="grid card bg-base-300 rounded-box place-items-center h-full w-full">
        Suggestions will go here
      </div>
    </div>
  </div>
  <br />
</template>
