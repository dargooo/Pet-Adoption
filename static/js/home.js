setUp();

function setUp() {
    //var url = 'http://127.0.0.1:5000/breed?species_id=0';
    var site = 'http://coasttocoast.web.illinois.edu';

    // adoptable pets
    var url = site + '/count/pet?status=\'adoptable\'';
    fetch(url)
        .then(res => {
                return res.json()
        })
        .then(data => {
                console.log(data);
                data.forEach(obj => {
                document.getElementById("count-adoptable").innerHTML=obj.count;
        });
        })
        .catch(error => console.log('ERROR'))

	// adopted pets
    var url = site + '/count/pet?status=\'adopted\'';
    fetch(url)
        .then(res => {
                return res.json()
        })
        .then(data => {
                console.log(data);
                data.forEach(obj => {
                document.getElementById("count-adopted").innerHTML=obj.count;
        });
        })
        .catch(error => console.log('ERROR'))

	// users
    var url = site + '/count/user?is_person=1';
    fetch(url)
        .then(res => {
                return res.json()
        })
        .then(data => {
                console.log(data);
                data.forEach(obj => {
                document.getElementById("count-person").innerHTML=obj.count;
        });
        })
        .catch(error => console.log('ERROR'))

	// shelters
    var url = site + '/count/user?is_person=0';
    fetch(url)
        .then(res => {
                return res.json()
        })
        .then(data => {
                console.log(data);
                data.forEach(obj => {
                document.getElementById("count-shelter").innerHTML=obj.count;
        });
        })
        .catch(error => console.log('ERROR'))

}

if ("{{ login }}" != "") {
    document.getElementById("mid-post").setAttribute("onclick", "window.location.href='/post/login/{{ login }}'");
    document.getElementById("mid-find").setAttribute("onclick", "window.location.href='/find/login/{{ login }}'");
    document.getElementById("mid-find-cat").setAttribute("onclick", "window.location.href='/find-cat/login/{{ login }}'");
    document.getElementById("mid-find-dog").setAttribute("onclick", "window.location.href='/find-dog/login/{{ login }}'");
    document.getElementById("mid-post-cat").setAttribute("onclick", "window.location.href='/post-cat/login/{{ login }}'");
    document.getElementById("mid-post-dog").setAttribute("onclick", "window.location.href='/post-dog/login/{{ login }}'");
}
