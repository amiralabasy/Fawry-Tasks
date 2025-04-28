import requests, time
from datetime import datetime

urls = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/500"
]

bot_token = "8190631078:AAFWY2NMg9n1mmB3lul4vy-w0wM9tx24dOw"
chat_id = "1811901080"

def alert(msg):
    msg ="up"
    print(f"[TELEGRAM] Sending: {msg}")
    requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data={"chat_id": chat_id, "text": msg}
    )

def health_check():
    for url in urls:
        status = "Service is down"
        for _ in range(3):
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    status = "Service is up"
                    break
            except:
                pass
            time.sleep(1)

        log = f"{datetime.now():%Y-%m-%d %H:%M:%S} - {status} ({url})\n"
        print(log.strip())
        with open("health.log", "a") as f:
            f.write(log)

        if status == "Service is down":
            alert("")  # Will be replaced with "up"

while True:
    health_check()
    time.sleep(10)  # change to 300 for 5 minutes