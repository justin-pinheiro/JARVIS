import speech_recognition as sr

def getTextFromMicrophoneRecord():
    r = sr.Recognizer()
    mic = sr.Microphone()
    input = ""

    with mic as source:

        print("Jarvis vous écoute ...")

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        print("Traitement ...")
    
        try:
            text = r.recognize_google(audio, language='fr-FR')
            return text

        except sr.UnknownValueError:
            print("Je n'ai pas compris votre requête", "fr-fr", "Axel", "speech.mp3")
        except sr.RequestError:
            ("Une erreur s'est produite", "fr-fr", "Axel", "speech.mp3")

    return input