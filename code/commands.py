import os
import json
import random
from collections import Counter

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def createIntent_Answers(UserInputList): 

    random_answers = ["Unfortunately, I cannot offer an adequate answer. Would you please phrase your question differently?", "I'm sorry, but I can't give you a suitable answer. Could you please rephrase your question?", "Unfortunately, I don't have a suitable answer. Please formulate your question differently."]

    with open('KeyPairList.json','r') as file: 
        BiggestCount = 0

        for line in file:
            item = json.loads(line)
            question_no = item['Question']
            keywords_no = item['Keywords']
            keywordcount_no = item['KeywordCount']
            answer_no = item['Answer']

            keywords_no = str(item['Keywords'])

            keywords_no.lower()
            splittedKeywords = keywords_no.split('_')

            counter1 = Counter(splittedKeywords)
            counter2 = Counter(UserInputList)

            HitCount = sum((counter1 & counter2).values())

            if HitCount > BiggestCount:
                BiggestCount = HitCount
                BestAnswer = answer_no

    if BiggestCount <= 0:
        #return[1] == false - Anfrage konnte nicht bearbeitet werden. counter+=1
        return print(random.choice(random_answers)),False

    #return[1] == true - Anfrage konnte bearbeitet werden. counter = 0 (reset)
    return print(BestAnswer),True
