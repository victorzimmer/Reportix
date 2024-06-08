<script setup lang="ts">
defineProps<{
  settingName: string
  promptOption: string
  dropdownOptions: string[]
}>()
</script>

<template>
  <span class="label-text w-full">{{ settingName }}</span>
  <select class="select select-sm select-bordered w-full max-w-xs flex items-center gap-2">
    <option disabled selected>{{ promptOption }}</option>
    <option v-for="dropdownOption in dropdownOptions">{{ dropdownOption }}</option>
  </select>
</template>
