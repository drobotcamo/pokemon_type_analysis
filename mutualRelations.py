import json

typeRelations = json.load(open('typechart.json'))

for type in typeRelations:
    for attackingType in typeRelations[type]["damageTaken"]:
        if typeRelations[type]["damageTaken"][attackingType] == 2:
            if typeRelations[attackingType]["damageTaken"][type] == 1:
                print(f"{type} and {attackingType} are a proper relation")

# the results of this analysis were interesting. in order to be a part of a perfect cycle, a type must have at lease one proper relation
# and be on the recieving end of a perfect relation. for dark type, it only has one proper edge, and is not on the recieving end of any 
# proper relations. the same goes for psychic and ghost, which are both lacking one of the two. this explains why they didnt show up
# in yesterday's analysis. cool.