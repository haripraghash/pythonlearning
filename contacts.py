# Example to loop through a dictionary containing another dictionary

contacts = {
    "number":4,
    "students":[
        {"name": "Harry", "email":"harry@hogwats.com"},
        {"name": "Hermione", "email":"hermione@hogwats.com"},
        {"name": "Ron", "email":"ron@hogwats.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])