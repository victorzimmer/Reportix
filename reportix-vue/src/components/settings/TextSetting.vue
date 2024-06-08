<script setup lang="ts">
import { computed, watch } from 'vue'

const props = defineProps<{
  settingName: string
  content?: string
  endpoint?: string
  propertyName?: string
  placeholderText?: string
}>()

const emit = defineEmits(['update:content'])

const internalContentValue = computed({
  get(): any {
    return props.content
  },
  set(newContent: string): any {
    return emit('update:content', newContent)
  }
})

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
  Load Settings
*/
const vLoadContent = {
  beforeMount: (el: any) => {
    loadContent()
  }
}
</script>

<template>
  <span class="label-text">{{ settingName }}</span>
  <input
    v-load-content
    class="input input-sm input-bordered w-full max-w-xs flex items-center gap-2"
    type="text"
    :placeholder="placeholderText"
    v-model="internalContentValue"
  />
</template>
