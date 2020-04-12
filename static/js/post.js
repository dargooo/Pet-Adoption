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

    /* set up breed list */
function setUp(species_id) {
	var url = 'http://coasttocoast.web.illinois.edu';
    fetch(url + '/breed?species_id=' + species_id)
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

	/* post image */
const handleImageUpload = event => {
  const files = event.target.files;
  const formData = new FormData();
  formData.append('image', files[0]);

//	var url = "http://127.0.0.1:5000"
  var url = 'http://coasttocoast.web.illinois.edu';
  fetch(url + '/image', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    //console.log(data.path)
  })
  .catch(error => {
    console.error(error)
  });
}

document.querySelector('#upload').addEventListener('change', event => {
  handleImageUpload(event)
});







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
