import requests
geturl ="http://127.0.0.1:5000/"
response = requests.get(geturl)
print("get status code",response.status_code)
print(response.json())


posturl = "http://127.0.0.1:5000/users"

data = {
    "name": "Ravi"
}

response = requests.post(posturl, json=data)

print("POST status code:", response.status_code)
print(response.json())



posturl = "http://127.0.0.1:5000/users"

data = {
    "name": "Ravi"
}

response = requests.post(posturl, json=data)

print("post status code", response.status_code)
print(response.json())



puturl = "http://127.0.0.1:5000/users/1"

data = {
    "name": "Arjun Updated"
}

response = requests.put(puturl, json=data)

print("put status code", response.status_code)
print(response.json())



deleteurl = "http://127.0.0.1:5000/users/1"

response = requests.delete(deleteurl)

print("delete status code", response.status_code)
print(response.json())
