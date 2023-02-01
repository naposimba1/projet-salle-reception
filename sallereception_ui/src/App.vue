<template>
  <div id="app">
    <topbar/>
    <div class="view">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Topbar from './components/topbar.vue'

export default {
  name: 'App',
  components: {
    Topbar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

