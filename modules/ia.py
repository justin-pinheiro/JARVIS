import openai
import keys
from enum import Enum

openai.api_key = keys.OPENAI_KEY

class Models (Enum):
    DAVINCI = "text-davinci-003"
    CURIE = "text-curie-001"
    BABBAGE = "text-babbage-001"
    ADA = "text-ada-001"

def getResponseFromGPT3ViaPrompt(model, input, prompt):
    print(prompt)

    response = openai.Completion.create(
        engine = "text-babbage-001",
        prompt = (
            prompt +
            "HUMAN: " + input +
            "JARVIS: "
        ),
        max_tokens = 200, #100 tokens = 75 mots
        temperature = 0.6,
        top_p = 1,
        frequency_penalty = 0.5,
        presence_penalty = 0.5,

    )
    return response.choices[0].text
