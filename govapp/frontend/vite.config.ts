import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'happy-dom'
  },
  build: {
	outDir: "../static/webapp",
	emptyOutDir: true,
	manifest: false,
	sourcemap: false,
        rollupOptions: {
          output: {
            entryFileNames: `assets/[name].js`,
            chunkFileNames: `assets/[name].js`,
            assetFileNames: `assets/[name].[ext]`
          }
        }

 	//rollupOptions: {
	//     chunkFileNames: "../static/webapp/[name].js",
	//     assetFileNames: "../static/webapp/[name].[ext]",
	//     cache: false,
	//},

  },
  server: {
    host: true,
    port: 9072,
    strictPort: true,
    proxy: {
      '/api': {
        target: `http://localhost:9071`,
        changeOrigin: true,
      },
     }
  }
  
  //rollupOptions: { 
  //   input: '/js/app.js',	  
  //   chunkFileNames: "[name].js"
  //} 
})

