from __future__ import print_function
import os
import time #To tell time
import datetime #To tell date
import pyjokes
import webbrowser
import calendar
import random
import smtplib
import wikipedia #To search on wikipedia
import playsound
import wolframalpha #For calculations
import requests
#import winshell
import subprocess
import ctypes
#from twilio.rest import Client
import pickle
import os.path
#from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
#from selenium import webdriver
from time import sleep
import webbrowser #import webbrowsers
from geopy.geocoders import Nominatim #provide current location
import subprocess #use to open any application within system
import ssl #for emails ending
from email.message import EmailMessage #for emails ending
import smtplib #for emails ending
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL #windows audio control
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume #windows audio control
import math #windows audio control




def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    year_now = now.year
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + " " +str(year_now) +"."

#function testing
#result = today_date()
#print(result)

def time_now():
    now_hour = datetime.datetime.now().hour
    now_minute = datetime.datetime.now().minute
    #now_second = datetime.datetime.now().second
    #strTime = datetime.datetime.now().strftime("%H:%M:%S")

    if now_minute < 10:
        now_minute = str(now_minute)
        now_minute = "0" +now_minute
    else:
        now_minute = str(now_minute)

    if now_hour>12:
        now_hour = now_hour - 12
        now_hour = str(now_hour)
        day_divider = "PM"
    else:
        now_hour = "0" +str(now_hour)
        day_divider = "AM"

        #it's already been converted to int -> string
    return "The time is " +now_hour +":" +now_minute +" " +day_divider

#function testing
#result = time_now()
#print(result)


def search_wikipedia(user_message):
    user_message = user_message.replace("wikipedia", " ")
    results = wikipedia.summary(user_message, sentences=3)
    return results

#function testing
#result = search_wikipedia("elon musk to wikipedia")
#print(result)

def greeting_in_timed_manner():
    current_hour = datetime.datetime.now().hour

    if current_hour>=0 and current_hour<4:
        wishing_upon_greeting = "You haven't slept, Technically it's a good morning though? How are you doing?"
        return wishing_upon_greeting
    elif current_hour >= 4 and current_hour < 10:
        wishing_upon_greeting = "Good morning love, How are you doing?, have you had your breakfast?"
        return wishing_upon_greeting
    elif current_hour >= 10 and current_hour < 12:
        wishing_upon_greeting = "it's almost daytime, Have you had a cup of tea?, Any way Good morning love,"
        return wishing_upon_greeting
    elif current_hour >= 12 and current_hour < 15:
        wishing_upon_greeting = "have you had lunch?, I am craving for some good lasgna now?, Good after noon, what are your plans at evening?,"
        return wishing_upon_greeting
    elif current_hour >= 15 and current_hour < 18:
        wishing_upon_greeting = "Wow it's reached almost the end of the day?, how are you feeling?, Have you had a cup of tea?, Good evening by the way,"
        return wishing_upon_greeting
    elif current_hour >= 18 and current_hour < 22:
        wishing_upon_greeting = "it's getting dark, I hope you have reached home by now, how was your day?, Good night by the way,"
        return wishing_upon_greeting
    elif current_hour >= 22 and current_hour < 0:
        wishing_upon_greeting = "it's time to sleep, Good night sweet dreams"
        return wishing_upon_greeting
    else:
        return "good day to you,"


def open_youtube():
    youtube_url = "https://www.youtube.com"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(youtube_url)

    except:
        webbrowser.open_new_tab(youtube_url)

    time.sleep(5)
    return ("Youtube is opened dear,")

#function testing
#result = open_youtube()
#print(result)

def search_youtube(user_message):
    youtube_search_url = "http://www.youtube.com/results?search_query="
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(youtube_search_url +user_message)

    except:
        webbrowser.get('chrome').open_new_tab(youtube_search_url +user_message)

    time.sleep(5)
    return ("Searching for.. " +str(user_message) +" on youtube")

#function testing
#search_youtube("search for cats in youtube")
#print(result)

def open_google():
    google_url = "https://www.google.com"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(google_url)

    except:
        webbrowser.open_new_tab(google_url)

    time.sleep(5)
    return ("google is opened dear,")

#function testing
#open_google()
#print(result)

def search_google(user_message):
    google_search_url = "https://www.google.com/search?q="
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(google_search_url +user_message)

    except:
        webbrowser.get('chrome').open_new_tab(google_search_url +user_message)

    time.sleep(5)
    return ("Searching for.. " +str(user_message) +" on google")

#function testing
#search_google("search for cats in google")
#print(result)

def open_gmail():
    gmail_url = "https://mail.google.com/"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(gmail_url)

    except:
        webbrowser.open_new_tab(gmail_url)

    time.sleep(5)
    return ("gmail is opened dear,")

#function testing
#open_gmail()
#print(result)

def open_github():
    github_url = "https://www.github.com"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(github_url)

    except:
        webbrowser.open_new_tab(github_url)

    time.sleep(5)
    return ("Github is opened dear,")

#function testing
#open_github()
#print(result)

