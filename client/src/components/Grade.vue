<template>
  <div class="Grade">
    
    <b-table striped hover :fields="fields" :items="info"></b-table>

  </div>
</template>

<script>
const axios = require('axios'); 
export default{
name: 'Grade',
data () { 
  return {    
    fields: [            
      'value',
      'professor',
      'discipline',                 
      'student'
    ],
    info: null
  }
},
mounted () {
  axios
    .get('http://localhost/grades/')
    .then(response => {
      this.loading = false
      console.log(response.data)
      this.info = response.data.results
    })
    .catch(error => {
      console.log(error)
      this.errored = true
    })
    .finally(() => this.loading = false)
  }
}

</script>

