//feilds
let email = document.querySelector(".email");
let password = document.querySelector(".password");
let repassword = document.querySelector(".password-two");
let btn = document.querySelector(".sign-up");
let error = document.querySelectorAll("h6");

//error feilds
let emailError = document.querySelector(".email-error");
let passOneError = document.querySelector(".pass-error");
let passTwoError = document.querySelector(".pass-two-error");

//Eye icons
let eyeOne = document.querySelector(".eye-one");
let eyeTwo = document.querySelector(".eye-two");
let eyes = document.querySelectorAll(".fa-eye");

//Show/hide password on eyes clicks
eyeOne.addEventListener("click" ,function() {
    if (password.type === "password") {
        eyeOne.classList.remove("fa-eye-slash");
        eyeOne.classList.add("fa-eye");
        eyeOne.style.opacity = .7;
        password.type = "text"
    }
    else {
        eyeOne.classList.remove("fa-eye")
        eyeOne.classList.add("fa-eye-slash");
        password.type = "password";
        eyeOne.style.opacity = .3;
    }
})
eyeTwo.addEventListener("click" ,function() {
    if (repassword.type === "password") {
        eyeTwo.classList.remove("fa-eye-slash");
        eyeTwo.classList.add("fa-eye");
        eyeTwo.style.opacity = .7;
        repassword.type = "text"
    }
    else {
        eyeTwo.classList.add("fa-eye-slash");
        eyeTwo.classList.remove("fa-eye");
        eyeTwo.style.opacity = .3;
        repassword.type = "password";
    }
})


//Sign up button on click (Inputs Validation)
let succed = false;
let info = []
if (localStorage.getItem("users")) {
    info = JSON.parse(localStorage.getItem("users"));
}

btn.addEventListener("click" , () => {
    error.forEach(e => {
        e.innerHTML = "";
    })
    //inputs validtaion
    if (email.value === "") {
        emailError.innerHTML = "Email feild can't be empty!";
    }
    else if (password.value === "") {
        passOneError.innerHTML = "Password feild can't be empty!";
    }
    else if (password.value.length < 10) {
        passOneError.innerHTML = "Password is too short!";
    }
    else if (repassword.value === "") {
        passTwoError.innerHTML = "Please confirm your password!";
    }
    else if (repassword.value !== password.value) {
        passTwoError.innerHTML = "Passwords are Different. Please confirm your password correctly!";
    }
    else {
        passTwoError.innerHTML = "You have created a new account successfully";
        passTwoError.style.fontSize = "17px";
        passTwoError.style.color = "#12c349";
        passTwoError.style.padding = "20px 0 0 20px";
        succed = true;
        if (succed === true) {
            const userData = {
                user:email.value + " " + password.value
                
            }
            setTimeout(() => {
                location.href = "index.html"
            }, 1500);
            info.push(userData);
            window.localStorage.setItem("users" , JSON.stringify(info));
        }
    } 
    });
