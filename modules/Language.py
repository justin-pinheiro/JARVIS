# from enum import Enum
# import json
# from io import StringIO

# class Language ():
#     def __init__(self, langStr):
#         langObj = json.load("/lang.json").langStr
#         self.ttsCode = langObj.ttsCode
#         self.sttCode = langObj.sttCode
#         self.voice = langObj.voice
#         self.prompt = langObj.prompt
#         self.unknownCommand = langObj.unknownCommand
#         self.greetings = langObj.greetings


from enum import Enum

class Languages (Enum):
    ENGLISH = "ENGLISH"
    FRENCH = "FRENCH"
    SPANISH = "SPANISH"


def getVoice(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return 'Harry'
        case Languages.FRENCH:
            return 'Axel'
        case Languages.SPANISH:
            return 'Diego'

def getTTScode(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "en-gb"
        case Languages.FRENCH:
            return "fr-fr"
        case Languages.SPANISH:
            return "es-es"

def getSTTCode(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return 'en-US'
        case Languages.FRENCH:
            return 'fr-FR'
        case Languages.SPANISH:
            return 'es-ES'

def getPrompt(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "Your are now Jarvis, the AI from Iron man. You will now behave exactly like it. If i greet you or ask something, you will reply by calling me sir.\n\n"
        case Languages.FRENCH:
            return "Tu es Jarvis, mon IA personnelle et multitâche. Tu es creatif, intelligent et très bavard. Tu as toujours quelque chose à dire et tu n'hésite pas à dire ce qui te passe par la tête. Tu m'appellera Monsieur."
        case Languages.SPANISH:
            return "Ahora eres Jarvis, la IA de Iron Man. Ahora te comportarás exactamente como él. Si te saludo o pregunto algo, responderás llamándome señor."

def unknownCommand(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "I am sorry, the command you asked for does not exist."
        case Languages.FRENCH:
            return "Je suis désolé, la commande demandée n'existe pas."
        case Languages.SPANISH:
            return "Lo siento, el comando que ha solicitado no existe."

def greetings(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "Hello, Sir."
        case Languages.FRENCH:
            return "Bonjour, Monsieur."
        case Languages.SPANISH:
            return "Hola, Señor."