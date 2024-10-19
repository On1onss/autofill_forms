from LxmlSoup import LxmlSoup
import requests
import random
import urllib.parse

items_to_be_deleted = ["[", "null", "false", ",", "]", "true", ""]


def html_encode(s):
    return ''.join('&#x{:06x};'.format(ord(c)) for c in s)


def delete_items(string, database):
    statement = string

    for x in range(0, len(database)):

        if items_to_be_deleted[x] in statement:
            statement = statement.replace(items_to_be_deleted[x], "")

    return statement


def get_payload(url):
    try:
        html = requests.get(url).text
        soup = LxmlSoup(html)
        list_items = soup.find_all("div")

        jsmodels = []

        for item in list_items:

            if item.has_attr("data-params"):
                jsmodels.append(item.get("data-params"))

        payload = ""

        for jsmodel in jsmodels:
            word = delete_items(jsmodel, items_to_be_deleted)
            list_number_and_answer = [x for x in word[4::].split('"') if x != ""]
            payload += f"entry.{list_number_and_answer[:-4][2][1::]}={urllib.parse.quote(random.choice(list_number_and_answer[3:-4]))}&"

        return payload
    except ValueError:
        return "Error"