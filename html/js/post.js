// DOG
const btnDog = document.getElementById('btn-post-dog');
if (btnDog) {
    setUp(0);
    btnDog.addEventListener('click', function(){ postPet(0); }, false);
}
// CAT
const btnCat = document.getElementById('btn-post-cat');
if (btnCat) {
    setUp(1);
    btnCat.addEventListener('click', function(){ postPet(1); }, false);
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
            document.getElementById("post-breed").appendChild(opt);
        });
        })
        .catch(error => console.log('ERROR'))
}


function postPet(species_id) {

    var name     	= document.getElementById("post-name").value;
    var breed   	= document.getElementById("post-breed").value;
    var gender  	= document.getElementById("post-gender").value;
    var age  		= document.getElementById("post-age").value;
    var color   	= document.getElementById("post-color").value;
    var hair    	= document.getElementById("post-hair").value;
    var weight   	= document.getElementById("post-weight").value;
    var personality = document.getElementById("post-personality").value;
    var title	 	= document.getElementById("post-title").value;
    var description = document.getElementById("post-description").value;
    var image   	= document.getElementById("post-image").src;

	//alert(name+breed+gender+age+color+hair+weight+personality+image);

//	var url = 'http://coasttocoast.web.illinois.edu';
	var url = 'http://127.0.0.1:5000';

	var json = {
		"name": 	    name,
		"breed":     	breed,
    	"gender":       gender,
    	"age":          age,
    	"color":        color,
    	"hair":         hair,
    	"weight":       weight,
    	"personality":  personality,
		"username":		"ywang14",
		"title":		title,
		"description":  description,
	}

	  fetch(url + "/pet", {
	    method: 'POST',
		headers: { 'Content-Type': 'application/json' },
	    body: JSON.stringify(json)
	  }).then(function(response) {
		  console.log(JSON.stringify(json));
	      return response.json();
	  }).then(function(data) {
	      //console.log('Created Gist:', data.html_url);
	  });


	fetch(url + "/image", {
        method: 'POST',
        headers: { 'Content-Type':'multipart/form-data' },
        body: { image }
    })
        .then((response) => response.json())
        .then((data)=>{
            this.setState({images: data.images, isLoading: false});
            this.props.updateImages(data.images);
        })
        .catch(error => this.setState({ error, isLoading: false}));

}






//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#post-image')
                .attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$(function () {
    $('#upload').on('change', function () {
        readURL(input);
    });
});

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById( 'upload' );
var infoArea = document.getElementById( 'upload-label' );

input.addEventListener( 'change', showFileName );
function showFileName( event ) {
  var input = event.srcElement;
  var fileName = input.files[0].name;
  infoArea.textContent = 'File name: ' + fileName;
}
