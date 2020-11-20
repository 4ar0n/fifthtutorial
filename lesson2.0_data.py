person_db = [
                ["Name","Sex","Age","Strength"],
                ["Aaron",False,28,["Basketball","100m","Teaching Competition"]],
                ["Twiggy",True,29,["Mahjong","Nothing at all"]],
                ["Billy",False,31,["Scam","etoro"]],
                ["Jason",False,33,["Butterfly Stroke"]],
            ]
# # Billy is a Male, he is 31, and he has 2 strength(s), they are scam and etoro.
def get_sex(value):
    if value == True:
        return ["female","she"]
    else:
        return ["male","he"]

# # ("%s is a %s, %s is %s, %s has %s strength,)
person_db.pop(0)

for person in person_db:
    name = person[0]
    gender = get_sex(person[1])  
    sex = gender[0]
    pronoun = gender[1]



    age = person[2]
    strengths = person[3]
    num_of_person = len(strengths)
    first_part = "%s is a %s, %s is %s, %s has %s strength(s), they are "%(name,sex,pronoun,age,pronoun,num_of_person)
    second_part = ""
    for strength in strengths:
        second_part+=strength
        second_part+=" and "
    second_part=second_part[0:-5]
    second_part+="."
    statement = first_part + second_part

    print (statement)






