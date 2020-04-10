if ("{{ login }}" != "") { 
	document.getElementById("login").innerHTML="{{ login }}"; 
	document.getElementById("nav-home").setAttribute("href", "/home/login/{{ login }}");
	document.getElementById("nav-post").setAttribute("href", "/post/login/{{ login }}");
	document.getElementById("nav-find").setAttribute("href", "/find/login/{{ login }}");
	document.getElementById("nav-account").setAttribute("href", "/account/login/{{ login }}");
	document.getElementById("nav-login").setAttribute("href", "/login/login/{{ login }}");
}


