function login() {

	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;

    var site = 'http://coasttocoast.web.illinois.edu';
    // user info
    var url = site + '/user?username=\"' + username + '\"';
    console.log(url);
    fetch(url)
    .then(res => res.json())
    .then(data => {
        console.log(data);
        data.forEach(obj => {
			if (obj.password == password) {
				alert("success!");
			// login success
			}
			else { alert("Username or password wrong !"); }
        });
    })
    .catch(error => console.log('ERROR'));

	alert("Username does not exist !");
}

document.getElementById('btn-login').addEventListener('click', function(){ login(); }, false);



var express = require('express');
var session = require('express-session');
var bodyParser = require('body-parser');
var path = require('path');

var app = express();
app.use(session({
	secret: 'secret',
	resave: true,
	saveUninitialized: true
}));
app.use(bodyParser.urlencoded({extended : true}));
app.use(bodyParser.json());

app.get('/', function(request, response) {
	response.sendFile(path.join(__dirname + '/login.html'));
});

app.post('/auth', function(request, response) {
	var username = request.body.username;
	var password = request.body.password;
	if (username && password) {
		var site = 'http://coasttocoast.web.illinois.edu';
   		 // user info
   		 var url = site + '/user?username=\"' + username + '\"';
   		 console.log(url);
   		 fetch(url)
   		 .then(res => res.json())
   		 .then(data => {
   		     console.log(data);
   		     data.forEach(obj => {
   		         if (obj.password == password) {
					request.session.loggedin = true;
                	request.session.username = username;
                	response.redirect('/home');
   		         // login success
   		         }
   		         else { 
					 response.send('Incorrect Username and/or Password!');
				 }
				 response.end();
   		     });
   		 })
   		 .catch(error => console.log('ERROR'));
		});
	} else {
		response.send('Please enter Username and Password!');
		response.end();
	}
});

app.get('/home', function(request, response) {
	if (request.session.loggedin) {
		response.send('Welcome back, ' + request.session.username + '!');
	} else {
		response.send('Please login to view this page!');
	}
	response.end();
});

app.listen(3000);
