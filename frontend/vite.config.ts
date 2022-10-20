import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'happy-dom'
  },
  server: {
    host: true,
    strictPort: true,
    proxy: {
      '/api': {
        target: `http://localhost:8000`,
        changeOrigin: true,
      },
    }
  }
})
