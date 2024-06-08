<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  settingName: string
  // fileList?: any[]
}>()

const emit = defineEmits(['update:selection'])

function selectionChanged() {}

// const internalSelectionValue = computed({
//   get(): any {
//     return props.selection
//   },
//   set(newSelection: string): any {
//     console.log('Updated selection: ', newSelection)
//     return emit('update:selection', newSelection)
//   }
// })
</script>

<template>
  <span class="label-text">{{ settingName }}</span>
  <input
    type="file"
    class="file-input file-input-sm w-full max-w-xs flex items-center gap-2"
    label="browse"
    webkitdirectory
    directory
    v-on:change="selectionChanged"
  />
</template>
