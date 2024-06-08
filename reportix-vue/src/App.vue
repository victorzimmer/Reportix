<script setup lang="ts">
import DocumentSettings from './components/DocumentSettings.vue'
import DocumentEditor from './components/DocumentEditor.vue'
import DocumentPDFPreview from './components/DocumentPDFPreview.vue'
</script>

<template>
  <div id="mainUI" class="h-screen w-screen flex flex-row">
    <div class="basis-3/5 flex flex-col">
      <div class="basis-1/3 bg-gray-100">
        <DocumentSettings />
      </div>
      <div class="basis-2/3 bg-gray-50 overflow-scroll max-h-full">
        <DocumentEditor />
      </div>
    </div>
    <div class="basis-2/5 bg-black">
      <DocumentPDFPreview />
    </div>
  </div>
</template>