def open_stackoverflow():
    stackoverflow_url = "https://stackoverflow.com/"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(stackoverflow_url)

    except:
        webbrowser.open_new_tab(stackoverflow_url)

    time.sleep(5)
    return ("Stackoverflow is opened dear,")


def search_stackoverflow(user_message):
    search_stackoverflow_url = "https://stackoverflow.com/search?q="
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(search_stackoverflow_url +user_message)

    except:
        webbrowser.open_new_tab(search_stackoverflow_url +user_message)

    time.sleep(5)
    return ("Searching for.." +str(user_message) +"on stackoverflow")

#function testing
#search_stackoverflow("python library error")
#print(result)
def open_google_translate():
    google_translate_url = "https://translate.google.com/"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(google_translate_url)

    except:
        webbrowser.open_new_tab(google_translate_url)

    time.sleep(5)
    return ("Google translate is opened dear,")

def open_whatsapp():
    whatsapp_web_url = "https://web.whatsapp.com/"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(whatsapp_web_url)

    except:
        webbrowser.open_new_tab(whatsapp_web_url)

    time.sleep(5)
    return ("Google translate is opened dear,")

def open_facebook():
    facebook_url = "https://www.facebook.com/"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(facebook_url)

    except:
        webbrowser.open_new_tab(facebook_url)

    time.sleep(5)
    return ("Google translate is opened dear,")

def open_porn_hub():
    pornhub_url = "https://www.pornhub.com/"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(pornhub_url)

    except:
        webbrowser.open_new_tab(pornhub_url)

    time.sleep(5)
    return ("Porn Hub is opened, It's time to wank then.")

def search_porn_hub(user_message):
    pornhub_search_url = "https://www.pornhub.com/video/search?search="
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(pornhub_search_url +user_message)

    except:
        webbrowser.open_new_tab(pornhub_search_url +user_message)

    time.sleep(5)
    return ("Searching for.. " +str(user_message) +" on pornhub")

def calculate(user_message):
    app_id = "X9R6L7-4WYATQWJ9V"
    client = wolframalpha.Client('R2K75H-7ELALHR35X')
    user_message = client.query(user_message)
    answer = next(user_message.results).text
    return answer

#function testing
#result = calculate("2+3")
#print(result)


#"""Functions to open windows applications"""
def return_error():
    return "i think something is wrong can you try again later, or contact developer for a fix,\n" \
           "email -> coorayeronnemanoshawoodapple@gmail.com"

def open_calculator():
    try:
        subprocess.Popen("C:\\Windows\\System32\\calc.exe")
        msg = "Calculator is opened dear,"
    except:
        msg = return_error()
    return msg

def open_snipping_tool():
    try:
        subprocess.Popen("C:\\Windows\\System32\\SnippingTool.exe")
        msg = "SnippingTool is opened dear,"
    except:
        msg = return_error()
    return msg
def open_paint():
    try:
        subprocess.Popen("C:\\Windows\\System32\\mspaint.exe")
        msg = "Mspaint is opened dear,"
    except:
        msg = return_error()
    return msg
def open_notepad():
    try:
        subprocess.Popen("C:\\Windows\\System32\\Notepad.exe")
        msg = "Notepad is opened dear,"
    except:
        msg = return_error()
    return msg

def open_word():
    try:
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        msg = "Word is opened honey,"
    except:
        msg = return_error()
    return msg
def open_excel():
    try:
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        msg = "Excel is opened honey,"
    except:
        msg = return_error()

    return msg

def open_powerpoint():
    try:
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
        msg = "Powerpoint is opened honey,"
    except:
        msg = return_error()

    return msg

def open_outlook():
    try:
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
        msg = "Ms Outlook is opened honey,"
    except:
        msg = return_error()

    return msg

def open_chrome():
    try:
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        msg = "Chrome is opened honey,"
    except:
        msg = return_error()

    return msg

def open_skype_for_business():
    try:
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\lync.exe")
        msg = "Skype is opened honey,"
    except:
        msg = return_error()

    return msg

def open_pycharm_com_e():
    try:
        subprocess.Popen("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.2\\bin\\pycharm64.exe")
        msg = "Pycharm is opened honey,"
    except:
        msg = return_error()

    return msg

def open_steam():
    try:
        subprocess.Popen("C:\\Program Files (x86)\\Steam\\Steam.exe")
        msg = "Steam is opened honey,"
    except:
        msg = return_error()

    return msg

#functions testing(just change name)
#result = open_chrome()
#print(result)

#"""End of the functions used to open system applications"""

#base function

#"""Current location identifies"""
def get_current_ip():
    try:
        r = requests.get("https://get.geojs.io/")

        ip_request = requests.get("https://get.geojs.io/v1/ip.json")
        ip_address = ip_request.json()['ip']
        return (ip_address)
    except:
        msg = return_error()

    return msg
def get_current_location_information():
    try:
        ip_address = get_current_ip()

        url = "https://get.geojs.io/v1/ip/geo/" +ip_address +".json"
        geo_request = requests.get(url)
        geo_data = geo_request.json()
        return(geo_data)

    except:
        msg = return_error()

    return msg

