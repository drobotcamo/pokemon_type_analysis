import json
import time
import requests
from flask import Blueprint, render_template

analyzer = Blueprint('analyzer', __name__)

@analyzer.route("/")
def hello_world():
    return render_template("homepage.html")

typechartFile = open('typechart.json')
typechart = json.load(typechartFile)

dexJSON = requests.get("https://play.pokemonshowdown.com/data/pokedex.json")
dex = dexJSON.json()

type1 = "null"
type2 = "null"
while not type1 in typechart:
    type1 = input("Please enter the primary type to search for:\n")
    type1 = type1.lower()
    type1 = type1.capitalize()
while (not type2 in typechart) and type2 != "None" and type2 != "Any" and type2 != type1:
    type2 = input("""Please enter the secondary type to search for. Enter 'Any' to see all pokemon that have the primary type, 
    and enter 'None' to see pokemon with ***only*** the primary type:\n""")
    type2 = type2.lower()
    type2 = type2.capitalize()

for x in dex:
    currentMon = dex[x]
    if currentMon["types"][0] == type1 and currentMon["num"] > 0 and (type2 == "Any" or (len(currentMon["types"]) == 2 and currentMon["types"][1] == type2) or (len(currentMon["types"]) == 1) and type2 == "None"):
        print(currentMon["name"])

