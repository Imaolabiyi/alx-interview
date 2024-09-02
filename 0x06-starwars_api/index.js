const axios = require('axios');

axios.get('https://swapi.dev/api/people/1/')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

