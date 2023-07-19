import os

def generated_cleaner():
    result2 = "Files are not there you are clear"
    result1 = "Files are cleared"
    try:
        os.remove("words.pkl")
        os.remove("classes.pkl")
        os.remove("chatbot_model.h5")
        result1

    except:
        result2

generated_cleaner()