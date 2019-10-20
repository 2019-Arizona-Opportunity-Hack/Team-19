
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

data = mongoDB.adopterData.find()

a = [a for a in data]
# for a in data: 
#     #print(a)
# print(a)

def deArrayfy(arr):
    for i in arr:
        temp = i
    return i
# inData = deArrayfy(a)
# inData = a[2]
# print("\nRecord 1 \n")
# print(inData)

def scoring(index):
    inData = a[index]

    AnimalType = inData["AnimalType"]

    print (AnimalType)

    homeStatus= inData["homeStatus"]
    homeType= inData["homeType"]
    previousSprayed = inData["sprayed"]
    age = inData["years owned"]
    planToMove=inData["planToMove"]
    currentVet = inData["vetInfo"]["currentVet"]
    emergencyVet = inData["vetInfo"]["currentVet"]
    doNotAdopt = inData["do-not-adopt"]
    criminalRecord = inData["criminal record"]
    lengthOfStay = inData["lengthOfStay"]

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
    if (previousSprayed): 
        score = score + w4
    else:
        score = score - w4/2
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
    if ("do-not-adopt"==True):
        print("do not adopt list")
        score = 0
    if ("criminal record"==True):
        print("there is a criminal record")
        score = 0
    #output Score
    print (score)
    if (score > 80):
        print("This is a very good canadate for adoption")
    elif(50 <= score <= 80):  
        print("this may be a good canatate for adoption")
    elif(25 <= score < 50):
        print("this is not a good canadate for adoption")
    elif(score < 25):
        print("this is a very bad canadate for adoption")
    #return score
ind = 0
for i in a: 
  #    ind = ind +1
    scoring(ind)
    ind = ind +1

scoring(4)
#print(mongoDB.adopters.find())

