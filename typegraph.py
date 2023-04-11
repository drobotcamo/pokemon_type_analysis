# cameron greene december 2022 #
# program that will find perfect 'cycles' of various degrees within the pokemon type effectiveness chart #

import json
import time

SUPER_EFFECTIVE = 1
NOT_VERY_EFFECTIVE = 2
IMMUNE = 3

# store type chart in a dictionary
typeRelations = json.load(open('typechart.json'))

# initialize dictionaries to create the graphs: keys are vertices and values are edges
weaknessesGraph = {}
resistanceGraph = {}

# read the relations, and store the weaknesses and resistances for each type in lists
for selectedType in typeRelations:
    #initialize lists to store edges for each
    weaknessesGraph[selectedType] = []
    resistanceGraph[selectedType] = []

    for attackingType in typeRelations[selectedType]["damageTaken"]:

        if typeRelations[selectedType]["damageTaken"][attackingType] == SUPER_EFFECTIVE:
            weaknessesGraph[selectedType].append(attackingType)

        if typeRelations[selectedType]["damageTaken"][attackingType] == NOT_VERY_EFFECTIVE:
            resistanceGraph[selectedType].append(attackingType)

# now we will loop in order to find some cycles... this is gonna require some thinking.

typeCycle = []  
CYCLE_LENGTH = 3
set_of_cycles = set()

def weaknessFinder(typeCheck, target_length): 

    global typeCycle, startType, set_of_cycles
    target_length -= 1

    for weakness in weaknessesGraph[typeCheck]:

        typeCycle.append(weakness)

        if target_length != 0:
            weaknessFinder(weakness, target_length)
        elif weakness == startType and verify(typeCycle):
            tuple_to_add = tuple(typeCycle)
            set_of_cycles.add(tuple_to_add)

        typeCycle.pop(len(typeCycle) - 1)

def step():
    input()

def verify(cycle):
    global set_of_cycles
    status = True
    for i in range(0, len(cycle) - 1):
        if cycle[i] not in resistanceGraph[cycle[i + 1]]:
            status = False
        if cycle[len(cycle) - 1] not in resistanceGraph[cycle[0]]:
            status = False
    for t in set_of_cycles:
        if cmpT(t, cycle):
            status = False

    return status

def cmpT(t1, t2):
    return sorted(t1) == sorted(t2)    

CYCLE_LENGTH = int(input("Please enter the order of the perfect cycles you'd like to find:\n"))

start_time = time.time()
for startType in typeRelations:
    weaknessFinder(startType, CYCLE_LENGTH)

for cycle in set_of_cycles:
    print(cycle)

end_time = time.time()

print(f"{len(set_of_cycles)} cycles of order {CYCLE_LENGTH} found in {end_time - start_time} seconds")