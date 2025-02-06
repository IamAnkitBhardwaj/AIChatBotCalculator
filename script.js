const chatbox = document.getElementById('chatbox');
const userInput = document.getElementById('userInput');

function sendMessage() {
  const input = userInput.value.trim();
  if (!input) return;

  // Append user message
  appendMessage(input, 'user-message');

  // Send request to the Flask server
  fetch('http://127.0.0.1:5000/calculate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ input }),
  })
    .then((response) => response.json())
    .then((data) => {
      const reply = data.result || data.error || 'Sorry, I didn\'t understand that.';
      appendMessage(reply, 'chatbot-message');
    })
    .catch((error) => {
      appendMessage('Error connecting to server.', 'chatbot-message');
    });

  userInput.value = '';
}

function appendMessage(message, className) {
  const messageElement = document.createElement('div');
  messageElement.classList.add(className);
  messageElement.innerHTML = `<p>${message}</p>`;
  chatbox.appendChild(messageElement);
  chatbox.scrollTop = chatbox.scrollHeight;
}

function fillInput(operation) {
  userInput.value = operation;
}



// Handle Instruction Chatbot
const instructionChatbox = document.getElementById('instruction-chatbox');
const instructionInput = document.getElementById('instructionInput');

function sendInstructionMessage() {
  const input = instructionInput.value.trim();
  if (!input) return;

  // Append user message
  appendInstructionMessage(input, 'user-message');

  // Send request to Flask server for instruction chatbot
  fetch('http://127.0.0.1:5000/instructions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ input }),
  })
    .then((response) => response.json())
    .then((data) => {
      const reply = data.result || data.error || 'Sorry, I didn\'t understand that.';
      appendInstructionMessage(reply, 'chatbot-message');
    })
    .catch((error) => {
      appendInstructionMessage('Error connecting to server.', 'chatbot-message');
    });

  instructionInput.value = '';
}

function appendInstructionMessage(message, className) {
  const messageElement = document.createElement('div');
  messageElement.classList.add(className);
  messageElement.innerHTML = `<p>${message}</p>`;
  instructionChatbox.appendChild(messageElement);
  instructionChatbox.scrollTop = instructionChatbox.scrollHeight;
}


// Handle messages for the currency converter chatbot
function convertCurrency() {
  const data = {
      from_currency: document.getElementById("fromCurrency").value,
      to_currency: document.getElementById("toCurrency").value,
      amount: parseFloat(document.getElementById("amount").value)
  };

  fetch("http://127.0.0.1:5001/convert_currency", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
  })
      .then(response => response.json())
      .then(result => {
          if (result.error) {
              alert(`Error: ${result.error}`);
          } else {
              alert(`Converted Amount: ${result.converted_amount} ${result.to_currency}`);
          }
      })
      .catch(error => {
          console.error("Error:", error);
          alert("An error occurred. Check the console for details.");
      });
}

function toggleMenu() {
  const navLinks = document.getElementById("navLinks");
  navLinks.classList.toggle("active");
}