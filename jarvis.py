import os
import openai
import requests
import winsound
import playsound
import speech_recognition as sr

import keys

run = True
openai.api_key = keys.OPENAI_KEY

while(run):
    

    #input
    r = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text_input = r.recognize_google(audio, language='fr-FR')
            print("\nMOI : " + text_input )
    except sr.RequestError as e:
        print("La requête a échoué: {0}".format(e))
    except sr.UnknownValueError:
        print("Je n'ai pas compris votre requête, merci de réessayer")
    except Exception as e:
        print("Une erreur s'est produite: {0}".format(e))


    #gpt
    english_prompt = "Your are now Jarvis, the AI from Iron man. You will now behave exactly like it. If i greet you or ask something, you will reply by calling me sir.\n\n"
    french_prompt = "Tu es maintenant Jarvis, l'IA d'Iron Man. Tu vas maintenant te comporter exactement comme elle. Si je te salue ou si je te demande quelque chose, tu répondras en m'appelant Monsieur.\n\n"

    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt = french_prompt + text_input,
    max_tokens=100, #100 tokens = 75 mots
    temperature=1
    )

    gpt_response = response.choices[0].text

    print("\nJARVIS : " + gpt_response )


    #tts
    language = 'fr-fr'
    voice = 'Axel'

    response = requests.get(f'http://api.voicerss.org/?key={keys.TTS_KEY}&hl={language}&v={voice}&src={gpt_response}&r=2&c=mp3')

    with open('speech.mp3', 'wb') as file:
        file.write(response.content)
    
    with open('speech.mp3', 'rb') as file:
        playsound.playsound("speech.mp3")
        file.close()
    
    os.remove("speech.mp3")

    if "Arrêt du système" in gpt_response:
        run = False