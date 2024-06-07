<script setup lang="ts">
import BrowseSetting from './settings/BrowseSetting.vue'
import DropdownSetting from './settings/DropdownSetting.vue'
import TextSetting from './settings/TextSetting.vue'

const availableModels = ['Llama2', 'Llama3']
const availableTemplates = ['Default', 'Formal', 'Weird']
</script>

<template>
  <div class="documentSettings flex flex-row h-fit mb-3">
    <div class="basis-1/2 flex flex-col pl-4 pt-4">
      <div>
        <TextSetting settingName="Author" placeholderText="William Shakespare" />
      </div>
      <div>
        <TextSetting settingName="Date" />
      </div>
    </div>
    <div class="basis-1/2 flex flex-col pt-4">
      <div>
        <DropdownSetting
          settingName="Model"
          promptOption="Select Model"
          :dropdownOptions="availableModels"
        />
      </div>
      <div>
        <BrowseSetting settingName="Code Directory" />
      </div>
      <div>
        <DropdownSetting
          settingName="LaTeX template"
          promptOption="Select Template"
          :dropdownOptions="availableTemplates"
        />
      </div>
    </div>

    <!-- <h1 class="">Document settings</h1>
    <h3>This area will contain settings TEST.</h3> -->
  </div>
</template>
