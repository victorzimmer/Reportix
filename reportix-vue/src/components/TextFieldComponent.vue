<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="textFieldComponent overflow-y-scroll">
    <h1 class="green">{{ msg }}</h1>
    <h3>This is {{ msg }} text field</h3>
    <textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full max-w-xs" ></textarea>
  </div>
</template>
