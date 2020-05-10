function init() {
    document.getElementById('btn-register').addEventListener('click', register);
	setAvatars();
}

var avaSelected = "";

function selectAva(ava) {
	document.getElementById(ava).setAttribute("style", "border: dashed 3px black");
	if (avaSelected != "") { document.getElementById(avaSelected).setAttribute("style", "border: none"); }
	avaSelected = ava;
}

function register() {
    var name = document.getElementById("name").value;
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var address = document.getElementById("address").value;
    var city = document.getElementById("city").value; 
    var state = document.getElementById("state").value;    
    var zip = document.getElementById("zip").value;
    var type = document.getElementById("type").value;
    var avatar = avaSelected + ".png";

    if (name == "" || username == "" || email == "" || password == "" || address == ""
        || city == "" || state == "" || zip == "" || type == "") {
        return;
    }

    var request = new XMLHttpRequest();
    request.open("GET", '/user?username=\"' + username + '\"', true);
    request.onload = () => {
        console.log("reached here");
        if (request.responseText.length == 3) {
            document.getElementById('register-form').submit();
            var json = {
                name: name,
                username: username,
                email: email,
                password: password,
                address: address + ", " + city + ", " + state,
                zipcode: zip,
                is_person: parseInt(type),
				avatar: avatar
            };
        
            fetch("http://coasttocoast.web.illinois.edu/user", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(json)
            })
            .then(function(response) {
                alert("You are now registered!");
                window.location = "/home/login/" + username;
            }).catch(error => console.log(error));;
        }
        else {
            document.getElementById("message").innerHTML = 'That username is taken, please try another.'
        }
        
    };
    request.send();
}

document.addEventListener('DOMContentLoaded', init);

function setAvatars() {
	var i;
	for (i = 1; i <= 50; i++) {
		 if (i % 5 == 1) {
            var row = document.createElement("div");
		    row.setAttribute("class", "avatar-row");
            row.setAttribute("id", "ava-row-" + ((i-1)/5 | 0));
            document.getElementById("avatar-form").appendChild(row);
		 }
		var img = document.createElement("IMG");
        img.setAttribute("src", "/static/img/avatar/ava" + i + ".png");
		img.setAttribute("class", "avatar");
		img.setAttribute("id", "ava" + i);
		img.setAttribute("onclick", "selectAva(\"ava" + i + "\")");
		document.getElementById("ava-row-" + ((i-1)/5 | 0)).appendChild(img);
	}
}
