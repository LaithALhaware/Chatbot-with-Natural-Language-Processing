import nltk
import gradio as gr
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

# Define the function to get the chatbot response
def respond_to_input(user_input):
    return chatbot.respond(user_input)

# Create the Gradio interface
iface = gr.Interface(fn=respond_to_input, 
                     inputs="text", 
                     outputs="text", 
                     title="Chatbot", 
                     description="This is a simple chatbot interface built with Gradio.")

# Launch the interface on the web
if __name__ == "__main__":
    iface.launch()
