import requests
from GetPayload import get_random_payload

url = input("Enter url: ")
number = input("Enter the number of iterations: ")


headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = get_random_payload(url)
print(payload)


if payload != "Error" and payload != "" and number.isdigit():
    url = "/".join(url.split("/")[:-1:]) + "/formResponse"
    print(url)

    for i in range(int(number)):
        r = requests.post(url, data=payload,  headers=headers)
        if r.status_code == 200:
            print(f"The {i + 1} package was sent successfully")
        else:
            print(f"Error. Status code {r.status_code}")
else:
    print("Error")

