from LxmlSoup import LxmlSoup
import requests
import random
import ast


# Maybe deleted?
def html_encode(s):
    return ''.join('&#x{:06x};'.format(ord(c)) for c in s)


def get_questions(url):
    try:
        html = requests.get(url).text
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
                                                  replace("true,", "")))

        return questions

    except ValueError:
        return "Error"


def get_random_payload(url):
    questions = get_questions(url)
    payload = ''

    for question in questions:
        answers = question[0][3][0][1]
        payload += f"entry.{question[0][0]}={random.choice(answers)[0]}&"

    return payload


# Test function
def interactive():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSeDdCIF3K4gHhJx3iTyGjjqkWf0_n_Avh9F_a01vkrRF8yVMQ/viewform"

    questions = get_questions(url)
    text = get_questions(url)[0]
    text1 = get_questions(url)[1]

    print(f"Form contain {len(questions)} questions")

    for number, question in enumerate(questions):
        answers = question[0][3][0][1]
        print(f"Question {number + 1}: {question[0][1]}")
        for idx, answer in enumerate(answers):
            print(f"\tAnswer {idx + 1}: {answer[0]}")

    question = text[0][1]
    answers = text[0][3][0][1]
    print("Question:", question)
    for i, answer in enumerate(answers):
        print(i + 1, answer[0])
    print(text1[0][3][0][1])

    print(get_random_payload(url))
