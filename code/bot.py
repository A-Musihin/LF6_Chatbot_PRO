from commands import createIntent_Answers
from commands import clear_console
from splash import print_splash
from DatabaseCommands import DBInsertRequest

######################################################################################
# imports #
######################################################################################




clear_console()
print_splash()

user_input_loop = True

user_input = ""

AnswerAttempts = 0

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

    possibleAnswer = createIntent_Answers(user_words)

    if possibleAnswer[1] == True:
        AnswerAttempts = 0

    if possibleAnswer[1] == False:
        #print("AnswerAttempts = ",AnswerAttempts)
        AnswerAttempts += 1

    if AnswerAttempts == 3:
        clear_console()
        print_splash()

        print("The request could not be processed and will be forwarded to the next supervisor.\nPlease contact the first level support or ask another Question.")
        #user_input_loop = False
        AnswerAttempts = 0
        DBInsertRequest(user_input) # Failed request inserted into dbone.request


