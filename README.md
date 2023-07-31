# Alexa GPT

![Alexa GPT](https://i.imgur.com/uk5sv5G.png)

[![License](https://img.shields.io/github/license/xtream-club/Alexa-ChatGPT)](LICENSE)

[![Last Commit](https://img.shields.io/github/last-commit/xtream-club/Alexa-ChatGPT)](https://github.com/xtream-club/Alexa-ChatGPT/commits/master)

[![Issues](https://img.shields.io/github/issues/xtream-club/Alexa-ChatGPT)](https://github.com/xtream-club/Alexa-ChatGPT/issues)

## ¡Bienvenido a Alexa ChatGPT!

Alexa ChatGPT es un chatbot inteligente impulsado por el potente modelo GPT-3.5-turbo, diseñado para interactuar con Amazon Alexa y brindar respuestas contextualizadas a las preguntas de los usuarios.

### Características principales

- **Respuestas inteligentes y contextuales:** Alexa ChatGPT utiliza el modelo GPT-3.5-turbo para ofrecer respuestas coherentes y relevantes en una amplia variedad de temas.

- **Sin necesidad de API externa:** A diferencia de otros chatbots, Alexa ChatGPT opera de forma independiente, eliminando la necesidad de una conexión a una API externa, lo que mejora su rendimiento y velocidad de respuesta.

- **Soporte para dispositivos Raspberry Pi:** Esta aplicación está optimizada para funcionar en dispositivos ARM64 y AMD, incluidos los populares dispositivos Raspberry Pi, lo que permite una experiencia óptima incluso en hardware de baja potencia.

### Cómo usar Alexa ChatGPT

Antes de utilizar Alexa ChatGPT, asegúrate de tener lo siguiente:

1. **Cuenta de Amazon Developer de Alexa:** Si aún no tienes una cuenta, regístrate en [Amazon Developer](https://developer.amazon.com/) y crea una nueva skill de Alexa.

2. **Alojar la API del chatbot:** Para que Alexa interactúe con el chatbot, debes alojar la API en un servidor accesible desde Internet. El endpoint para la API puede quedar de la siguiente manera: `https://apigpt.onrender.com`.

3. **Configuración del modelo de interacción:** Utiliza el siguiente JSON para configurar el modelo de interacción de tu skill de Alexa.

```json
{
    "interactionModel": {
        "languageModel": {
            "invocationName": "abre chat",
            "intents": [
                {
                    "name": "GptQueryIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.Person"
                        }
                    ],
                    "samples": [
                        "{query}"
                    ]
                },
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                }
            ],
            "types": []
        }
    },
    "endpoint": {
        "uri": "https://apigpt.onrender.com/chatgpt"
    }
}
```

### Cómo alojar y ejecutar Alexa ChatGPT

Puedes alojar y ejecutar Alexa ChatGPT de dos formas:


1. **Alojamiento en la nube:** Configura y despliega la API de Alexa ChatGPT en el proveedor de servicios en la nube de tu elección (por ejemplo, Heroku, AWS, Google Cloud, render, etc.). Asegúrate de exponer la API y sea accesible para las peticiones. Para desplegar el servicio gratis puedes usar [Render](https://render.com).

#### 2. Alojamiento local con Docker:

1. **Instalación de Docker:** Asegúrate de tener Docker instalado en tu Raspberry Pi o computadora.

2. **Clonar el repositorio:** Clona este repositorio en tu dispositivo.

3. **Construir el contenedor:** Navega al directorio del proyecto y construye el contenedor de Docker utilizando el siguiente comando:

   ```bash
   docker build -t tecnodaniel/alexa-gpt:latest .
   ```

4. **Ejecución del contenedor:** Ejecuta el contenedor utilizando el siguiente comando:

   ```bash
   docker run -d -p 5001:5001 tecnodaniel/alexa-gpt:latest
   ```

5. **Configuración de Alexa:** En la consola de Amazon Developer, configura la URL de tu endpoint utilizando la dirección IP y el puerto de tu Raspberry Pi o computadora donde se está ejecutando el contenedor (por ejemplo, `http://192.168.1.100:5001`).

### Cómo probar Alexa ChatGPT

Para probar el funcionamiento de Alexa ChatGPT, sigue estos pasos:

1. Activa tu dispositivo Alexa y abre la skill diciendo "Alexa, abre chat".

2. Haz preguntas en lenguaje natural a Alexa, por ejemplo: "¿Quién fue Albert Einstein?"

3. Alexa enviará tus preguntas al chatbot y te proporcionará respuestas inteligentes y contextualizadas basadas en el modelo GPT-3.5-turbo.

![Alexa ChatGPT](https://i.imgur.com/L5SRoqS.png)

### Contribución

¡Contribuciones son bienvenidas! Si deseas mejorar o agregar nuevas características a Alexa ChatGPT, simplemente crea un fork del repositorio, realiza tus cambios y envía un pull request. También puedes informar problemas o solicitar características a través de la sección de "Issues".

### Licencia

Este proyecto está licenciado bajo la Licencia MIT.

### Contacto

Si tienes alguna pregunta o sugerencia, no dudes en dejarnos un mensaje en la sección de "Issues".

Esperamos que disfrutes usando Alexa ChatGPT. ¡Diviértete interactuando con tu asistente virtual impulsado por GPT-3.5-turbo!
