from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Function to get a response from the chatbot
def get_bot_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

# Example usage
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Exiting the chatbot.")
        break
    
    bot_response = get_bot_response(user_input)
    print("Bot:", bot_response)
