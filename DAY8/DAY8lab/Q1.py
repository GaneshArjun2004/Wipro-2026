import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "User-Agent": "Python-Requests",
    "Accept": "application/json"
}

try:
    response = requests.get(url, headers=headers)

    response.raise_for_status()

    data = response.json()

    extracted_data = []

    for user in data:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        })

    with open("users_data.json", "w") as file:
        json.dump(extracted_data, file, indent=4)

    print("Data saved successfully")

except requests.exceptions.HTTPError as e:
    print("HTTP error occurred:", e)

except requests.exceptions.RequestException as e:
    print("Request error occurred:", e)
