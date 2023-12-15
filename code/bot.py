from commands import createIntent_Answers
from commands import clear_console
from splash import print_splash

clear_console()
print_splash()

user_input_loop = True

user_input = ""
while user_input_loop != False:

    user_input = ""
    while user_input == "":
        user_input = input("\nAsk your Question: ")
        
    user_input = user_input.lower()
    user_words = user_input.split()

    # Quitting software
    for words in user_words:
        if words == "exit":
            print("Program will be terminated")
            user_input_loop = False

    createIntent_Answers(user_words)
