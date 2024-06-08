<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  settingName: string
  promptOption: string
  selection?: string
  dropdownOptions: string[]
}>()

const emit = defineEmits(['update:selection'])

const internalSelectionValue = computed({
  get(): any {
    return props.selection
  },
  set(newSelection: string): any {
    console.log('Updated selection: ', newSelection)
    return emit('update:selection', newSelection)
  }
})
</script>

<template>
  <span class="label-text w-full">{{ settingName }}</span>
  <select
    class="select select-sm select-bordered w-full max-w-xs flex items-center gap-2"
    v-model="internalSelectionValue"
  >
    <option disabled selected>{{ promptOption }}</option>
    <option v-for="dropdownOption in dropdownOptions">{{ dropdownOption }}</option>
  </select>
</template>
