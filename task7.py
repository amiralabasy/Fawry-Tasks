import requests

ip = "8.8.8.8"
url = f"http://ip-api.com/json/{ip}"

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    
    if data['status'] == 'success':
        print("IP:", data['query'])
        print("City:", data['city'])
        print("Region:", data['regionName'])
        print("Country:", data['country'])
        print("Coordinates:", f"{data['lat']}, {data['lon']}")
    else:
        print("API Error:", data['message'])

except requests.exceptions.RequestException as e:
    print("Network error:", e)