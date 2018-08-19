<template>
  <div id="app">     
    <b-nav justified tabs>   
    <b-btn v-b-modal.modalLogin>login</b-btn>
    <b-nav-item><router-link to="/">Home</router-link></b-nav-item>
    <b-nav-item><router-link to="/grades">Notas em Geral</router-link></b-nav-item>
    <b-nav-item><router-link to="/professors">professors</router-link> </b-nav-item>    
    <b-btn v-b-modal.modalStudent>cadastrar aluno</b-btn>
    </b-nav>
        

    <!-- Modal Component -->
    <b-modal id="modalStudent"
             ref="modal"
             title="Student"
             @ok="createStudent">
      <form @submit.stop.prevent="handleSubmit">
        <b-form-input type="text"
                      placeholder="Enter your name"
                      v-model="newStudent.name"></b-form-input>
        <b-form-input type="text"
                      placeholder="Enter your username"
                      v-model="newStudent.username"></b-form-input>                      
        <b-form-input type="text"
                      placeholder="Enter your email"
                      v-model="newStudent.email"></b-form-input>  
        <b-form-input type="text"
                      placeholder="Enter your password"
                      v-model="newStudent.password"></b-form-input>                      
      </form>
    </b-modal>
    <!-- Modal Component -->
    <b-modal id="modalLogin"
             ref="modal"
             title="Student"
             @ok="login">
      <form @submit.stop.prevent="handleSubmit">
        <b-form-input type="text"
                      placeholder="Enter your username"
                      v-model="user.username"></b-form-input>
        <b-form-input type="text"
                      placeholder="Enter your password"
                      v-model="user.password"></b-form-input>                              
      </form>
    </b-modal>
    <router-view/>
  </div>

</template>

<script>
const axios = require('axios'); 
export default {
  name: 'App',
  data () { 
    return {    
        user: {'username':null,'password':null},
        newStudent: {'firstname': null, 'username': null,'email':null, 'password': null},
        loading: true,
        errored: false
    }
  },  
  methods: {
  createStudent() {
  this.loading = true;
  axios
  .post('http://localhost:8000/students/',this.newStudent, {headers: { "content-type": "application/json", "Authorization" : "Token " + JSON.parse(this.$cookie.get("user-token")).token}})
      .then((response) => {        
        this.loading = false;        
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
        if(error.response.status == '401'){
          this.redirectToLogin();
        }
      })
  },
  login() {
    axios
        .post('http://localhost:8000/api/token/', this.user, {
          headers: { "content-type": "application/json" }
        })
        .then(
          result => {
            this.response = result.data;
            const token = this.response;
            this.$cookie.set("user-token", JSON.stringify(token), 1);
            console.log(JSON.parse(this.$cookie.get("user-token")).token);
           
          },
          error => {
            console.error(error);
            this.$cookie.delete("user-token");
          }
        );
  }
}
}
</script>
