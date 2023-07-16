import random
import json
import pickle
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer
from keras.models import load_model

import Mia_features as mf

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

def pass_response(ints, intents):
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
        result = mf.calculate(message)

    return result

#please delete chatbot_model.h5, classes.pkl, words.pkl and rerun training.py if intents.json file updated
print("Mia is waiting for you attention!")

while True:
    message = input("You: ")
    ints = predict_class(message)
    #res = get_response(ints, intents)
    res = pass_response(ints, intents)
    print("Mia: "+res)

