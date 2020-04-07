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
			document.getElementById("user-username").innerHTML	 = obj.username;
			document.getElementById("user-name").innerHTML		 = obj.name;
			document.getElementById("user-addr").innerHTML		 = obj.address + " " + obj.zipcode;
			document.getElementById("user-email").innerHTML		 = obj.email;
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

            var div = document.createElement("div");
            div.setAttribute("class", "w3-quarter");

            var img = document.createElement("IMG");
            img.setAttribute("src", obj.image);
            img.setAttribute("alt", "Sandwich");
            img.setAttribute("style", "width:100%;");
            if (count > 4) {  img.setAttribute("style", "margin-top:30px;"); }
            div.appendChild(img);

            var a = document.createElement("a");
            a.setAttribute("href", "http://coasttocoast.web.illinois.edu/present-dog/" + obj.id);
			a.setAttribute("style", "margin:0;");
            var t = document.createTextNode(obj.name + ' &#183; ' + obj.status);
            a.appendChild(t);
            div.appendChild(a);

            document.getElementById("user-post-container").appendChild(div);
            count++;
        });
    })
    .catch(error => console.log('ERROR'));

}

