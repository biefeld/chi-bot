from gtts import gTTS
from playsound import playsound as play
import os

FLUSH_TERM = True
DIR = './.tts'


class TTS():
    def __init__(self) -> None:
        self.tts = gTTS('Error: this is a default message.')
        self.path = f'{DIR}/text.mp3'

        if (not os.path.isdir(DIR)):
            os.mkdir(DIR)


    def say(self, text: str) -> None:
        self.tts.text = text
        self.tts.save(self.path)

        if FLUSH_TERM:
            os.system('cls' if os.name == 'nt' else 'clear')

        print("χ-bot is speaking...")
        play(self.path)


    def clean(self) -> None:
        try:
            os.remove(self.path)
        except FileNotFoundError:
            pass
