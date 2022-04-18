var btn = document.getElementById("icon-button");
var nav = document.getElementById("nav-menu");

function changeClass() {
            nav.className = "visible";
}
function changeClassBack() {
            nav.className = "hidden";
}
    btn.addEventListener('click', changeClass, false);
    btn.addEventListener('blur', changeClassBack, false);