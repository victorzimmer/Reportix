<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  settingName: string
  content?: string
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
</script>

<template>
  <span class="label-text">{{ settingName }}</span>
  <input
    class="input input-sm input-bordered w-full max-w-xs flex items-center gap-2"
    type="text"
    :placeholder="placeholderText"
    v-model="internalContentValue"
  />
</template>
