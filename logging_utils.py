from datetime import datetime

def log_action(action):
    with open("log.txt", "a", encoding = "utf-8") as f:
        f.write(f"{datetime.now()} - {action}\n")