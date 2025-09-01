import requests
response_get = requests.get("https://todo.pixegami.io")
print(response_get)  # Response [200]
print(response_get.status_code)  # int
print(response_get.json())  # dict
print(response_get.json()["message"])  # dict

body = response_get.json() #-> body: {'message': 'Hello world from Todo API'}
print(body["message"])

def test_can_call_api():
    respnse = requests.get("https://todo.pixegami.io")
    code = response.status_code
    expected = 200
    print(f"expected: {expected}, status_code: {code}")
    assert code == expected