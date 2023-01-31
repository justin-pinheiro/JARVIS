from enum import Enum
import json
from io import StringIO

class Language ():
    def __init__(self, langStr):
        langObj = json.load("/lang.json").langStr
        self.ttsCode = langObj.ttsCode
        self.sttCode = langObj.sttCode
        self.voice = langObj.voice
        self.prompt = langObj.prompt
        self.unknownCommand = langObj.unknownCommand
        self.greetings = langObj.greetings
