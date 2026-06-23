from fastapi import APIRouter
from pydantic import BaseModel

from src.travel_agent_api_giulianatecchio.services.agent_service import Agent

chat_router = APIRouter()

# Modello per validare i dati inviati dal frontend
class ChatCompletionRequest(BaseModel):
    messages: list

    model_config = {
        "json_schema_extra": {
            "example": {
                "messages": [{"role": "user", "content": "Vorrei organizzare un viaggio a Napoli"}]
            }
        }
    }

@chat_router.post("/travel-agent")
def chat_completion(request: ChatCompletionRequest):
    # Tracing richiesto dal professore
    print("*" * 80)
    print("Richiesta ricevuta in chat_completion")
    
    agent = Agent()
    response = agent.run(messages=request.messages)
    
    print("Risposta generata con successo")
    print("*" * 80)
    
    return response
