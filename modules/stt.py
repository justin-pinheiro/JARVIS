import speech_recognition as sr

def getTextFromMicrophoneRecord(language_code):
    r = sr.Recognizer()
    mic = sr.Microphone()
    input = ""

    with mic as source:
        print("Jarvis vous écoute ...")

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        print("Traitement ...")
    
        try:
            text = r.recognize_google(audio, language=language_code)
            return text
        except sr.UnknownValueError:
            print("UnknownValueError")
        except sr.RequestError:
            print("RequestError")

    return input