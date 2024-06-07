<script setup lang="ts">
defineProps<{
  settingName: string
}>()
</script>

<template>
  <span class="label-text">{{ settingName }}</span>
  <input
    type="file"
    class="file-input file-input-sm w-full max-w-xs flex items-center gap-2"
    label="browse"
    webkitdirectory
    directory
  />
</template>
