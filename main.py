from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

from schemas import Answer

import aiohttp

load_dotenv()

TG_API = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ID")

app = FastAPI()


@app.post("/")
async def read_root(obj: Answer):
    if obj.message.chat.id == int(ADMIN_ID):
        if obj.message.reply_to_message is not None:
            data = {
                'chat_id': obj.message.chat.id,
                'from_chat_id': obj.message.from_f.chat_id,
                'message_id': obj.message.message_id,
                "text": obj.message.text if obj.message.text else "No text for message"
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(f'https://api.telegram.org/bot{TG_API}/sendMessage', data=data) as response:
                    print(response.status)
    else:
        data = {
            'chat_id': ADMIN_ID,
            'from_chat_id': obj.message.from_f.chat_id,
            'message_id': obj.message.message_id
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://api.telegram.org/bot{TG_API}/forwardMessage', data=data) as response:
                print(response.status)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="localhost", reload=True)
