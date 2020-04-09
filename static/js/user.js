function getUser(username) {
	var site = 'http://coasttocoast.web.illinois.edu';

	// user info
	var url = site + '/user?username=\"' + username + '\"';
	console.log(url);
	fetch(url)
	.then(res => res.json())
	.then(data => {
		console.log(data);
		data.forEach(obj => {
			var is_person = obj.is_person;
			if (is_person) { document.getElementById("user-username").innerHTML       = obj.username + ' &#183; individual'; }
			else 		   { document.getElementById("user-username").innerHTML       = obj.username + ' &#183; shelter'; }
			document.getElementById("user-name").innerHTML	= obj.name;
			document.getElementById("user-addr").innerHTML	= obj.address + " " + obj.zipcode;
			document.getElementById("user-email").innerHTML = obj.email;
			//document.getElementById("user-avatar").setAttribute("src", obj.avatar);
		});
	})
    .catch(error => console.log('ERROR'));

	// counts - posted
    var url = site + '/count/pet?username=\"' + username + '\"';
    fetch(url)
        .then(res => {
                return res.json()
        })
        .then(data => {
                console.log(data);
                data.forEach(obj => {
                document.getElementById("user-c-posted").innerHTML=obj.count;
        });
        })
        .catch(error => console.log('ERROR'))

	// counts - adopted
    var url = site + '/count/pet?username=\"' + username + '\"\&status=\'adopted\'';
    fetch(url)
        .then(res => {
                return res.json()
        })
        .then(data => {
                console.log(data);
                data.forEach(obj => {
                document.getElementById("user-c-adopted").innerHTML=obj.count;
        });
        })
        .catch(error => console.log('ERROR'));

	// posted pets list
	var url = site + '/pet/user/' + username;
	console.log(url);
	fetch(url)
    .then(res => res.json())
    .then(data => {
        console.log(data);
        var count = 0;
        data.forEach(obj => {
            console.log(count);
			if (count % 4 == 0) {
                var row = document.createElement("div");
                row.setAttribute("class", "w3-row-padding w3-padding-8 w3-center");
                row.setAttribute("id", "row-" + (count/4 | 0));
				row.setAttribute("style", "margin-top:30px;"); 
                document.getElementById("user-post-container").appendChild(row);
            }

            var div = document.createElement("div");
            div.setAttribute("class", "w3-quarter");

            var img = document.createElement("IMG");
            img.setAttribute("src", obj.image);
            img.setAttribute("alt", "/static/img/nophoto-dog.png");
            img.setAttribute("style", "width:100%;");
            div.appendChild(img);

            var a = document.createElement("a");
            a.setAttribute("href", "http://coasttocoast.web.illinois.edu/present-dog/" + obj.id);
			a.setAttribute("style", "margin:0;");
			var text = obj.name + ' - ' + obj.adopt_status;
			var t = document.createTextNode(text);
            a.appendChild(t);
            div.appendChild(a);
            document.getElementById("row-" + (count/4 | 0)).appendChild(div);
            count++;
        });
    })
    .catch(error => console.log('ERROR'));

}

