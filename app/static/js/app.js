function removeLoginClass() {
    let elementLogin = document.getElementById("id_username");
    elementLogin.classList.remove("is-invalid");
    let elementPassword = document.getElementById("id_password");
    elementPassword.classList.remove("is-invalid");
}

try {
    removeLoginClass();
} catch (err) {

}

function addClassToRedactor() {
    let element = document.querySelector(".django-ckeditor-widget");
    element.classList.add("container");
}

try {
    addClassToRedactor();
} catch (err) {

}

let form = document.getElementById("commentForm");
let text = document.getElementById("id_text");

document.addEventListener("DOMContentLoaded", (event) => {
    event.preventDefault();
    text.value = ''
});

function myFunctionDropMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function (event) {
    if (!event.target.matches('.btn') && !event.target.matches('.bi-people') && !event.target.matches('.d-print-block')) {
        let dropdowns = document.getElementsByClassName("dropdown-menu");
        let i;
        for (i = 0; i < dropdowns.length; i++) {
            let openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}