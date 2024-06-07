<script setup lang="ts">
import DocumentSettings from './components/DocumentSettings.vue'
import DocumentEditor from './components/DocumentEditor.vue'
import DocumentPDFPreview from './components/DocumentPDFPreview.vue'
// import HelloWorld from './components/HelloWorld.vue'
// import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <div id="mainUI" class="h-screen w-screen flex flex-row">
    <div class="basis-3/5 flex flex-col">
      <div class="basis-1/3 bg-red-100">
        <DocumentSettings />
      </div>
      <div class="basis-2/3 bg-blue-100 overflow-scroll max-h-full">
        <DocumentEditor />
      </div>
    </div>
    <div class="basis-2/5 bg-green-100">
      <DocumentPDFPreview />
    </div>
  </div>

  <!-- <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
    <h1 class="text-3xl font-bold underline">Hello world!</h1>
    <button class="btn btn-primary">Button</button>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main> -->
</template>

<!-- <style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style> -->
