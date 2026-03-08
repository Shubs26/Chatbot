const chatWindow = document.getElementById("chatWindow");
const chatForm = document.getElementById("chatForm");
const userMessageInput = document.getElementById("userMessage");
const ownerNameInput = document.getElementById("ownerName");
const productFocusInput = document.getElementById("productFocus");
const saveProfileButton = document.getElementById("saveProfile");

const profile = {
  ownerName: "there",
  productName: "Ecogram GG",
  productFocus: "product overview"
};

function addMessage(sender, content) {
  const bubble = document.createElement("article");
  bubble.className = `message ${sender}`;
  bubble.textContent = content;
  chatWindow.appendChild(bubble);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function buildReply(message) {
  const text = message.toLowerCase();

  if (text.includes("hello") || text.includes("hi")) {
    return `Hi ${profile.ownerName}! I'm your Ecogram GG assistant. I can help with FAQs, feature highlights, onboarding flow, and support replies.`;
  }

  if (text.includes("feature") || text.includes("what can")) {
    return "Core ideas for Ecogram GG: smart onboarding, friendly product guidance, and instant answers for common customer questions.";
  }

  if (text.includes("pricing")) {
    return "For pricing questions, I suggest sharing value-first messaging: problem solved, expected outcomes, then plan options.";
  }

  if (text.includes("focus") || text.includes("strategy")) {
    return `Current focus for your chatbot is: ${profile.productFocus}. I can tailor responses around that angle.`;
  }

  if (text.includes("help")) {
    return "Try asking: 'How should I pitch Ecogram GG?', 'Give me onboarding copy', or 'Create a support reply template'.";
  }

  return `Great question. For Ecogram GG, I'd answer in a concise, helpful tone and connect it to ${profile.productFocus}. Want me to draft a customer-ready response?`;
}

function saveProfile() {
  const ownerName = ownerNameInput.value.trim();
  const productFocus = productFocusInput.value.trim();

  if (ownerName) {
    profile.ownerName = ownerName;
  }

  if (productFocus) {
    profile.productFocus = productFocus;
  }

  addMessage(
    "bot",
    `Profile updated. I'll address you as ${profile.ownerName} and prioritize ${profile.productFocus} for Ecogram GG.`
  );
}

saveProfileButton.addEventListener("click", saveProfile);

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const message = userMessageInput.value.trim();
  if (!message) {
    return;
  }

  addMessage("user", message);
  const reply = buildReply(message);

  setTimeout(() => {
    addMessage("bot", reply);
  }, 250);

  userMessageInput.value = "";
  userMessageInput.focus();
});

addMessage(
  "bot",
  "Welcome! I'm the Ecogram GG personal chatbot template. Save your profile, then ask me product, onboarding, pricing, or support questions."
);