def get_current_city():
    try:
        current_location_information_data = get_current_location_information()
        current_country = (current_location_information_data['country'])
        current_city = (current_location_information_data['city'])
        return("You are currently in "+current_city +", " +current_country +".")
    except:
        msg = return_error()

    return msg

def get_current_city_only():
    try:
        current_location_information_data = get_current_location_information()
        current_city = (current_location_information_data['city'])
        return(current_city)
    except:
        msg = "colombo"

    return msg

def get_current_timezone():
    try:
        current_location_information_data = get_current_location_information()
        current_timezone = (current_location_information_data['timezone'])
        return ("your current time zone is " +current_timezone)
    except:
        msg = return_error()

    return msg

def get_current_country_code():
    try:
        current_location_information_data = get_current_location_information()
        current_country_code = (current_location_information_data['country_code3'])
        return ("your current country code is " +current_country_code)
    except:
        msg = return_error()

    return msg

#functions testing(just change name)
#result = get_current_country_code()
#print(result)

#"""End of current location identifies"""

#"""Weather details"""

def get_current_weather_parameters():
    try:
        api_key = "3e826e0f9e9479c77abab338620624bd"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        current_city_name = get_current_city_only()
        complete_url = base_url + "appid=" + api_key + "&q=" + current_city_name
        response = requests.get(complete_url)
        return response.json()
    except:
        msg = return_error()

    return msg

def get_current_weather():
    try:
        x = get_current_weather_parameters()
        current_city_name = get_current_city_only()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature = current_temperature - 273.15
            current_temperature = int(current_temperature)
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            return ("It will be about " + str(current_temperature) + " Celcius" + " in " +current_city_name
                    +"\nHumidity is around " +str(current_humidity) +"%"
                    +"\n" +current_city_name +" is having a " + str(weather_description)) +" day."
    except:
        msg = return_error()

    return msg
def get_current_temprature():
    try:
        x = get_current_weather_parameters()
        current_city_name = get_current_city_only()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature = current_temperature - 273.15
            current_temperature = int(current_temperature)
            return "Current temp in " +current_city_name +" is " +str(current_temperature) +" Celcius"
    except:
        msg = return_error()

    return msg

#functions testing(just change name)
#result = get_current_temprature()
#print(result)

#"""End of weather details"""

#"""Pc shutdown, restart, sleep functions"""
def pc_shutdown():
    try:
        seconds = 10
        strOne = "shutdown /s /t"
        strTwo = str(seconds)
        str = strOne+strTwo

        os.system(str)
        return ("Your system is going to shut down in 10 seconds, starting from now")

    except:
        msg = return_error()
        return msg

def pc_restart():
    try:
        seconds = 10
        strOne = "shutdown /r /t"
        strTwo = str(seconds)
        str = strOne + strTwo

        os.system(str)
        return ("Your system is going to shut down in 10 seconds, starting from now")

    except:
        msg = return_error()
        return msg

#functions testing(just change name)
#result = get_current_temprature()
#print(result)

#"""End of Pc shutdown, restart, sleep functions"""


#"""Sending an email functions"""
    #ui -> user input

def return_error_for_email():
    return "You might have to check the username and password whether matches or not. \nMake sure to equip your account with 2step verifiaction and to use a generated app app password instead of user password."
def sending_email_part1():
    return "Enter your email     : "
def sending_email_part2(email_sender_ui):
    global email_sender
    email_sender = email_sender_ui
    return "Enter your password  : "

def sending_email_part3(email_password_ui):
    global email_password
    email_password = email_password_ui
    return "Enter receivers email: "

def sending_email_part4(email_receivers_ui):
    global email_receiver
    email_receiver = email_receivers_ui
    return "Enter subject        : "

def sending_email_part5(subject_ui):
    global subject
    subject = subject_ui
    return "Enter body           : "

def sending_email_part6(body_ui):
    try:
        global body
        body = body_ui

        em = EmailMessage()

        em['From'] = email_sender

        em['To'] = email_receiver

        em['Subject'] = subject

        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        email_parameter_cleaning()

        return "Email sent successfully."
    except:
        email_parameter_cleaning()
        return return_error_for_email()


def email_parameter_cleaning():
    email_sender = ""
    email_receiver = ""
    subject = ""
    body = ""


#""" End of sending an email functions"""

#"""Windoes volume control"""



# Get default audio device using PyCAW
def audio_increase():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get current volume
    currentVolumeDb = volume.GetMasterVolumeLevel()

    increasing_value = 6.0

    volume.SetMasterVolumeLevel(currentVolumeDb + increasing_value, None)

    return "Audio has been increased"

def audio_decrease():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get current volume
    currentVolumeDb = volume.GetMasterVolumeLevel()

    increasing_value = 6.0

    volume.SetMasterVolumeLevel(currentVolumeDb - increasing_value, None)

    return "Audio has been decreased"

#functions testing(just change name)
#result = audio_decrease()
#print(result)


#""" End of windoes volume control"""