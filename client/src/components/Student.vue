<template>
<div id="app">  
    
    <section v-if="errored">
    <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
    </section>
    <section v-else>
    <div v-if="loading">Loading...</div>

    <b-table striped hover :fields="fields" :items="info">
      <template slot="notas" slot-scope="data">
      <a :href="data.value">notas</a>
      </template>
    </b-table>


    </section>
  </div>    
</template>
<script>       
    const axios = require('axios');       
    export default {
      name: 'Student',
      data: () => ({ 
          fields: [            
            'name',
            'notas'
          ],       
          info: [],
          loading: true,
          errored: false
        }),     
      mounted () {
        axios
          .get('http://localhost/students/')
          .then(response => {            
            this.loading = false
            console.log(response.data.results)            
            for(var i = 0; i<response.data.results.length; i++){              
              this.info.push({'name':response.data.results[i].name, 'notas':"http://localhost:8080/student/"+response.data.results[i].pk+"/grades"})
            }            
            console.log(this.info)
          })
          .catch(error => {
            console.log(error)
            this.errored = true
          })
          .finally(() => this.loading = false)
      }
    }
</script>