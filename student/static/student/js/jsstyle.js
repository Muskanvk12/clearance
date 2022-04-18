var main = document.getElementById("main");
var hr = document.getElementsByTagName("header");
var icon = document.getElementById("icon");
var about = document.getElementById("about");

function hovr(){
    document.getElementById("header").className = "hovered";
   icon.style.display = "flex";
   about.style.display = "flex"
    
}

document.getElementById("header").onmouseover = hovr;
