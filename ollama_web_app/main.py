from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import json
from langchain.llms import Ollama  # ✅ Import the Ollama client

app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize templates directory
templates = Jinja2Templates(directory="templates")

# Render the frontend
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Initialize Ollama client
gemma_9b = Ollama(base_url="http://localhost:11434", model="gemma2")

# API route to handle user input and call Ollama
@app.post("/generate")
async def generate_response(data: dict):
    user_input = data.get("message", "")
    print("User input:", user_input)
    
    if not user_input:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        print("Calling Ollama...")
        response = gemma_9b(user_input)  # ✅ Direct call to Ollama API
        print("Response received:", response)

        return {"response": response}

    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))
