authSelector = function(num) {
    if (num == 0) {
        document.getElementById("register").style.display = "none";
        document.getElementById("login").style = "display: block";
    } 
    else if (num == 1) {
        document.getElementById("login").style.display = "none";
        document.getElementById("register").style = "display: block";
        document.getElementById("register-summit").style = "display: none";
    }
    else if (num == 2) {
        document.getElementById("register-first").style.display = "none";
        document.getElementById("register-second").style = "display: block";
        document.getElementById("register-summit").style = "display: block";
    }
    else if (num == 3) {
        document.getElementById("register-first").style.display = "block";
        document.getElementById("register-second").style = "display: none";
        document.getElementById("register-summit").style = "display: none";
    }
}

