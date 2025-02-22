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


def get_text_answers(question):
    answers = question[0][3][0][1]

    if len(answers) == 0:
        answers = [["Your answer"]]

    return answers


# Choice, DropDown, Liner, Rating, CheckBox
def get_choice_answers(question):
    answers = question[0][3][0][1]
    return answers


# Refactor to choice
def get_dropdown_answers(question):
    answers = question[0][3][0][1]
    return answers


# Refactor to choice
def get_checkbox_answers(question):
    answers = question[0][3][0][1]
    return answers


# Refactor to choice
def get_liner_answers(question):
    answers = question[0][3][0][1]
    return answers


def get_grid_answers(question):
    columns = question[0][3][0][1]
    raws = [raw[2] for raw in question[0][3]]

    return [raws, columns]


def get_date_answers(question):
    answers = question[0][3][0][1]

    if len(answers) == 0:
        answers = [["Your answer format: dd.mm.yyyy"]]

    return answers


def get_time_answers(question):
    answers = question[0][3][0][1]

    if len(answers) == 0:
        answers = [["Your answer format hour:minute"]]

    return answers


# Refactor to choice
def get_rating_answers(question):
    answers = question[0][3][0][1]
    return answers


def get_answers(question):
    type_of_question = question[0][2]

    if type_of_question == 0 or type_of_question == 1:
        answers = get_text_answers(question)
    elif type_of_question == 2:
        answers = get_choice_answers(question)
    elif type_of_question == 3:
        answers = get_dropdown_answers(question)
    elif type_of_question == 4:
        answers = get_checkbox_answers(question)
    elif type_of_question == 5:
        answers = get_liner_answers(question)
    elif type_of_question == 7:
        answers = get_grid_answers(question)
    elif type_of_question == 9:
        answers = get_date_answers(question)
    elif type_of_question == 10:
        answers = get_time_answers(question)
    elif type_of_question == 18:
        answers = get_rating_answers(question)
    else:
        return f"Error", type_of_question

    return answers, type_of_question


def get_random_payload(questions):
    payload = ''
    try:
        for question in questions:
            answers = question[0][3][0][1]
            payload += f"entry.{question[0][3][0][0]}={random.choice(answers)[0]}&"

        return payload
    except:
        return "Error"


# TODO: Make different conclusions for different types
def interactive(questions):

    print(f"Form contain {len(questions)} questions")
    payload = ''

    for number, question in enumerate(questions):

        answers, type_of_question = get_answers(question)

        if answers == "Error":
            print(f"{answers}. Type {type_of_question} not supported. Question: \"{question}\"")
            continue

        print(f"Question {number + 1}: \"{question[0][1]}\"")

        answer_idx = 0
        text_answer = ''

        if type_of_question == 7:
            for id_raw, raw in enumerate(answers[0]):
                print(f"\tRaw: \"{raw[0]}\"")
                for id_column, column in enumerate(answers[1]):
                    print(f"\t\tAnswer {id_column + 1}: \"{column[0]}\"")

                while True:
                    try:
                        choice = int(input("\tEnter number of choice: "))

                        if choice > len(answers) or choice <= 0:
                            print("The number is higher or lower than it should be")
                            continue

                        answer_idx = choice
                        break
                    except:
                        print("Error. Enter NUMBER of choice")
                        continue
                payload += f"entry.{question[0][3][id_raw][0]}={answers[1][answer_idx - 1][0]}&"
        else:
            for idx, answer in enumerate(answers):
                print(f"\tAnswer {idx + 1}: \"{answer[0]}\"")

            while True:
                if type_of_question == 0 or type_of_question == 1:
                    try:
                        text_answer = input("Enter text: ")
                        if len(text_answer) == 0:
                            print("Text is empty")
                            continue

                        break
                    except:
                        print("Error")
                        continue
                if type_of_question == 4:
                    try:
                        choice = input("Enter the number of your choice separated by space: ")
                        try:
                            choice = [int(x) for x in choice.split()]
                        except:
                            print("One or more choice is not number. Or invalid input choice")
                            continue

                        if max(choice) > len(answers) or min(choice) <= 0:
                            print("The number is higher or lower than it should be")
                            continue

                        answer_idx = choice
                        break
                    except:
                        print("Error. Enter NUMBER of choice")
                        continue
                elif type_of_question == 9:
                    try:
                        choice = input("Enter date: ").split(".")
                        # # Check date
                        # ...
                        answer_idx = choice
                        break
                    except:
                        print("Error. Enter DATE")
                        continue
                elif type_of_question == 10:
                    try:
                        choice = input("Enter time: ").split(":")
                        # # Check time
                        # ...
                        answer_idx = choice
                        break
                    except:
                        print("Error. Enter TIME")
                        continue
                else:
                    try:
                        choice = int(input("Enter number of choice: "))

                        if choice > len(answers) or choice <= 0:
                            print("The number is higher or lower than it should be")
                            continue

                        answer_idx = choice
                        break
                    except:
                        print("Error. Enter NUMBER of choice")
                        continue

            if type_of_question == 0 or type_of_question == 1:
                payload += f"entry.{question[0][3][0][0]}={text_answer}&"
            elif type_of_question == 4:
                for idx in answer_idx:
                    payload += f"entry.{question[0][3][0][0]}={answers[idx - 1][0]}&"
            elif type_of_question == 9:
                payload += f"entry.{question[0][3][0][0]}_year={answer_idx[2]}&"
                payload += f"entry.{question[0][3][0][0]}_month={answer_idx[1]}&"
                payload += f"entry.{question[0][3][0][0]}_day={answer_idx[0]}&"
            elif type_of_question == 10:
                payload += f"entry.{question[0][3][0][0]}_hour={answer_idx[0]}&"
                payload += f"entry.{question[0][3][0][0]}_minute={answer_idx[1]}&"
            else:
                payload += f"entry.{question[0][3][0][0]}={answers[answer_idx - 1][0]}&"

    return payload
