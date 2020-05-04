function init() {
    document.getElementById('btn-register').addEventListener('click', register);
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
                is_person: parseInt(type)
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
