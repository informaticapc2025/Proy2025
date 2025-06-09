<template>
  <div>
    <!-- Solo muestra login -->
    <router-view v-if="esLogin" />

    <!-- Para todas las otras rutas -->
    <n-layout v-else has-sider style="height: 100vh; display: flex">
      <n-layout-sider bordered width="15%" content-style="padding: 10px 20px;">
        <UserCard style="margin-bottom: 20px" />
        <SidebarMenu />
      </n-layout-sider>

      <n-layout has-sider class="base-layout">
        <n-layout-content style="width: 100%; padding: 20px">
          
        </n-layout-content>
      </n-layout>
    </n-layout>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

import SidebarMenu from '@/components/layout/SidebarMenu.vue'
import UserCard from '@/components/layout/UserCard.vue'

const route = useRoute()
const esLogin = computed(() => route.path === '/login')
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
