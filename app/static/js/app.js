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

let protocolHost = window.location.protocol + '//' + window.location.host
getButtonUrlDataset = document.querySelector('.likeButton').dataset.like

if (getButtonUrlDataset != "") {
    document.querySelector('.likeButton').addEventListener('click', () => {
        let requestURL = new URL(String(protocolHost + getButtonUrlDataset + '?format=json'));
        const xhr = new XMLHttpRequest();
        xhr.open
            ('GET', requestURL, false);
        xhr.send();
        let likeJson = JSON.parse(xhr.response);
        if (xhr.status === 401) {
        return
        } else if (likeJson.likes != 0) {
            document.querySelector(".likeSpan").style.display = "flex";
            document.querySelector('.likeSpan').innerHTML = likeJson.likes
        } else if (likeJson.likes === 0) {
            document.querySelector(".likeSpan").style.display = "none";
        }
    });
    document.querySelector('.likeButtonDown').addEventListener('click', () => {
        let requestURL = new URL(String(protocolHost + getButtonUrlDataset + '?format=json'));
        const xhr = new XMLHttpRequest();
        xhr.open
            ('GET', requestURL, false);
        xhr.send();
        let likeJson = JSON.parse(xhr.response);
        if (xhr.status === 401) {
        return
        } else if (likeJson.likes != 0) {
            document.querySelector(".likeSpanDown").style.display = "flex";
            document.querySelector('.likeSpanDown').innerHTML = likeJson.likes
        } else if (likeJson.likes === 0) {
            document.querySelector(".likeSpanDown").style.display = "none";
        }
    });
}