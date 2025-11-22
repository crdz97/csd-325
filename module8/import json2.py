import json 

FILENAME = "students.json"
#Print Class List
def print_students(student_list):
    for s in student_list:
        print(f"{s['L_Name']}, {s['F_Name']} :"
              f" ID = {s['Student_ID']} , Email = {s['Email']}")
    print()

#Load JSON file into a python list using json.load() "r+" -read and write mode
with open(FILENAME, "r+") as f:
    data = json.load(f)

if not isinstance(data, list):
    raise TypeError("JSON file is not a list")

#Print original student list
print("===== Original Student List =====")    
print_students(data)

#Append new student dictionary to the list
data.append({
    "F_Name": "Carolina",
    "L_Name": "Rodriguez",
    "Student_ID": "9001018",
    "Email": "crodriguez1@example.com" 
})

#Print updated student list
print("===== Updated Student List =====")
print_students(data)

#Save updated list back to JSON file using json.dump()-writes file
with open(FILENAME, "w") as f:
    json.dump(data, f, indent=4) #indent for pretty printing

print("Student added successfully.")