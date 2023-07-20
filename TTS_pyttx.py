import pyttsx3

#For `No module named win32com.client`, `No module named win32`, or `No module named win32api`, install `pypiwin32`.

engine = pyttsx3.init()

#testing
#engine.say("Testing, Hello how are you")
#engine.runAndWait()

#now we can change voice and rate of volume

#rate
rate = engine.getProperty('rate')
#print(rate)

rate_new_value = 135

engine.setProperty('rate', rate_new_value)

#engine.say("Testing, Hello how are you")
#engine.runAndWait()

#volume
volume = engine.getProperty('volume')
#print(volume)

volume_new_value = 1.0
engine.setProperty('volume', volume_new_value)

#print(volume)

#voice
voices = engine.getProperty('voices')

male_voice = voices[0].id
female_voice = voices[1].id

#engine.setProperty('voice', male_voice)

engine.setProperty('voice', female_voice)

#engine.say("Testing, Hello how are you")
#engine.runAndWait()

#voice save
#install 'ffmpeg'
#engine.save_to_file('parameter', 'filename.mp3')
#engine.runAndWait()

def pyttxs3_TTspeech(response):
    engine.say(response)
    engine.runAndWait()

