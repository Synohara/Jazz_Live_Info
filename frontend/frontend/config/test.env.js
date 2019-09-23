"use strict";
const merge = require("webpack-merge");
const devEnv = require("./dev.env");

export default merge(devEnv, {
  NODE_ENV: '"testing"'
});
