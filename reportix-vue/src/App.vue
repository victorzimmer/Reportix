<script setup lang="ts">
import DocumentSettings from './components/DocumentSettings.vue';
</script>

<template>
  <!-- <header>
    <h1 class="text-3xl font-bold underline">Hello world!</h1>
    <button class="btn btn-primary">Button</button>
  </header> -->

  <main>
    <div>
      <div>
        <DocumentSettings/>
        <Editor/>
      </div>
      <div>
        <PDF />
      </div>
    </div>
  </main>

</template>

<!-- 
<style scoped>
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
