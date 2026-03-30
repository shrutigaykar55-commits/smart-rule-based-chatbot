import re
import datetime

knowledge_base = {
    "python": "Python is a high-level programming language used for AI, web, and automation.",
    "ai": "Artificial Intelligence enables machines to mimic human intelligence.",
    "chatbot": "A chatbot is a software that can simulate conversation with users.",
    "machine learning": "Machine Learning is a subset of AI that learns from data."
}

patterns = {
    "greeting": r"\b(hi|hello|hey)\b",
    "help": r"\b(help|assist|support)\b",
    "smalltalk": r"\b(how are you|what's up)\b",
    "exit": r"\b(exit|bye|quit)\b"
}

responses = {
    "greeting": "Hello! 👋 How can I help you?",
    "help": "I can answer questions about Python, AI, and chatbots.",
    "smalltalk": "I'm just a bot, but I'm doing great! 😊",
    "unknown": "Sorry, I don't understand that."
}

log_file = open("chat_log.txt", "a", encoding="utf-8")

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def log_conversation(user, bot):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"[{timestamp}] You: {user}\n")
    log_file.write(f"[{timestamp}] Bot: {bot}\n\n")

def chatbot_response(user_input):
    user_input = user_input.lower()
    for intent, pattern in patterns.items():
        if re.search(pattern, user_input):
            if intent == "exit":
                return "Goodbye! 👋", True
            return responses[intent], False
    for key in knowledge_base:
        if key in user_input:
            return knowledge_base[key], False
    return responses["unknown"], False

print("🤖 Smart Chatbot Started (type 'exit' to quit)\n")

while True:
    user_input = input(f"[{get_time()}] You: ")
    response, exit_flag = chatbot_response(user_input)
    print(f"[{get_time()}] Bot: {response}")
    log_conversation(user_input, response)
    if exit_flag:
        break

log_file.close()
