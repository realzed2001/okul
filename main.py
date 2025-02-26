# filepath: /c:/Users/Asus/git_okul/okul/okul/main.py
from fastapi import FastAPI, Request
#komut satırına çalıştırmak için yazılacak -->  uvicorn main:app --reload 

app = FastAPI()

@app.get("/")
def read_root():
    client_ip = request.client.host
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/client-ip")
def get_client_ip(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}