import speech_recognition as sr
import pyaudio
import TTS_pyttx as ttp
import TTS_gtts as ttg

def take_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #listening
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-us')

        except Exception as e:
            #ttp.pyttxs3_TTspeech("Pardon me, please say that again")
            #ttg.gTTS_TTspeech("Pardon me, please say that again")
            return " "
    return statement

#z =take_speech()
#print(z)