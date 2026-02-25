const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Function to add a message bubble to the screen
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    
    let avatarHTML = sender === 'bot' ? `<div class="avatar"><i class="fa-solid fa-robot"></i></div>` : '';
    
    messageDiv.innerHTML = `
        ${avatarHTML}
        <div class="bubble">${text}</div>
    `;
    
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
}

// Handle sending message
async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    // 1. Show user message
    addMessage(text, 'user');
    userInput.value = '';

    try {
        // 2. Send to Python backend
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });

        const data = await response.json();

        // 3. Show Bot response
        if (data.reply) {
            addMessage(data.reply, 'bot');
        } else {
            addMessage("Error: Could not get a response.", 'bot');
        }
    } catch (error) {
        addMessage("Connection error. Is your Python server running?", 'bot');
    }
}

// Click send or press Enter
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});