<template>
  <body>
    <n-layout has-sider style="height: 100vh; display: flex">
      <n-layout-sider bordered width="15%" content-style="padding: 10px 20px;">
        <UserCard style="margin-bottom: 20px" />
        <SidebarMenu />
        <ButtonAction style="margin-top: 20px" label="Realizar queja" />
      </n-layout-sider>

      <n-layout has-sider class="base-layout">
        <n-layout-content style="width: 70%; padding: 20px">
          <router-view />
        </n-layout-content>

        <n-layout-sider style="width: 30%; padding: 20px">
          <n-image width="100%" :src="logo" />
          <CelebrationCard />
          <n-layout-header bordered style="padding: 10px">
            <n-button @click="showModal = true">Abrir Modal</n-button>
            <n-modal v-model:show="showModal">
              <div style="padding: 1em">¡Hola desde Naive UI!</div>
            </n-modal>
          </n-layout-header>
        </n-layout-sider>
      </n-layout>
    </n-layout>
  </body>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'

import logo from '@/assets/OGBU-logo.png'
import SidebarMenu from '@/components/layout/SidebarMenu.vue'
import CelebrationCard from '@/components/layout/CelebrationCard.vue'
import UserCard from './components/layout/UserCard.vue'
import ButtonAction from './components/layout/ButtonAction.vue'

const showModal = ref(false)
</script>

<style scoped>
.base-layout {
  min-height: 100vh;
  background: url('../src/assets/background.jpg');
}
.base-layout::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: rgba(255, 255, 255, 0.8);
  z-index: 1;
}
.base-layout > * {
  position: relative;
  z-index: 2;
}
</style>
