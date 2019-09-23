<template>
  <v-toolbar>
    <v-toolbar-title><h2>Jazz Live Informarion</h2></v-toolbar-title>

    <v-spacer></v-spacer>

    <v-form ref="form" lazy-validation>
      <v-text-field
        label="Search"
        prepend-icon="search"
        solo-inverted
        clearable
        clear-icon="mdi-close-circle-outline"
      ></v-text-field>
    </v-form>
  </v-toolbar>
</template>

<script>
export default {
  data: () => ({
    valid: true
  }),
};
</script>