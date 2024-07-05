from fastapi import FastAPI, HTTPException
from httpx import AsyncClient

app = FastAPI()

@app.post("/send-message")
async def send_message():
    async with AsyncClient() as client:
        url = "http://localhost:8080/send-message"
        await client.post(url, json={"message": "Hey.. This is an application to strean messages."})
    return {"message": "Message sent successfully"}
