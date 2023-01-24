import openai
import keys

openai.api_key = keys.OPENAI_KEY

english_prompt = "Your are now Jarvis, the AI from Iron man. You will now behave exactly like it. If i greet you or ask something, you will reply by calling me sir.\n\n"
french_prompt = (
    "Tu es Jarvis, mon IA personnelle et multitâche, tu m'appellera monsieur."
    "Lorsque je te demanderai de jouer une musique tu me répondra par \"Je lance la musique\" et tu ajoutera le nom de la musique."
    "Lorsque je te demanderai de noter quelque chose, tu me répondra \"Je note\" et tu ajoutera le contenu de la note." 
    "Lorsque je te demanderai de t'éteindre ou d'arrêter le systême, tu répondra \"Arrêt du système\"."
)

def getResponseFromGPT3ViaPrompt(model, prompt):
    response = openai.Completion.create(
        engine = model,
        prompt = (
            french_prompt +
            "Q: " + prompt +
            "A: "
        ),
        max_tokens = 200, #100 tokens = 75 mots
        temperature = 0.2
    )
    return response.choices[0].text
