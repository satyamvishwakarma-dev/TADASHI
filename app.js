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

const loginBox = document.querySelector('.login-box');

loginBox.addEventListener('mousemove', (e) => {
    // Get the position of the box on the screen
    const rect = loginBox.getBoundingClientRect();
    
    // Calculate exactly where the mouse is inside the box
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    // Send those coordinates to the CSS
    loginBox.style.setProperty('--mouse-x', `${x}px`);
    loginBox.style.setProperty('--mouse-y', `${y}px`);
});

document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault(); 
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, password: password })
        });

        const result = await response.json();
        
        if (result.status === "success") {
            // REDIRECT TO CHAT PAGE HERE
            window.location.href = "chat.html"; 
        } else {
            alert(result.message); // Shows error if wrong
        }
        
    } catch (error) {
        console.error("Error:", error);
    }
});