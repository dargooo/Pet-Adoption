function init() {
    document.getElementById('btn-register').addEventListener('click', register);
}

function login(ev) {
    ev.preventDefault();
    ev.stopPropagation();

	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;

    var site = 'http://coasttocoast.web.illinois.edu';
    var request = new XMLHttpRequest();
    request.open("GET", '/user?username=\"' + username + '\"', true);
    request.onload = () => {
        console.log(request.responseText);
        var json = JSON.parse(request.responseText);

        if (json.password == password) {
            window.location = site + "/home/login/" + username;
        }
        else {
            alert("Username and/or password is wrong!");
        }
    };
}

document.addEventListener('DOMContentLoaded', init);
