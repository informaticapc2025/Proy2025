<template>
   <n-layout has-sider style="height: 100vh; display: flex;">
    <n-layout-sider
      bordered
      width="220"
      content-style="padding: 10px;"
      style="background-color: antiquewhite;"
    >
      <SidebarMenu />
    </n-layout-sider>

    <n-layout>
      <n-layout-header bordered style="padding: 10px;">
        <n-button @click="showModal = true">Abrir Modal</n-button>
        <n-modal v-model:show="showModal">
          <div style="padding: 1em;">¡Hola desde Naive UI!</div>
        </n-modal>
      </n-layout-header>

      <n-layout-content style="padding: 20px;">
        <router-view />
      </n-layout-content>
      
    </n-layout>
  </n-layout>
</template>

<script setup lang="ts">

import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import SidebarMenu from '@/components/layout/SidebarMenu.vue'

const router = useRouter()
const route = useRoute()

const showModal = ref(false)

</script>

<style scoped>
</style>
