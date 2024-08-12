import requests
from dotenv import load_dotenv
import os

load_dotenv()

TG_API = os.getenv("TOKEN")

whook = ""

r = requests.get(f"https://api.telegram.org/bot{TG_API}/setWebhook?url={whook}/")
print(r.json())

