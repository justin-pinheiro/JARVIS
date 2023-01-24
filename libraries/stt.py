import speech_recognition as sr

def getTextFromMicrophoneRecord():
    try:
        r = sr.Recognizer()
        mic = sr.Microphone()
        input = ""

        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            input = r.recognize_google(audio, language='fr-FR')
            
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return input