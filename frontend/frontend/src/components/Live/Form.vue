<template>
  <v-toolbar dense>
    <v-toolbar-title><h2>Jazz Live Informarion</h2></v-toolbar-title>

    <v-spacer></v-spacer>

    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        v-model="search"
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
    valid: true,
    name: "",
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ],
    email: "",
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false
  }),

  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    }
  }
};
</script>