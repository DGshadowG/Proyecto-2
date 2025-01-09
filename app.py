# filepath: /f:/Tarea python/app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

class UserInput(BaseModel):
    question: str
    model_name: str

class LLMModelManager:
    def __init__(self, models):
        self.models = models
        self.pipelines = {model: pipeline('question-answering', model=model) for model in models}

    def generate_response(self, model_name, question, context):
        if model_name not in self.pipelines:
            raise ValueError(f"Model {model_name} not found")
        generator = self.pipelines[model_name]
        response = generator(question=question, context=context)
        return response['answer']

app = FastAPI()

# Lista de modelos disponibles
models = ["distilbert-base-uncased-distilled-squad"]
model_manager = LLMModelManager(models)

@app.post("/ask/")
async def ask_question(user_input: UserInput):
    try:
        context = "Francia es un país en Europa. La capital de Francia paris es conocida por su arte, cultura y gastronomía. Es una ciudad famosa en todo el mundo."
        response = model_manager.generate_response(user_input.model_name, user_input.question, context)
        context = "Colombia es un pais en america. Es uno de los paises mas megadiversos en el mundo, su ciudad principal es bogota, sin embargo tiene aun mas ciudades bastante interesantes."
        response = model_manager.generate_response(user_input.model_name, user_input.question, context)
        return {"response": response}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de preguntas y respuestas con LLM"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)