// Listen for the login form to be submitted
document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Stop the page from reloading
    event.preventDefault(); 
    
    // Get the email and password the user typed
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Show it in the browser console to check if it works
    console.log("Login Attempt:", email);
});