import os
import eel

from engine.features import *
from engine.commands import *
from engine.auth import recoganize
def start():
    
    eel.init("www")

    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak_now("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        flag=1
        if flag == 1:
            eel.hideFaceAuth()
            speak_now("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak_now("Welcome Sir!!")
            eel.hideStart()
            playAssistantSound()
        else:
            speak_now("Face Authentication Fail")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)