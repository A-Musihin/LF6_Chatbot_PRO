import random
from commands import createIntent_Answers
from commands import clear_console

clear_console()

random_answers = ["Interessant ...", "Ich verstehe ...", "Leider habe ich darauf keine passende Antwort."]
intent_answers = createIntent_Answers()
user_input_loop = True

user_input = ""
while user_input_loop != False:

    user_input = ""
    while user_input == "":
        user_input = input("Ihre Frage/Antwort: ")

    user_input = user_input.lower()
    user_words = user_input.split()

    for words in user_words:
        if words in intent_answers:
            print(intent_answers[words])
            found_match = True
            break
        else:
            #print(random.choice(random_answers))
            found_match = False

        if words == "bye":
            print("Programm wird beendet.")
            user_input_loop = False
            found_match = True
            
    if not found_match:
        print(random.choice(random_answers))

#print("Einen schönen Tag wünschen wir Ihnen. Bis zum nächsten mal")