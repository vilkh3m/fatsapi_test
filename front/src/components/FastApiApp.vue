<template>
    <div>
      <h1>FastAPI Vue App</h1>
      <input v-model="number" type="number" placeholder="Enter a number" />
      <button @click="fetchNumber">Get Number</button>
      <p v-if="numberResponse">Response: {{ numberResponse }}</p>
  
      <button @click="fetchDatetime">Get Current Datetime</button>
      <p v-if="datetimeResponse">Datetime: {{ datetimeResponse }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        number: '',
        numberResponse: null,
        datetimeResponse: null
      };
    },
    methods: {
      async fetchNumber() {
        try {
          const response = await axios.get(`http://localhost:8000/number/${this.number}`);
          this.numberResponse = response.data.number;
        } catch (error) {
          console.error("Error fetching number:", error);
        }
      },
      async fetchDatetime() {
        try {
          const response = await axios.get("http://localhost:8000/datetime");
          this.datetimeResponse = response.data.datetime;
        } catch (error) {
          console.error("Error fetching datetime:", error);
        }
      }
    }
  };
  </script>
  
  <style>
  button {
    margin: 10px;
    padding: 5px 10px;
    cursor: pointer;
  }
  </style>
  