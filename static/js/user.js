

 /* post review */
function postReview(reviewee) {
    var reviewer  = "sb1";
    var content   = document.getElementById("user-review-content").value;
    var recommand = document.getElementById("togBtn").value;

    var json = {
		"reviewer": reviewer,
		"reviewee": reviewee,
		"content": content,
		"recommand": recommand
    }

//  var url = "http://127.0.0.1:5000"
    var url = 'http://coasttocoast.web.illinois.edu';
    fetch(url + "/reviews", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(json)
      }).then(function(response) {
          console.log(JSON.stringify(json));
          return response.json();
      }) .then(data => {
          //console.log(data);
          //var obj = JSON.parse(data);
       }).catch(error => console.log('ERROR'));

}

