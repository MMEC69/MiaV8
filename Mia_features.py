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

import subprocess #use to open any application within system



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
    return ("Searching for.." +str(user_message) +"on youtube")

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
    return ("Searching for.." +str(user_message) +"on google")

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

#function testing
#open_stackoverflow()
#print(result)

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

def calculate(user_message):
    app_id = "X9R6L7-4WYATQWJ9V"
    client = wolframalpha.Client('R2K75H-7ELALHR35X')
    user_message = client.query(user_message)
    answer = next(user_message.results).text
    return answer

#function testing
#result = calculate("2+3")
#print(result)


"""Functions to open windows applications"""
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

"""End of the functions used to open system applications"""