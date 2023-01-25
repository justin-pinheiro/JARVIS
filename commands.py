import datetime
import MusicPlayer
from time import sleep
from MusicPlayer import playMusic
from jarvis import Jarvis


keywords_list = {
    "STOP": ["stop", "stoppe"],
    "DATE": ["date"],
    "PLAY": ["joue", "lance"]
}

class CommandLauncher:

    """
    Initialize a new CommandLauncher object.

    :param keyword: The keyword to recognize
    :param options: Additional options for the command
    """
    def __init__(self, jarvis : Jarvis, keyword : str, options : str):
        
        self.jarvis = jarvis
        self.keyword = keyword.lower()
        self.options = options.lower()

    """
    Recognize the command keyword.

    :return: True if keyword is recognized, False otherwise
    """
    def recognizeCommand(self) -> bool:
        
        if any(self.keyword in v for v in keywords_list.values()):
            print(f"Keyword recognized : [{self.keyword}]\n")
            return True
        else:
            return False
            
    """
    Activate the command.
    """
    def activate(self) -> None:

        #stop the system
        if self.keyword in keywords_list["STOP"]:
            print("Stopping the system...")
            sleep(1)
            self.jarvis.run = False

        #print current date
        elif self.keyword in keywords_list["DATE"]:
            date = datetime.datetime.now()
            print(date.strftime("%B %d, %Y"))
            
        #play music
        elif self.keyword in keywords_list["PLAY"]:
            playMusic(self.options)
            
        #print error message
        else:
            print("COMMAND ERROR: keyword ["+ self.keyword +"] not recognized")

         