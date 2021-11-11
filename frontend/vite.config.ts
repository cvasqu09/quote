import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
const path = require("path");

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  css: {
    preprocessorOptions: {
      scss: { additionalData: `@import "./src/assets/_colors.scss";` },
    },
  },
  resolve: {
    alias: {
      "@quote": path.resolve(__dirname, "./src/quotes"),
      "@utils": path.resolve(__dirname, "./src/utils"),
    },
  },
});
