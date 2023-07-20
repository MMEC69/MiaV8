import os
import time
from gtts import gTTS
from pygame import mixer

def gTTS_TTspeech(response):
    tts = gTTS(response, lang='en', tld="ae")
    try:
        os.remove("mia_speech.mp3")
        text_msg = "Audio file removed, "
    except:
        text_msg = "Old audio file is not available everything is good to go."
    print(text_msg +"new audio file has been created.")

    tts.save("mia_speech.mp3")
    length_of_characters = len(response)
    # 1s -> 8 c
    # length_of_time = 0
    length_of_time = int(length_of_characters) / 10
    mixer.init()
    mixer.music.load("mia_speech.mp3")
    mixer.music.play()
    time.sleep(length_of_time)
    mixer.quit()
    # query = input(" ") #simple waiting mechanism
    return ("Audio played successfully.")


#gTTS_TTspeech("hello there")

#x="how are you doing, hey there General kenobi, i am looking forward of our meeting"
#gTTS_TTspeech(x)


#print (len("how are you dawdadawdawdadadawoing"))

#xall both of these functions to generate TTS



