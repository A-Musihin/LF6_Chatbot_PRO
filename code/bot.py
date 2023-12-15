import random
from commands import createIntent_Answers
from commands import clear_console
from splash import print_splash

clear_console()
print_splash()


random_answers = ["Unfortunately, I cannot offer an adequate answer. Would you please phrase your question differently?", "I'm sorry, but I can't give you a suitable answer. Could you please rephrase your question?", "Unfortunately, I don't have a suitable answer. Please formulate your question differently."]
intent_answers = createIntent_Answers()
user_input_loop = True

user_input = ""
while user_input_loop != False:

    user_input = ""
    while user_input == "":
        user_input = input("\nAsk your Question: ")

    user_input = user_input.lower()
    user_words = user_input.split()

    for words in user_words:
        if words in intent_answers:
            print("\n" + intent_answers[words])
            found_match = True
            break
        else:
            #print(random.choice(random_answers))
            found_match = False

        if words == "exit":
            print("Program will be terminated")
            user_input_loop = False
            found_match = True
            
    if not found_match:
        print(random.choice(random_answers))

#print("Einen schönen Tag wünschen wir Ihnen. Bis zum nächsten mal")