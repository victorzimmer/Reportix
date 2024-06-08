<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="textFieldComponent pt-10 w-full">
    <h1 class="green">{{ msg }}</h1>
    <textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full " ></textarea>
  </div>
</template>
