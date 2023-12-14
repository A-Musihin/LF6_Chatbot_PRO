import os
import json

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def createIntent_Answers():

    with open('data.json','r') as file:
        data = [json.loads(line) for line in file]

    intent_answers = {item['KeyNo']: item['AnswerNo'] for item in data}

    return intent_answers
