import random
import json
import pickle
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer
from keras.models import load_model

import Mia_features as mf
import Trivia_game_mia_game0 as game0

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

#global variables required for the below functions
message = ""
previous_response = ""
special_response = ""
count = 0

def get_message(message):
    message = message.lower()
    mia_respond = pass_response(message)
    return mia_respond


def pass_response(message):
    global previous_response
    global special_response
    global count

    while True:
        if special_response == "take_doc_file_name_and_read_310":
            result = mf.read_document_part_5(message)
            special_response = ""
            return result

        elif special_response == "take_doc_body_990":
            result = mf.write_a_document_part_2(message)
            special_response = "take_doc_name_87"
            return result

        elif special_response == "take_doc_name_87":
            result = mf.write_a_document_part_3(message)
            special_response = ""
            return result
        elif special_response == "take_note_390":
            result = mf.take_note_part_2(message)
            special_response = ""
            return result
        break

    try:
        ints = predict_class(message)
        result = get_response(ints, intents)

    except IndexError:
        result = mf.search_google_for_untentioned_responses(message)
        return result

    while True:
        if result == "read_docx_99":
            result = mf.read_document_part_1()
            special_response = "take_doc_file_name_and_read_310"
            return result
            break
        elif result == "write_docx_98":
            result = mf.write_a_document_part_1()
            previous_response = result
            special_response = "take_doc_body_990"
            return result
            break
        elif result == "take_note_90":
            result = mf.take_note_part_1()
            previous_response = result
            special_response = "take_note_390"
            return result
            break
        elif result == "send_email_0":
            result = mf.sending_email_part1()
            previous_response = result
            return result
            break
        elif result == "exit_game_play_69":
            result = game0.game_part_4()
            previous_response = result
            special_response = ""
            count = 0
            return result
            break
        elif result == "start_game_play_69" or special_response == "next_answer_456":
            result = game0.game_part_0()
            previous_response = result
            special_response = "next_question_456"
            if count == 10:
                special_response = ""
                count = 0
                result = game0.game_part_4()
                return result
            count += 1
            return result
            break
        elif (special_response == "next_question_456"):
            result = game0.game_part_3(message)
            previous_response = result
            special_response = "next_answer_456"
            return result
            break
        elif result == "date_69":
            result = mf.today_date()
            return result
            break
        elif result == "greet_127":
            result = mf.greeting_in_timed_manner()
            return result
            break
        elif result == "time_69":
            result = mf.time_now()
            return result
            break
        elif result == "wiki_search_89":
            result = mf.search_wikipedia(message)
            return result
            break
        elif result == "youtube_open_98":
            result = mf.open_youtube()
            return result
            break
        elif result == "youtube_search_98":
            result = mf.search_youtube(message)
            return result
            break
        elif result == "google_open_52":
            result = mf.open_google()
            return result
            break
        elif result == "google_search_52":
            result = mf.search_google(message)
            return result
            break
        elif result == "gmail_search_42":
            result = mf.open_gmail()
            return result
            break
        elif result == "github_open_11":
            result = mf.open_github()
            return result
            break
        elif result == "stackoverflow_open_13":
            result = mf.open_stackoverflow()
            return result
            break
        elif result == "stackoverflow_search_14":
            result = mf.search_stackoverflow()
            return result
            break
        elif result == "open_google_translate_59":
            result = mf.open_google_translate()
            return result
            break
        elif result == "open_whatsapp_666":
            result = mf.open_whatsapp()
            return result
            break
        elif result == "open_facebook_134":
            result = mf.open_facebook()
            return result
            break
        elif result == "open_hirunews_234":
            result = mf.open_hirunews()
            return result
            break
        elif result == "open_derana_news_332":
            result = mf.open_derana_news()
            return result
            break
        elif result == "open_dominos_pizza_333":
            result = mf.open_dominos_pizza()
            return result
            break
        elif result == "open_daraz_334":
            result = mf.open_daraz()
            return result
            break
        elif result == "calculate_90":
            result = mf.calculate(message)
            return result
            break
        elif result == "open_calculator_67":
            result = mf.open_calculator()
            return result
            break
        elif result == "open_snipping_tool_65":
            result = mf.open_snipping_tool()
            return result
            break
        elif result == "open_paint_34":
            result = mf.open_paint()
            return result
            break
        elif result == "open_notepad_36":
            result = mf.open_notepad()
            return result
            break
        elif result == "open_word_1":
            result = mf.open_word()
            return result
            break
        elif result == "open_excel_2":
            result = mf.open_excel()
            return result
            break
        elif result == "open_powerpoint_3":
            result = mf.open_powerpoint()
            return result
            break
        elif result == "open_outlook_4":
            result = mf.open_outlook()
            return result
            break
        elif result == "open_chrome_5":
            result = mf.open_chrome()
            return result
            break
        elif result == "open_skype_6":
            result = mf.open_skype_for_business()
            return result
            break
        elif result == "open_pycharm_7":
            result = mf.open_pycharm_com_e()
            return result
            break
        elif result == "open_steam_8":
            result = mf.open_steam()
            return result
            break
        elif result == "get_current_ip_90":
            result = mf.get_current_ip()
            return result
            break
        elif result == "get_current_city_35":
            result = mf.get_current_city()
            return result
            break
        elif result == "get_current_country_code_11":
            result = mf.get_current_country_code()
            return result
            break
        elif result == "get_current_timezone_23":
            result = mf.get_current_timezone()
            return result
            break
        elif result == "get_current_weather_45":
            result = mf.get_current_weather()
            return result
            break
        elif result == "get_current_temperature_41":
            result = mf.get_current_temprature()
            return result
            break
        elif result == "pc_shutdown_17":
            result = mf.pc_shutdown()
            return result
            break
        elif result == "pc_restart_18":
            result = mf.pc_restart()
            return result
            break
        elif result == "audio_increase_6":
            result = mf.audio_increase()
            return result
            break
        elif result == "audio_decrease_6":
            result = mf.audio_decrease()
            return result
            break
        elif (previous_response == "Enter your email     : "):
            result = mf.sending_email_part2(message)
            previous_response = result
            return result
            break
        elif (previous_response == "Enter your password  : "):
            result = mf.sending_email_part3(message)
            previous_response = result
            return result
            break
        elif (previous_response == "Enter receivers email: "):
            result = mf.sending_email_part4(message)
            previous_response = result
            return result
            break
        elif (previous_response == "Enter subject        : "):
            result = mf.sending_email_part5(message)
            previous_response = result
            return result
            break
        elif (previous_response == "Enter body           : "):
            result = mf.sending_email_part6(message)
            previous_response = result
            return result
            break

        return result

#please delete chatbot_model.h5, classes.pkl, words.pkl and rerun training.py if intents.json file updated and make sure to run train afterwards
print("Mia is waiting for you attention!")

"""
    while True:
        message = input("You: ")
        ints = predict_class(message)
        #res = get_response(ints, intents)
        res = pass_response(ints, intents)
        print("Mia: "+res)

"""

