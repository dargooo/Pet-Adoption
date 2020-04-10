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
				window.location = url + "/home/" + username;
			}
			else { alert("Username or password wrong !"); }
        });
    })
    .catch(error => console.log('ERROR'));

	alert("Username does not exist !");
}

document.getElementById('btn-login').addEventListener('click', function(){ login(); }, false);


