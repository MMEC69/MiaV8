import os

def generated_cleaner():
    result2 = "Files are not there you are clear"
    result1 = "Files are cleared"
    try:
        os.remove("words.pkl")
        os.remove("classes.pkl")
        os.remove("chatbot_model.h5")
        os.remove("mia_speech.mp3")
        return result1

    except:
        return result2

print(generated_cleaner())