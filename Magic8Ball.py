#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
   responses = [
        "Yes, it is",
        "It is certain.",
        "Without a doubt.",
        "You may rely on it.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Don't count on it.",
        "My reply is no.",
        "Very doubtful."
    ]

  question = input("Ask me a question (preferably a yes/no question):  ").strip()
  #Answer question randomly with one of the options from your earlier list.
  answer = random.choice(responses)



  print(f"The Magic 8 Ball says: {answer}")


 
if __name__ == '__main__':
  main()
