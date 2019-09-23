<template>
  <div>
    <v-footer height="auto">
      <v-card class="flex" flat tile raised>
        <v-card-title class="justify-center blue-grey lighten-2">
          <strong class="subheading"></strong>

          <v-spacer></v-spacer>

          <v-btn v-for="icon in icons" :key="icon" class="mx-3" dark icon>
            <v-icon size="24px">{{ icon }}</v-icon>
          </v-btn>
        </v-card-title>

        <v-card-actions class="blue-grey darken-1 justify-center">
          &copy;2019 —
          <strong>Jazz Live情報</strong>
        </v-card-actions>
      </v-card>
    </v-footer>
  </div>
</template>

<script>
export default {
  data: () => ({
    icons: [
      "fab fa-twitter",
      "fab fa-github"
    ]
  })
};
</script>