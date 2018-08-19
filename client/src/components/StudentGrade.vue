<template>
	<div class="StudentGrade">
		<center><h1> Notas {{info[0].student}}</h1></center>
      <b-table striped hover :fields="fields" :items="info"></b-table>
    </div>
</template>

<script>
const axios = require('axios');      
export default{
name: 'StudentGrade',
data () {	
	return {		
      fields: [            
            'value',
            'professor',
            'discipline',            
          ],
      info: null,
      id: this.$route.params.id,
	    loading: true,
      errored: false
	}
},
created(){
  console.log("Authorization"  +  "Token " + JSON.parse(this.$cookie.get("user-token")).token)
	axios
	.get("http://localhost:8000/students/"+ this.id + "/grades/", {
      headers: { "content-type": "application/json", "Authorization" :  "Token " + JSON.parse(this.$cookie.get("user-token")).token}}).then(response => {
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
<style>
</style>
