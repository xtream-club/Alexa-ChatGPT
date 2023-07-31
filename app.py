from fastapi import FastAPI, Request
import g4f
import random
from cachetools import TTLCache

app = FastAPI()

# Respuestas aleatorias para hacer la conversación más interesante
random_responses = [
    "Claro, puedo ayudarte con eso.",
    "¡Por supuesto! Estoy aquí para responder tus preguntas.",
    "Interesante pregunta. Permíteme pensar en la respuesta.",
    "Me encanta esa pregunta. Déjame encontrar la mejor respuesta para ti.",
    "Estoy listo para responder. Adelante, pregúntame lo que quieras."
]

# Sugerencias de preguntas para iniciar la conversación
suggested_questions = [
    "Cuéntame un chiste.",
    "¿Cuál es la capital de Francia?",
    "¿Qué es el efecto invernadero?",
    "Háblame sobre la teoría de la relatividad.",
    "¿Cómo puedo cocinar una pizza?"
]

# Caché con tiempo de vida para almacenar respuestas previas
response_cache = TTLCache(maxsize=100, ttl=60)  # Tiempo de vida de 60 segundos

def get_random_response():
    return random.choice(random_responses)

def get_chatgpt_response(query):
    if query in response_cache:
        return response_cache[query]

    # Realizar la llamada a la API de chatgpt utilizando el modelo GPT-3.5-turbo
    response = g4f.ChatCompletion.create(
        model='gpt-3.5-turbo',
        provider=g4f.Provider.DeepAi,
        messages=[{"role": "user", "content": query}]
    )

    # Almacenar la respuesta en caché
    response_cache[query] = response

    return response

def create_alexa_response(text, should_end_session=False):
    # Crear la respuesta para Alexa en el formato adecuado
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": text
            },
            "shouldEndSession": should_end_session
        }
    }

@app.post("/chatgpt")
async def chat_with_gpt(request: Request):
    try:
        data = await request.json()

        if data["request"]["type"] == "LaunchRequest":
            # Respuesta para el inicio de la conversación con sugerencias de preguntas
            welcome_message = "¡Hola! Soy tu asistente virtual, listo para responder tus preguntas. ¿En qué puedo ayudarte hoy?"
            suggested_qs = "Puedes preguntarme sobre: " + ", ".join(suggested_questions)
            response_text = f"{welcome_message} {suggested_qs}"
        elif data["request"]["type"] == "IntentRequest":
            # Si es una solicitud de intent, obtener el valor del slot "query"
            query = data["request"]["intent"]["slots"]["query"]["value"]
            response_text = get_chatgpt_response(query)
        else:
            # Si es otro tipo de solicitud, responder con una respuesta aleatoria
            response_text = get_random_response()

        # Mantener la sesión activa para permitir más interacciones
        alexa_response = create_alexa_response(response_text, should_end_session=False)

        return alexa_response

    except Exception:
        error_response = create_alexa_response("¡Gracias por usarme y espero poder ayudarte pronto!",
                                               should_end_session=True)
        return error_response

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5001)
