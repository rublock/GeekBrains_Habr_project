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
getButtonUrlDataset = document.querySelectorAll('.likeButton')

getButtonUrlDataset.forEach(element => {
    if (element.dataset.like != "") {
        element.addEventListener('click', () => {
            let requestURL = new URL(String(protocolHost + element.dataset.like));
            const xhr = new XMLHttpRequest();
            xhr.open
                ('GET', requestURL, false);
            xhr.status
            xhr.send();
            let likeJson = JSON.parse(xhr.response);
            getLikeSpanButtons = document.querySelectorAll('.likeSpan')
            if (xhr.status === 401) {
                return
            } else if (likeJson.likes != 0) {
                getLikeSpanButtons.forEach(elem => {
                    elem.style.display = "flex";
                    elem.innerHTML = likeJson.likes
                })
            } else if (likeJson.likes === 0) {
                getLikeSpanButtons.forEach(elem => {
                    elem.style.display = "none";
                })
            }
        });
    };
});

const likeButtons = document.querySelectorAll(".likeButtonComment")
likeButtons.forEach(likeButton => {
    const link = likeButton.dataset.like
    if (link != "") {
        likeButton.addEventListener("click", () => {
            const requestURL = new URL(String(protocolHost + link + "?format=json"));
            const xhr = new XMLHttpRequest();
            xhr.open
                ("GET", requestURL, false);
            xhr.send();
            const likeJson = JSON.parse(xhr.response);
            with (likeButton.querySelector(".likeSpanComment")) {
                if (xhr.status === 401) {
                    return
                } else if (likeJson.likes != 0) {
                        style.display = "flex";
                        innerHTML = likeJson.likes;
                } else if (likeJson.likes === 0) {
                    style.display = "none";
                }
            }
        });
    }
});