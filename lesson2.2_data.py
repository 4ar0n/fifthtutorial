from pprint import pprint

person_db = {
            "Aaron":{ "Sex":False, "Age":28 , "Strength":["Basketball","100m","Teaching Competition"]},
            "Twiggy":{ "Sex":True, "Age":29 , "Strength":["Mahjong","Nothing at all"]},
            "Billy":{ "Sex":False, "Age":31 , "Strength":["Scam","etoro"] },
            "Jason":{ "Sex":False, "Age":33 , "Strength":["Butterfly Stroke", "1+1-you" ]},

        }

# print ( person_db["Aaron"]["Age"] )
for person,info in person_db.items():
    print (person_db[person]["Age"])
    if person_db[person]["Age"] > 30:
        person_db[person]["Maturity"] = "Old"
    else:
        person_db[person]["Maturity"] = "Young"

print (person_db)



