import requests

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en"

def fetch_word_data(word: str):
    url = f"{BASE_URL}/{word}"
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    else:
        response.raise_for_status()

    
