// JAVASCRIPT verify if its good


// SIGN UP 
function sign_up(){
    // The namee is gathered from the sign up section 
    namee = document.getElementById('name').value;
    // Email variable is gathered from the sign up section 
    email = document.getElementById('email').value;
    // Password variable is gathered from the sign up section 
    password = document.getElementById('password').value;

    // Verification that it worked 
    alert(namee);
    alert(email);
    alert(password);
    
    
}
// LOGIN
function log_in(){
    // LOG IN

    // The 'email' variable grabs data the user uses from the Log In section 
    email = document.getElementById('log_in_email').value; 
    // The 'password' variable grabs the data the user put in the password section in the log in section 
    password = document.getElementById('log_in_password').value;
   
    // Verification that it worked 
    alert(email);
    alert(password); 
}

// Sign-In info! 