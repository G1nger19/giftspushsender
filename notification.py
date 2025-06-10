import requests

PUSHOVER_USER_KEY = "gb3witvz73fniipbh9wnxtcnm84mqr"
PUSHOVER_API_TOKEN = "axc7sa4t81e4tbjv6ivfp7ntso76yt"
PUSHOVER_URL = "https://api.pushover.net/1/messages.json"

def send_pushover_notification(title: str, message: str):
    data = {
        "token": PUSHOVER_API_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "title": title,
        "message": message,
        "priority": 1,
        "sound": "siren",
    }
    try:
        response = requests.post(PUSHOVER_URL, data=data)
        response.raise_for_status()
        print("Pushover notification sent")
    except requests.RequestException as e:
        print(f"Pushover error: {e}")
