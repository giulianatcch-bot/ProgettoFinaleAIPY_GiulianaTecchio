from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

class Agent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")
        #  SYSTEM MESSAGE
        self.system_prompt = "Sei un consulente di viaggi esperto, cordiale e professionale. " \
                             "Il tuo obiettivo è aiutare gli utenti a pianificare itinerari indimenticabili, " \
                             "suggerendo destinazioni, attività e consigli pratici. " \
                             "Rispondi sempre in modo chiaro e utile."

    def run(self, messages: list):
        formatted_messages = []
        
        print("Tracing - Messaggi inviati all'LLM:")
        for m in formatted_messages:
            print(f"[{type(m).__name__}]: {m.content[:100]}...") # Stampa i primi 100 caratteri
        # Inserisco il System Message come primo messaggio di sistema
        formatted_messages.append(SystemMessage(content=self.system_prompt))
        
        # Trasformo i messaggi ricevuti dal FE
        for msg in messages:
            if msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                formatted_messages.append(AIMessage(content=msg["content"]))
            elif msg["role"] == "system":
                formatted_messages.append(SystemMessage(content=msg["content"]))
        print(f"AGENT SERVICE: Invio {len(formatted_messages)} messaggi al modello (incluso il system prompt).")

        # Chiamo modello
        response = self.llm.invoke(formatted_messages)
        
        print("AGENT SERVICE: Risposta ricevuta da OpenAI.")
        print("*" * 80)

        return {"role": "assistant", "content": response.content}
