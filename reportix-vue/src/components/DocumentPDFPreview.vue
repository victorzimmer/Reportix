<script setup lang="ts">
var lastPdfRandId: any = 1

async function reloadPDF() {
  let response = await fetch('/report/compile_randid')
  let loadedRandId = await response.json()

  console.log('RandID: ' + lastPdfRandId)
  console.log('Loaded RandID: ' + loadedRandId)

  if (lastPdfRandId != loadedRandId) {
    lastPdfRandId = loadedRandId
    console.log('Reloading PDF')
    document.getElementById('pdfframe').contentWindow.location.reload()
  }
}

setInterval(reloadPDF, 5000)
</script>

<template>
  <div class="documentPDFPreview">
    <iframe id="pdfframe" class="w-full h-screen" src="/pdf/test.pdf"></iframe>
  </div>
</template>
