function removeLoginClass() {
    let elementLogin = document.getElementById("id_username");
    elementLogin.classList.remove("is-invalid");
    let elementPassword = document.getElementById("id_password");
    elementPassword.classList.remove("is-invalid");
}

removeLoginClass();
