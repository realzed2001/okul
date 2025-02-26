# filepath: /c:/Users/Asus/git_okul/okul/okul/main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    client_ip = request.client.host
    return templates.TemplateResponse("index.html", {"request": request, "client_ip": client_ip})

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/client-ip")
async def get_client_ip(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}