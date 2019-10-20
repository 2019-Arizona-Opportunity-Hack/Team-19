from ws import mongoDB, app
from flask import render_template

@app.route("/adopters")
def adopters(): 
    mongoDB.adopters.insert_one({
        "name": " ", 
        " aliases": [],
        "Current Animals": [{
            'Name': '',
            'Breed': '', 
            'Sprayed/nutered': False, 
            'Age': 0, 
            'Last year Vaccinated': 0
            }],
        "over18HouseholdMembers": [{
            'name': '',
            'age': 0,
            'relationship': "",
        }],
        "under18HouseholdMembers": [{
            'name': '',
            'age': 0, 
            'relationship': '',
        }],
        "Housing":{
            'homeType':'',
            'homeStatus':'',
            'petDeposit': 0,
            'addationalPetRent': 0,
            'rentalRestriction': '',
            'landlord': '',
            'landLordPhone': '', 
            'houseFeatures': {
                'pool': False,
                'Doggie Door': False,
                'fencedYard': False,
            },
            "planToMove": "",
            "planIfMove!AllowPets": "",
            "animalOutside": "",
            "visitingAnimals": "",
            "visitingAnimalsType": "",
            "vistiingChildren": "",
            "childrenAgeAndFrequency": "",
        },
        "do-not-adopt": False,
        "Social Media Accounts": {
            "facebook": "",
            "Twitter": "",
            "linkedIn": ""
        }, 
        "Previous Pets": [{
            'name': '',
            'breed':'',
            'sprayed': False,
            'age': 0,
            'years owned': 0,
        }],
        "vetInfo": {
            'currentVet': '',
            'emergencyVet':''
        },
        "otherPetInfo":{
        },
        "criminal record": False,
        "Finances": {},
        "Employment": {
            'employer': '',
            'occupation': '',
            'previous employer':'',
            'previous occupation': ''
        },
        "score": 0,
    })
    return render_template(
        'index.html',
        title='Adopter test')
    