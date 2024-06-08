<script setup lang="ts">
defineProps<{
  textFieldName: string
}>()
</script>

<template>
  <div class="divider">{{ textFieldName }}</div>
  <div class="textFieldEditor flex flex-row">
    <div class="textFieldInput w-3/5">
      <div class="w-full p-3">
        <textarea
          class="textarea textarea-bordered min-h-32 w-full"
          :placeholder="textFieldName"
        ></textarea>
      </div>
    </div>
    <div class="textFieldSuggestions w-2/5 m-3 min-h-32">
      <div class="grid card bg-base-300 rounded-box place-items-center h-full w-full">
        Suggestions will go here
      </div>
    </div>
  </div>
  <br />
</template>
