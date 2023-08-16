from playsound import playsound
import os
import json
import re
import threading
class AudioPlayer:
    def __init__(self):
        self.absolute_path = os.path.dirname(__file__)
        self.audioFolder = os.path.join(self.absolute_path, "audio\\")
        self.audioFileDict = {}
        self.splitPattern = r"(\.|Both|Left|Right)"

    def start(self):
        self.sortFiles()

    def sortFiles(self):
        for file_name in os.listdir(self.audioFolder):
            if file_name.startswith(("Both", "Left", "Right")):
                fileSplit = re.split(self.splitPattern, file_name)
                if fileSplit[2] not in self.audioFileDict:
                    self.audioFileDict[fileSplit[2]] = {fileSplit[1]: file_name}
                else:
                    self.audioFileDict[fileSplit[2]][fileSplit[1]] = file_name

        
        return self.audioFileDict

    def playAudio(self, fileName):
        playsound(self.audioFolder + fileName, block=False)

    def playSortedSounds(self):
        for sound in self.audioFileDict:
            # Add your code here to play the sounds in the desired order
            pass


