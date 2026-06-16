import random

responses = {
    "hello": ["Hi!", "Hello there!", "Hey! How can I help you?"],
    "hi": ["Hi!", "Hello there!", "Hey!"],
    "how are you": ["I'm fine, thanks!", "Doing great, thanks for asking!"],
    "what is your name": ["I'm a simple Python chatbot.", "You can call me PyBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care."],
    "thank you": ["You're welcome!", "No problem!"],
    "thanks": ["You're welcome!", "Anytime!"],
}

default_responses = [
    "Sorry, I didn't understand that.",
    "Can you rephrase that?",
    "I'm not sure how to respond to that."
]


def get_response(user_input):
    user_input = user_input.lower().strip()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(default_responses)


def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    chat()
