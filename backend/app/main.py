from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for your Netlify frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://creative-sunshine-f27320.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Ciyaar OmniMind Backend Running!"}

@app.get("/api/greet/{name}")
async def greet(name: str):
    return {"greeting": f"Hello, {name}! Welcome to Ciyaar OmniMind."}

@app.post("/api/echo")
async def echo(data: dict):
    return {"you_sent": data}
