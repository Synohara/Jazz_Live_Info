<template>
  <div>
    <v-card>
      <v-container grid-list-lg>
        <v-layout row wrap>
          <v-flex xs6 v-for="data in lives" :key="data.id">
            <v-card color="primary" class="white--text">
              <v-card-title primary-title>
                <h3 class="headline mb-0">
                  <div>{{ data.artist }}</div>
                </h3>
              </v-card-title>
              <v-card-text>
                <div>{{ data.description }}</div>
              </v-card-text>
              <v-card-text>
                <div>{{ data.ticketAvailableDate|printDate }}</div>
              </v-card-text>
              <v-card-actions>
                <v-btn outline color="gray" :href="data.link" target="_blank">
                  <b>リンク</b>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
          <infinite-loading
            class="infinite-scroll"
            ref="infiniteLoading"
            spinner="circles"
            @infinite="infiniteHandler"
          >
            <div slot="no-results"/>
          </infinite-loading>
        </v-layout>
      </v-container>
    </v-card>
  </div>
</template>


<script>
import axios from "axios";
import moment from "moment";
import InfiniteLoading from "vue-infinite-loading";
import { setTimeout } from "timers";

export default {
  name: "LiveIndex",
  components: {
    InfiniteLoading
  },
  data() {
    return {
      lives: [],
      page: 0
    };
  },
  filters: {
    printDate(val) {
      return moment(val)
        .locale("ja")
        .format("YYYY年MM月DD日(ddd)");
    }
  },
  methods: {
    fetchData() {
      this.$request.lives.list(this.page).then(res => {
        this.lives.push(...res.data.results);
      });
    },
    infiniteHandler() {
      setTimeout(() => {
        this.page++;
        console.log(this.page);
        this.$request.lives.list(this.page).then(res => {
          this.lives.push(...res.data.results);
          this.$refs.infiniteLoading.stateChanger.loaded();
        });
      }, 1000);
    }
  },
  mounted() {
    this.fetchData();
  }
};
</script>

<style>
.infinite-scroll {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 680px;
  margin: 100px 0;
}
</style>