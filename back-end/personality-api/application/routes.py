from application import app
from flask import Flask, request, render_template, url_for
import random 

#letter route 

@app.route("personlity/", methods=['GET'])
def personality():
     characteristics = random.choice([("Anticipative", "Brave", "Curious"),("Decisive", "Emotive","Funny" ,"Grounded"),("Home-Bound", "Intelligent", "Jolly", "Knightly"),("Loud", "Melachonly", "Naughty",  "Optimistic", "Patient"),("Quiet", "Restless", "Sad", "Tainted"),("Upright", "Versatile", "Worldly"),("Xenial", "Youthful","Zazzy")])
     return Response (characteristics)