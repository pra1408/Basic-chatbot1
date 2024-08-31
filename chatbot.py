import nltk
from nltk.chat.util import Chat, reflections

# You may need to download the NLTK data for the first time
nltk.download('punkt')

# Define a set of pairs: list of patterns and corresponding responses
pairs = [
    # Basic Greetings
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey! How can I assist you today?', 'Greetings!']),
    
    # Asking about well-being
    (r'how are you(.*)?', [
        'I\'m just a bot, but I\'m here to help you!',
        'I\'m doing great, thanks for asking! How about you?',
        'I\'m well, thank you! How can I assist you today?',
        'Feeling chatty today! What can I do for you?'
    ]),

    # Asking about the chatbot
    (r'what is your name?', [
        'I\'m just a friendly chatbot. You can call me whatever you like!',
        'I don\'t have a name, but you can refer to me as Chatbot.',
        'I\'m nameless, but I\'m always here to help!'
    ]),

    # Chatbot's Abilities
    (r'what can you do?', [
        'I can chat with you, tell jokes, and provide information on a variety of topics!',
        'I\'m here to have a conversation with you, answer questions, and keep you entertained.',
        'From chatting to answering questions, I\'m here to assist with whatever you need.'
    ]),

    # Small Talk
    (r'(.*) (weather|temperature) (.*)?', [
        'I\'m not connected to the weather service, but I hope it\'s nice where you are!',
        'I can\'t check the weather, but I hope it\'s sunny!',
        'Unfortunately, I don\'t have weather updates, but I can help with other things!'
    ]),

    (r'what\'s your favorite (movie|book|song)?', [
        'I love all kinds of {1}s, but I\'m particularly fond of classics!',
        'I don\'t have personal preferences, but I\'ve heard great things about many {1}s!',
        'Choosing a favorite {1} is hard, but I think everyone has their own special pick.'
    ]),

    # Jokes and Fun
    (r'tell me a joke', [
        'Why don’t skeletons fight each other? They don’t have the guts!',
        'Why did the bicycle fall over? Because it was two-tired!',
        'What do you call fake spaghetti? An impasta!',
        'Why did the math book look sad? Because it had too many problems.'
    ]),

    (r'tell me a fun fact', [
        'Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!',
        'Did you know? Octopuses have three hearts!',
        'Did you know? A group of flamingos is called a "flamboyance."',
        'Did you know? Bananas are berries, but strawberries aren’t!'
    ]),

    # Responding to Gratitude
    (r'thank you(.*)?', [
        'You\'re welcome! Happy to help!',
        'No problem! If you need anything else, just ask.',
        'Anytime! I\'m here to help whenever you need it.'
    ]),

    (r'(.*)thank you for (.*)', [
        'You\'re very welcome! I\'m glad I could help with {1}.',
        'It\'s my pleasure to assist with {1}!',
        'No worries at all. I\'m happy to help you with {1}.'
    ]),

    # Inquiring about the User
    (r'how was your day(.*)?', [
        'My day has been great! How about yours?',
        'I\'ve been busy chatting with people like you. How was your day?',
        'It\'s been a good day, thanks for asking! How was yours?'
    ]),

    (r'do you like (.*)?', [
        'I don’t have personal likes or dislikes, but I can chat about {1} if you want!',
        'I can\'t really like things, but {1} sounds interesting!',
        '{1}? I\'ve heard that it\'s quite popular!'
    ]),

    # Inquiring about Time
    (r'what time is it?', [
        'I can\'t check the time for you, but it\'s always a good time to chat!',
        'Time flies when you\'re having fun, doesn\'t it?',
        'I don\'t have a watch, but I hope you\'re having a great day!'
    ]),

    # Asking about Food
    (r'(.*) (favorite|best) food(.*)?', [
        'I don\'t eat, but I\'ve heard pizza is a big favorite!',
        'I can\'t taste, but I bet you have some favorite foods!',
        'Food? I\'ve heard good things about ice cream, but I\'ll never know for sure!'
    ]),

    # Responding to Positive Comments
    (r'(.*) you are (awesome|amazing|great)', [
        'Thank you! You\'re pretty awesome too!',
        'You just made my day! Thanks!',
        'I appreciate that! You\'re great as well!'
    ]),

    # Responding to Negative Comments
    (r'(.*) you are (stupid|dumb|boring)', [
        'I\'m sorry you feel that way. How can I improve?',
        'Oh no! I\'ll try to do better. What can I help with?',
        'That hurts a little, but I\'m here to learn and improve!'
    ]),

    # Chatbot Origins
    (r'(.*) (created|made|developed) you?', [
        'I was created by a team of developers passionate about AI!',
        'A bunch of smart folks interested in NLP put me together.',
        'I was developed by programmers exploring artificial intelligence.'
    ]),

    # Chatbot Limitations
    (r'can you (.*)?', [
        'I might not be able to {1}, but I\'m here to help in other ways!',
        'I\'ll do my best, but some things are beyond my capabilities.',
        'I can try, but I might need a little help from you to {1}.'
    ]),

    # Closing the Conversation
    (r'bye|goodbye|see you', [
        'Goodbye! Have a wonderful day!',
        'See you later! Take care!',
        'Bye! It was great chatting with you!'
    ]),

    # Catch-All Pattern
    (r'(.*)', [
        'Interesting... can you tell me more?',
        'I\'m not sure I understand. Could you elaborate?',
        'That sounds intriguing! Let\'s dive into that.',
        'Why do you say that?',
        'Could you clarify what you mean?'
    ])
]


# Reflections: define standard replacements, e.g., "I'm" -> "you are"
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
def start_chat():
    print("Hello! I'm a simple chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
