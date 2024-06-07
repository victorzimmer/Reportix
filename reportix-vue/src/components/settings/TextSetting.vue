<script setup lang="ts">
defineProps<{
  settingName: string
  placeholderText?: string
}>()
</script>

<template>
  <span class="label-text">{{ settingName }}</span>
  <input
    class="input input-sm input-bordered w-full max-w-xs flex items-center gap-2"
    v-bind:placeholder="placeholderText"
  />
</template>
