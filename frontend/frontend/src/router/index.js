import Vue from "vue";
import Router from "vue-router";
import LiveIndex from "@/components/Live/Index";
import LiveFooter from "@/components/Live/Footer";
import LiveForm from "@/components/Live/Form"
Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "LiveIndex",
      components: {
        index: LiveIndex,
        footer: LiveFooter,
        form: LiveForm
      }
    }
  ]
});
