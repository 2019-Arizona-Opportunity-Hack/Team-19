
from flask import Flask
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from pymongo import MongoClient
import os

# Set up database connection
client = MongoClient("localhost:27017")
mongoDB=client["animal-rescue"]

# Set up app
app = Flask(__name__)

# Set up Monogo Engine
db = MongoEngine(app)

data = mongoDB.adopters.find()

a = [a for a in data]
#for a in data: 
  #  print(a)
#print(a)

def deArrayfy(arr):
    for i in arr:
        return i
inData = deArrayfy(a)

print(inData['do-not-adopt'])




"""
input 
  "name": " ", 
        "AnimalType": "",
        "Housing":{
            'homeType':'',  
            'homeStatus':'', own ++ |  rent -- should be a small factor 
            'petDeposit': 0,  --, depedent of financhal
            'addationalPetRent': 0, ^ 
            'rentalRestriction': '', -- Must qualify, NLTK? 
            "planToMove": "", --
            "animalOutside": "", Large --
            "visitingAnimals": "", --
            "visitingAnimalsType": "", info
            "vistiingChildren": "", --
            "childrenAgeAndFrequency": "", --
        },
        "do-not-adopt": False, If true return 0
        "Previous Pets": [{ ++ 
            'name': '', info 
            'breed':'', info 
            'sprayed': False, ++ 
            'age': 0, higher is better   < 4 --, > 4 ++ 
            'years owned': 0,  higher is better  < 4 --, > 4 ++ 
        }],
        "vetInfo": {
            'currentVet': '', if true ++ 
            'emergencyVet':'' if true ++ 
        },
        "criminal record": False, large --
        "Employment": {
            'employer': '', 
            'occupation': '', 
            'lengthOfStay': 0, ++ 
        },
"""



AnimalType = inData[0]["Current Animals"][0]["name"]

print (AnimalType)
"""
homeStatus= db.StringField()

previousSprayed = db.BooleanField
age = db.IntField()
planToMove=db.StringField()
currentVet = db.StringField()

emergencyVet = db.StringField()

doNotAdopt = db.BooleanField()

criminalRecord = db.StringField()

lengthOfStay = db.IntField()

score = 50 

w1 = 2
w2 =  5
w3 = 10
w4 = 10
w5 = 10
w6 = 8


if AnimalType == "dog":
    if homeType == "appartment":
        score = score - w1

if homeStatus == "own":
    score = score + w2
else:
    score = score - w2

if previousSprayed == true: 
    score = score + w4
if age > 4:
    score = score + (age - 4)
else: 
    score = score - (4-age)

 
if (currentVet):
    score = score + w4

if (emergencyVet):
    score = score + w5
if (planToMove):
    score = score - w6
score = score + lengthOfStay

if "do-not-adopt" == true:
    score = 0

if "criminal record" == true:
    score = 0


#output Score
#print score 
#return score


#print(mongoDB.adopters.find())
"""