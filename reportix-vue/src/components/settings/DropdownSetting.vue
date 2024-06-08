<script setup lang="ts">
import { computed, ref, watch } from 'vue'

const props = defineProps<{
  settingName: string
  promptOption: string
  selection?: string
  endpointOptions?: string
  endpointSelected?: string
  propertyName?: string
  dropdownOptions: string[]
}>()

const emit = defineEmits(['update:selection'])

var internalOptionsValue = ref(props.dropdownOptions)

var internalSelectionValue = ref(props.selection)
const internalSelectionValueDynamic = computed({
  get(): any {
    return internalSelectionValue.value
  },
  set(newSelection: string): any {
    internalSelectionValue.value = newSelection
    console.log('Selected new value for ' + props.settingName + ': ' + newSelection)
    return emit('update:selection', newSelection)
  }
})

async function loadContent() {
  console.log(props)
  if (props.endpointOptions) {
    console.log('Fetching options for ' + props.settingName + ' from ' + props.endpointOptions)
    let response = await fetch(props.endpointOptions)
    let loadedContent = await response.json()
    internalOptionsValue.value = loadedContent
  }
  if (props.endpointSelected) {
    let response = await fetch(props.endpointSelected)
    let loadedContent = await response.json()
    internalSelectionValue.value = loadedContent
  }
}

async function updateSelection() {
  if (props.endpointSelected && props.propertyName) {
    var payload: any = {}
    payload[props.propertyName] = internalSelectionValue.value
    const response = await fetch(props.endpointSelected, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
  }
}

watch(internalSelectionValue, updateSelection)

/*
  Load Settings
*/
const vLoadContent = {
  beforeMount: (el: any) => {
    loadContent()
  }
}
</script>

<template>
  <span class="label-text w-full">{{ settingName }}</span>
  <select
    v-load-content
    class="select select-sm select-bordered w-full max-w-xs flex items-center gap-2"
    v-model="internalSelectionValue"
  >
    <option disabled selected>{{ promptOption }}</option>
    <option v-for="dropdownOption in internalOptionsValue">{{ dropdownOption }}</option>
  </select>
</template>
