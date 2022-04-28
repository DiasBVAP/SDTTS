import time
from gtts import gTTS
from pygame import mixer

def main():
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.set_volume(1.0)
    while True:
        message = input('Mensagem: ')
        if message[0] == '*':
            tts = gTTS(message[1:], lang="en")
        else:
            tts = gTTS(message, lang="pt")
        tts.save('mensagem.mp3')
        mixer.music.load('mensagem.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.5)
        mixer.music.unload()

if __name__ == "__main__":
    main()