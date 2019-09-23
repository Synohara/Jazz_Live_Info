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
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
  white-space: pre-line;
  word-wrap:break-word;
}
</style>