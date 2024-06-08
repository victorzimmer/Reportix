<script setup lang="ts">
import { computed, ref } from 'vue'

const props = defineProps<{
  settingName: string
  endpointReset?: string
  endpointFiles?: string
  endpointDone?: string
  propertyNamePath?: string
  propertyNameContent?: string
  propertyNameFile?: string
}>()

const emit = defineEmits(['update:selection'])

const filesSelected = ref(false)
const filesUploaded = ref(0)
const filesToUpload = ref(0)

async function selectionChanged(event: any) {
  console.log(event)
  if (props.endpointReset) {
    console.log('Resetting selected files for ' + props.settingName + ' at ' + props.endpointReset)
    let response = await fetch(props.endpointReset)
    let loadedContent = await response.json()
  }
  if (props.endpointFiles && props.propertyNameFile) {
    filesUploaded.value = 0
    filesToUpload.value = event.srcElement.files.length - 1
    filesSelected.value = true
    console.log('Uploading files for ' + props.settingName + ' to ' + props.endpointFiles)
    for (let file_id: number = 0; file_id < event.srcElement.files.length; file_id++) {
      console.log(
        'Uploading file' +
          event.srcElement.files[file_id].name +
          ' for ' +
          props.settingName +
          ' to ' +
          props.endpointFiles
      )
      let payload: any = {}
      payload[props.propertyNameFile] = event.srcElement.files[file_id].name
      if (props.propertyNameContent) {
        payload[props.propertyNameContent] = await event.srcElement.files[file_id].text()
      }
      if (props.propertyNamePath) {
        payload[props.propertyNamePath] = event.srcElement.files[file_id].webkitRelativePath
      }
      console.log(payload)
      let response = await fetch(props.endpointFiles, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
      filesUploaded.value = file_id
    }
  }
  if (props.endpointDone) {
    console.log(
      'Done uploading files for ' + props.settingName + ' notifying ' + props.endpointDone
    )
    let response = await fetch(props.endpointDone)
    let loadedContent = await response.json()
  }
}
</script>

<template>
  <span class="label-text">{{ settingName }}</span>
  <input
    type="file"
    class="file-input file-input-sm w-full max-w-xs flex items-center gap-2"
    label="browse"
    webkitdirectory
    directory
    @change="selectionChanged"
  />
  <progress
    v-if="filesSelected"
    class="progress max-w-xs"
    :value="filesUploaded"
    :max="filesToUpload"
  ></progress>
</template>
