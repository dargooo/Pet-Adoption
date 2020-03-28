//fetch('https://jsonplaceholder.typicode.com/todos/1')
//fetch('http://coasttocoast.web.illinois.edu/pet/user/otlak33',{mode: 'no-cors'})
fetch('http://127.0.0.1:5000/pet?species_id=0')
  .then(function(response) {
    return response.text();
  })
  .then(function(text) {
    console.log('Request successful', text);
  })
  .catch(function(error) {
    log('Request failed', error)
  });


/*
fetch('https://jsonplaceholder.typicode.com/todos/1')
.then(res => console.log(res))

fetch('http://127.0.0.1:5000/pet/user/otlak33',{
	"Access-Control-Allow-Origin":"127.0.0.1:5000"
})
.then(res => console.log(res))
*/
