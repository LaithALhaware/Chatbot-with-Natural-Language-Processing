import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources
nltk.download('punkt')

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you for asking!', 'I am doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created to help you!']),
    (r'bye|exit', ['Goodbye!', 'See you later!']),
    (r'(.*)', ['Sorry, I didn\'t quite understand that. Could you please rephrase?'])
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Start the chat
def start_chat():
    print("Chatbot: Hi! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit']:
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
