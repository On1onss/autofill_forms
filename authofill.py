import requests
from GetPayload import get_random_payload
from authofill_forms.GetPayload import interactive, get_questions

banner = r'''             _    _   _______   _    _    ____    ______   _____   _        _      
     /\     | |  | | |__   __| | |  | |  / __ \  |  ____| |_   _| | |      | |     
    /  \    | |  | |    | |    | |__| | | |  | | | |__      | |   | |      | |     
   / /\ \   | |  | |    | |    |  __  | | |  | | |  __|     | |   | |      | |     
  / ____ \  | |__| |    | |    | |  | | | |__| | | |       _| |_  | |____  | |____ 
 /_/    \_\  \____/     |_|    |_|  |_|  \____/  |_|      |_____| |______| |______|
                                                                                   
                                                                      made by Bb0LP'''

print(banner)

while True:
    choice = input("Choose interactive or random mode? (R, I): ")

    if choice == "R" or choice == "I" or choice == "r" or choice == "i":
        break

    print(f"Select R or I. NOT \"{choice}\"..")

while True:
    url = input("Enter url: ")
    if "forms" in url and (url.startswith("http://") or url.startswith("https://")):
        questions = get_questions(url)
        if questions == "Error":
            print("Error. Invalid url.")
            continue
        break

    print("This is not a url")

while True:
    try:
        number = int(input("Enter the number of iterations: "))
        if number <= 0:
            print("The quantity cannot be less than zero or zero")
            continue
        break
    except:
        print("Enter NUMBER")

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

if choice == "R" or choice == "r":
    print("Send data.", end='')
    count = 0

    for _ in range(number):
        payload = get_random_payload(questions)

        if payload != "Error" and payload != "":
            url = "/".join(url.split("/")[:-1:]) + "/formResponse"
            r = requests.post(url, data=payload,  headers=headers)

            if r.status_code == 200:
                print(".", end='')
                count += 1
            else:
                print(f"\nError. Status code {r.status_code}")
                print("Send.")
        else:
            print("Error")

    print(f"\nSuccessfully. Sent {count} data")

elif choice == "I" or choice == "i":
    payload = interactive(questions)
    print("Send data.", end='')
    count = 0

    for _ in range(number):

        if payload != "Error" and payload != "":
            url = "/".join(url.split("/")[:-1:]) + "/formResponse"
            r = requests.post(url, data=payload,  headers=headers)

            if r.status_code == 200:
                print(".", end='')
                count += 1
            else:
                print(f"\nError. Status code {r.status_code}")
        else:
            print("Error")

    print(f"\nSuccessfully. Sent {count} data")


