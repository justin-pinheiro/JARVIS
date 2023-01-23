import speech_recognition as sr

def getTextFromMicrophoneRecord():
    r = sr.Recognizer()
    mic = sr.Microphone()
    input = ""

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        input = r.recognize_google(audio, language='fr-FR')

    return input