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

async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    // Show user message and clear input
    addMessage(text, 'user');
    userInput.value = '';

    // Show typing indicator
    const typingIndicator = document.getElementById('typing-indicator');
    typingIndicator.style.display = 'flex';
    chatBox.appendChild(typingIndicator); // Move it to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });

        const data = await response.json();

        // Hide typing indicator
        typingIndicator.style.display = 'none';

        if (data.reply) {
            addMessage(data.reply, 'bot');
        } else {
            addMessage("Error: Could not get a response.", 'bot');
        }
    } catch (error) {
        typingIndicator.style.display = 'none';
        addMessage("Connection error. Is your Python server running?", 'bot');
    }
}

// Click send or press Enter
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

const newChatBtn = document.querySelector('.new-chat-btn');

newChatBtn.addEventListener('click', async () => {
    try {
        // Tell Python to forget the history
        await fetch('http://127.0.0.1:5000/reset', { method: 'POST' });
        
        // Clear the chat box on the screen and add the default starting message
        chatBox.innerHTML = `
            <div class="message bot">
                <div class="avatar"><i class="fa-solid fa-robot"></i></div>
                <div class="bubble">Hello! How can I assist you today?</div>
            </div>
        `;
    } catch (error) {
        console.error("Error resetting chat:", error);
    }
});