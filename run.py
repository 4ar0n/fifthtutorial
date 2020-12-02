
from pprint import pprint

                        
good_list = ["banana","apple","melon", "orange"]

wisdom = 1000

students = {"ka":[] , "ja":[]}

for student , list in students.items():
    students[student] = wisdom
    # list = good_list

students["ja"] -= 20
pprint (students)



