import json

# Lese die JSON-Datei ein
with open('data.json', 'r') as file:
    for line in file:
        item = json.loads(line)
        key_no = item['KeyNo']
        answer_no = item['AnswerNo']
        print(f"Key: {key_no}, Answer: {answer_no}")


