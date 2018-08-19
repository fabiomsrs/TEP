<template>
<div id="app">	
		
		<section v-if="errored">
		<p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
		</section>
		<section v-else>
		<div v-if="loading">Loading...</div>

		<b-table striped hover :fields="fields" :items="info"></b-table>

		</section>
	</div>		
</template>
<script>		
		const axios = require('axios');				
		export default {
		  name: 'Professor',
		  data: () => ({
		  	  fields: [            
	            'name',	            
	          ],
		      info: null,
		      loading: true,
		      errored: false
		    }),	    
		  mounted () {
		    axios
		      .get('http://localhost:8000/professors/')
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