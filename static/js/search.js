// DOG
const btnDog = document.getElementById('btn-search-dog');
if (btnDog) {
	setUp(0);
	btnDog.addEventListener('click', function(){ getPet(0); }, false);
}
// CAT
const btnCat = document.getElementById('btn-search-cat');
if (btnCat) {
	setUp(1);
	btnCat.addEventListener('click', function(){ getPet(1); }, false);
}

function setUp(species_id) {
	var site = 'http://coasttocoast.web.illinois.edu';
	// breed list
	var url = site + '/breed?species_id=' + species_id;
	fetch(url)
        .then(res => {
                return res.json()
        })
        .then(data => {
                console.log(data);
                data.forEach(obj => {
			var opt = document.createElement("option");
                        var t = document.createTextNode(obj.name);
                        opt.appendChild(t);
			document.getElementById("breed").appendChild(opt);
		});
        })
        .catch(error => console.log('ERROR'))
}

function getPet(species_id){
	var zipcode 	= document.getElementById("zipcode").value;
	var miles 	= document.getElementById("miles").value;
	var breed 	= document.getElementById("breed").value;
	var gender 	= document.getElementById("gender").value;
	var minAge 	= document.getElementById("minAge").value;
	var maxAge 	= document.getElementById("maxAge").value;
	var color 	= document.getElementById("color").value;
	var hair 	= document.getElementById("hair").value;
	var arr = document.getElementById("personality").selectedOptions;
	personalities = "";
	for (let i=0; i<arr.length; i++) {
		if (i>0) { personalities = personalities + ","; }
		personalities = personalities + "\"" + arr[i].value + "\"";
	}
	//var url = 'http://127.0.0.1:5000/pet?species_id=0';
	var url = 'http://coasttocoast.web.illinois.edu/pet?species_id=' + species_id;
	if (zipcode) { 
		url = url + "\&zipcode=" + zipcode; 
		if (miles) { url = url + "\&miles=" + miles; }
		else 	   { url = url + "\&miles=" + 100; } 
	}
	if (breed) 	 { url = url + "\&breed=" + breed; }
	if (gender) 	 { url = url + "\&gender=" + gender; }
	if (minAge) 	 { url = url + "\&minAge=" + parseInt(minAge); }
	if (maxAge) 	 { url = url + "\&maxAge=" + parseInt(maxAge); }
	if (color) 	 { url = url + "\&color=" + color; }
	if (hair) 	 { url = url + "\&hair=" + hair; }
	if (personalities) { url = url + "\&personality=" + personalities + ""; }
	console.log(url);

	fetch(url)
	.then(res => res.json())
	.then(data => {
		document.getElementById("display-grid").innerHTML = "";
		console.log(data);
		var count = 0;
		data.forEach(obj => {
			console.log(count);
			if (count % 4 == 0) {
				var row = document.createElement("div"); 
				row.setAttribute("class", "w3-row-padding w3-padding-8 w3-center");
				row.setAttribute("id", "row-" + (count/4 | 0));
				document.getElementById("display-grid").appendChild(row);
			}

			var div = document.createElement("div");                       
			div.setAttribute("class", "w3-quarter");

			var img = document.createElement("IMG");  
			img.setAttribute("src", obj.image);
  			img.setAttribute("style", "width:100%");
			div.appendChild(img);                                          

			var a = document.createElement("a");
			a.setAttribute("href", "http://coasttocoast.web.illinois.edu/present-dog/" + obj.id);
			var t = document.createTextNode(obj.name);
			a.appendChild(t);
			a.setAttribute("style", "font-size: 25px; color:rgb(94,94,94);");
			div.appendChild(a);    

			//var p = document.createElement("p");
            //var tt = document.createTextNode(obj.personality);
            //p.appendChild(tt);
            //div.appendChild(p);

			document.getElementById("row-" + (count/4 | 0)).appendChild(div);
			count++;
		});
	})
        .catch(error => console.log('ERROR'))

}

