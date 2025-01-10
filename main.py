
def chatbot(user_input):
    response = generate_response(user_input)
    return response

def generate_response(message):
    # Basic responses for demonstration
    if 'hello' in message.lower():
        return 'Hello! How can I help you today?'
    elif 'bye' in message.lower():
        return 'Goodbye! Have a great day!'
    else:
        return 'I am not sure how to respond to that.'

if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot(user_input)
        print("Bot:", response)