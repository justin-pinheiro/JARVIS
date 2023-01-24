import openai
import nlpcloud
import keys

openai.api_key = keys.OPENAI_KEY
client = nlpcloud.Client("fast-gpt-j", keys.NLPCLOUD_KEY, True)

english_prompt = "Your are now Jarvis, the AI from Iron man. You will now behave exactly like it. If i greet you or ask something, you will reply by calling me sir.\n\n"
french_prompt = "Je suis JARVIS, une IA très intelligente, Monsieur. J'ai été créé par Tony Stark. Je réponds toujours de manière formelle et je vous appelle Monsieur. Quand on me demande de jouer de la musique, je réponds \"MUSIC ON\". \n\n"

def getResponseFromGPT3ViaPrompt(model, prompt):
    response = openai.Completion.create(
        engine      = model,
        prompt      = french_prompt + "Q: " + prompt + "\nA: ",
        max_tokens  = 200, #100 tokens = 75 mots
        temperature = 0.7
    )
    return response.choices[0].text

def getResponseFromChatBot(input, context, history):
    response = client.chatbot(input, context, history)
    return response["response"]