<template>
  <div id="app">     
    <b-nav justified tabs>   
    <b-nav-item><router-link to="/">Home</router-link></b-nav-item>
    <b-nav-item><router-link to="/grades">Notas em Geral</router-link></b-nav-item>
    <b-nav-item><router-link to="/professors">professors</router-link> </b-nav-item>    
    </b-nav>
    <router-view/>
  </div>

</template>

<script>
export default {
  name: 'App'
}
</script>
