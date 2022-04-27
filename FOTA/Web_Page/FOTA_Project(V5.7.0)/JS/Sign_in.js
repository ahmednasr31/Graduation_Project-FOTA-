//Eye icons
let eyeOne = document.querySelector(".eye-one");

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

//Validation
let email = document.querySelector(".email");
let password = document.querySelector(".password");
let btn = document.querySelector(".log-in");
let error = document.querySelector(".error");

// //empty array

let info = [];
if (localStorage.getItem("users")) {
    info = JSON.parse(localStorage.getItem("users"));
}

btn.addEventListener("click" , () => {
    error.innerHTML = "Email or Password is not Correct , Please try again!"
    for(let i = 0; i < info.length; i++) {
        if (info[i].user === email.value + " " + password.value) {
            {
                error.style.color = "#12c349";
                error.style.fontSize = "18px";
                error.style.paddingLeft = "100px";
                setTimeout(() => {
                    location.href = "Upload.html"
                }, 1500);
                return error.innerHTML = "Login Successful";
                
            }
        }
    }
});

