from LxmlSoup import LxmlSoup
import requests
import random
import ast


def get_questions(url):
    try:
        request = requests.get(url)

        if request.status_code != 200:
            return "Error"

        html = request.text
        soup = LxmlSoup(html)
        list_items = soup.find_all("div")

        questions = []

        for item in list_items:
            idx = 0
            if item.has_attr("data-params"):
                for _ in item.get("data-params"):
                    if _ == "[":
                        break
                    idx += 1

                questions.append(ast.literal_eval("[" + item.get("data-params")[idx:].
                                                  replace("null,", "").
                                                  replace("false,", "").
                                                  replace("true,", "").
                                                  replace("false", "").
                                                  replace("true", "")))

        return questions

    except:
        return "Error"


def get_random_payload(questions):
    payload = ''
    try:
        for question in questions:
            answers = question[0][3][0][1]
            payload += f"entry.{question[0][3][0][0]}={random.choice(answers)[0]}&"

        return payload
    except:
        return "Error"


# Test function
def interactive(questions):

    print(f"Form contain {len(questions)} questions")
    payload = ''

    for number, question in enumerate(questions):
        answers = question[0][3][0][1]
        print(f"Question {number + 1}: {question[0][1]}")
        answer_idx = 0
        for idx, answer in enumerate(answers):
            print(f"\tAnswer {idx + 1}: {answer[0]}")

        while True:
            try:
                choice = int(input("Enter number of choice:"))

                if choice > len(answers) or choice <= 0:
                    print("The number is higher or lower than it should be")
                    continue

                answer_idx = choice
                break
            except:
                print("Error. Enter NUMBER if choice")
                continue

        payload += f"entry.{question[0][3][0][0]}={answers[answer_idx - 1][0]}&"

    return payload
