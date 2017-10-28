function allOn() {
    var theUrl = "http://192.168.0.117/allOn"
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send();
    //return xmlHttp.responseText;

}

function allOff() {
    var theUrl = "http://192.168.0.117/allOff"
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    //return xmlHttp.responseText;
}

function sendMessage() {
    var message = document.getElementById("message").value;
    if (message != ""){
    var theUrl = "http://192.168.0.117/message/" + message
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    document.getElementById("message").value = "";
    return xmlHttp.responseText;
}
}

function blink() {
    var theUrl = "http://192.168.0.117/blink"
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;

}