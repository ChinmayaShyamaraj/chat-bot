import nltk
import rules
from nltk.chat.util import Chat, reflections

def chatbot():
      print("Hello..I am the bot")

chat = Chat(rules.set_pairs, reflections)
chat.converse()
  
      
print("Hello i've changed")
if __name__ == "__main__":
      chatbot()
