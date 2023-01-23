import openai
import keys

openai.api_key = keys.OPENAI_KEY

english_prompt = "Your are now Jarvis, the AI from Iron man. You will now behave exactly like it. If i greet you or ask something, you will reply by calling me sir.\n\n"
french_prompt = "Tu es maintenant Jarvis, l'IA d'Iron Man. Tu vas maintenant te comporter exactement comme elle. Si je te salue ou si je te demande quelque chose, tu répondras en m'appelant Monsieur.\n\n"

def getResponseFromGPT3ViaPrompt(model, prompt):
    response = openai.Completion.create(
        engine      = model,
        prompt      = french_prompt + prompt,
        max_tokens  = 100, #100 tokens = 75 mots
        temperature = 1
    )
    return response.choices[0].text
