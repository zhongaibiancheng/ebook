import { fileURLToPath, URL } from "node:url";

import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";
import vuetify, { transformAssetUrls } from "vite-plugin-vuetify";
import AutoImport from "unplugin-auto-import/vite";
import { createHtmlPlugin } from 'vite-plugin-html';
// https://vitejs.dev/config/

export default defineConfig(({ mode }) => {
    // 加载 .env 文件
    const env = loadEnv(mode, process.cwd());
    return {
        server: {
            port: 3000, // 指定开发服务器的端口
            open: true, // 启动时自动在浏览器中打开
        },
        plugins: [
            vue({
                template: { transformAssetUrls }
            }),
            createHtmlPlugin({
                inject: {
                    data: {
                        title: env.VITE_APP_TITLE,
                        apiUrl: env.VITE_API_URL,
                    },
                },
            }),
            vueDevTools(),
            vuetify(),
            AutoImport({
                // https://github.com/unplugin/unplugin-auto-import?tab=readme-ov-file#configuration
                include: [/\.vue$/],
                imports: [{
                    from: "vue",
                    imports: ["ref", "reactive", "computed", "watch", "watchEffect"]
                }],
                dts: "./auto-imports.d.ts"
            })
        ],
        resolve: {
            alias: {
                "@": fileURLToPath(new URL("./src",
                    import.meta.url))
            }
        }
    }
});