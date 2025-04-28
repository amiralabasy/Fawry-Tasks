import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url)
    response.raise_for_status()

    
    data = response.json()
    
    with open("posts_data.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print("Data successfully saved to posts_data.json.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while accessing the API: {e}")


    