import requests

url = "http://127.0.0.1:5000/generate"
payload = {"topic": "cybersecurity and ai ", "slides": 12,"theme": "Modern Dark"}
response = requests.post(url, json=payload)

if response.status_code == 200:
    with open("presentations/test_presentation.pptx", "wb") as f:
        f.write(response.content)
    print("Presentation saved")
else:
    print("Error:", response.status_code, response.text)
