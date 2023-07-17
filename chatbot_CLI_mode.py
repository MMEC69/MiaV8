import random
import json
import pickle
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer
from keras.models import load_model

import Mia_features as mf

bot_name = "Mia"

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def pass_response(message):
    ints = predict_class(message)
    result = get_response(ints, intents)
    if result == "date_69":
        result = mf.today_date()
    if result == "time_69":
        result = mf.time_now()
    if result == "wiki_search_89":
        result = mf.search_wikipedia(message)
    if result == "youtube_open_98":
        result = mf.open_youtube()
    if result == "youtube_search_98":
        result = mf.search_youtube(message)
    if result == "google_open_52":
        result = mf.open_google()
    if result == "google_search_52":
        result = mf.search_google(message)
    if result == "gmail_search_42":
        result = mf.open_gmail()
    if result == "github_open_11":
        result = mf.open_github()
    if result == "stackoverflow_open_13":
        result = mf.open_stackoverflow()
    if result == "stackoverflow_search_14":
        result = mf.search_stackoverflow()
    if result == "calculate_90":
        result = mf.calculate(ints)
    if result == "open_calculator_67":
        result = mf.open_calculator()
    if result == "open_snipping_tool_65":
        result = mf.open_snipping_tool()
    if result == "open_paint_34":
        result = mf.open_paint()
    if result == "open_notepad_36":
        result = mf.open_notepad()
    if result == "open_word_1":
        result = mf.open_word()
    if result == "open_excel_2":
        result = mf.open_excel()
    if result == "open_powerpoint_3":
        result = mf.open_powerpoint()
    if result == "open_outlook_4":
        result = mf.open_outlook()
    if result == "open_chrome_5":
        result = mf.open_chrome()
    if result == "open_skype_6":
        result = mf.open_skype_for_business()
    if result == "open_pycharm_7":
        result = mf.open_pycharm_com_e()
    if result == "open_steam_8":
        result = mf.open_steam()
    if result == "get_current_ip_90":
        result = mf.get_current_ip()
    if result == "get_current_city_35":
        result = mf.get_current_city()
    if result == "get_current_country_code_11":
        result = mf.get_current_country_code()
    if result == "get_current_timezone_23":
        result = mf.get_current_timezone()
    if result == "get_current_weather_45":
        result = mf.get_current_weather()
    if result == "get_current_temperature_41":
        result = mf.get_current_temprature()
    if result == "pc_shutdown_17":
        result = mf.pc_shutdown()
    if result == "pc_restart_18":
        result = mf.pc_restart()

    return result

#please delete chatbot_model.h5, classes.pkl, words.pkl and rerun training.py if intents.json file updated and make sure to run train afterwards
print("Mia is waiting for you attention!")


while True:
    message = input("You: ")
    result = pass_response(message)
    print("Mia: " +result)



