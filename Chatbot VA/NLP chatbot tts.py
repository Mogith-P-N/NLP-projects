# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:49:46 2023

@author: mogit
"""
#importing necessary packages
import pymongo 
import pyttsx3
import speech_recognition as sr

#we are storing the user details in a json format in local mongodb as a document.

mongo=pymongo.MongoClient("mongodb://127.0.0.1:27017/") #calling mongodb local instance , if needed you can add mongo atlas link with credentials to store it in cloud db.
mydb=mongo['chatbot_VA']
mycollection=mydb['Customer_details']


def voice_input():
  engine = pyttsx3.init() #declaring the text to speech engine
  r = sr.Recognizer()     #creating recognizer instance
  mic = sr.Microphone(device_index=1) #assigning microphone to get speech input
  with mic as source:
    print("\n I'm listening ...")
    r.adjust_for_ambient_noise(source, duration=0.3) #the listener waits for 0.3 secs 
    audio = r.listen(source)
  try:
    #print(r.recognize_google(audio)) #will recognizes our audio input and check the possible permutations and give the one with high confidence value
    return r.recognize_google(audio) #returning the processed audio as a text (string)
  except:
      return 'NA'
    

if __name__ == '__main__': #main code
    
    customer_detail={}
    print("Hi, this is jarvis here to assist you with your booking")
    print("\n may I know please know the name... ?")
    customer_detail['name']=voice_input()
    print("\n Your contact number ....?")
    customer_detail['contact']=voice_input()
    print("\n Your Address....?")
    customer_detail['address']=voice_input()
    print("\n what ID proof you gonna submit ....?")
    customer_detail['id']=voice_input()
    print("\n What type of room you want ....?")
    customer_detail['roomtype']=voice_input()
    print("\n Your date of arrival ....?")
    customer_detail['arrival']=voice_input()
    print("\n checkout date ....?")
    customer_detail['checkout']=voice_input()
    
    mycollection.insert_one(customer_detail) #inserting the collected details into mongodb database named "chatbot_VA"
    
    print("Thanks for booking with jarvis. Here is your booking details \n",customer_detail)

























    