function getPet(pet_id) {
	var site = 'http://coasttocoast.web.illinois.edu';

	// from pet
	var url = site + '/pet?id=' + pet_id + '\&species_id=0';
	console.log(url);
	fetch(url)
	.then(res => res.json())
	.then(data => {
		console.log(data);
		data.forEach(obj => {
			document.getElementById("present-name").innerHTML		 = obj.name;
			document.getElementById("present-breed").innerHTML		 = obj.breed;
			document.getElementById("present-gender").innerHTML		 = obj.gender;
			document.getElementById("present-age").innerHTML		 = obj.age;
			document.getElementById("present-color").innerHTML		 = obj.color;
			document.getElementById("present-hair").innerHTML		 = obj.hair;
			document.getElementById("present-weight").innerHTML 	 = obj.weight;
			document.getElementById("present-personality").innerHTML = obj.personality;
            if (obj.image == null) { document.getElementById("present-img").setAttribute("src", "/static/img/nophoto-dog.png"); }
            else                   { document.getElementById("present-img").setAttribute("src", obj.image); }
		});
	})
        .catch(error => console.log('ERROR'));

	// from posts
	url = site + '/posts?pet_id=' + pet_id;
	fetch(url)
    .then(res => res.json())
    .then(data => {
        console.log(data);
        data.forEach(obj => {
            document.getElementById("present-title").innerHTML       = obj.title;
            document.getElementById("present-description").innerHTML = obj.description;
            document.getElementById("present-postby").innerHTML      = obj.username;
			document.getElementById("present-postby").setAttribute("href", "http://coasttocoast.web.illinois.edu/userpage/" + obj.username);
            document.getElementById("present-posttime").innerHTML    = obj.open_time;
        });
    })

}

