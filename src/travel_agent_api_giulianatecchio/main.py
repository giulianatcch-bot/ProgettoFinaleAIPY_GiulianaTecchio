from dotenv import load_dotenv 
load_dotenv() 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importazione del router dalla cartella routes
from src.travel_agent_api_giulianatecchio.routes.chat_router import chat_router

app = FastAPI()

# Configurazione CORS (collegamento Laravel)
origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrazione del router
app.include_router(chat_router, prefix="/chat", tags=["Chat"])