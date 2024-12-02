import json

courses = '{"name": "GeorgeAshraf", "languages": [ "Java", "Python" ]}'

# Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses["name"])   # GeorgeAshraf
print(dict_courses["languages"][0])  # Java
list_languages = dict_courses["languages"]
print(list_languages[0])    # Java

#  Parse content present in json file
with open("course.json") as f:
    data = json.load(f)
    print(type(data))
    print(data)

    print(data["courses"][1]["title"])  # Cypress
    print(data['dashboard']['website']) # rahulshettyacademy.com

# price of course RPA from json file
    print(type(data['courses']))
    for course in data['courses']:
        # print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45

# Compare two json files (previous one and new one added)

with open("course1.json") as f1:
    data2 = json.load(f1)
    assert data == data2
