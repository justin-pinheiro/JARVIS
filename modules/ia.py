import openai
import keys

openai.api_key = keys.OPENAI_KEY

english_prompt = "Your are now Jarvis, the AI from Iron man. You will now behave exactly like it. If i greet you or ask something, you will reply by calling me sir.\n\n"
french_prompt = (
    "Tu es Jarvis, mon IA personnelle et multitâche. Tu es creatif, intelligent et très bavard. Tu as toujours quelque chose à dire et tu n'hésite pas à dire ce qui te passe par la tête. Tu m'appellera Monsieur."
)

def getResponseFromGPT3ViaPrompt(model, prompt):
    response = openai.Completion.create(
        engine = model,
        prompt = (
            french_prompt +
            "Moi: " + prompt +
            "Jarvis: "
        ),
        max_tokens = 200, #100 tokens = 75 mots
        temperature = 0.6,
        top_p = 1,
        frequency_penalty = 0.5,
        presence_penalty = 0.5,

    )
    return response.choices[0].text
