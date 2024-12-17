import requests, time, random

url = 'http://localhost:5001/login'

while True:
    time.sleep(random.randint(1, 6))
    response = requests.get(url)
    print(response.json())
