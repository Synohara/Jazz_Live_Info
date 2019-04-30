<template>
  <v-app id="app">
    <router-view name="form"></router-view>
    <v-content>
      <v-container fluid>
        <router-view name="index"></router-view>
      </v-container>
    </v-content>
    <router-view name="footer"></router-view>
  </v-app>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
</style>