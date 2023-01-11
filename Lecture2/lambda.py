people = [
    {"name": "Harry", "house":"Gryffibdor"},
    {"name": "Ron", "house":"Ravenclaw"},
    {"name": "Hermione", "house":"Gryffibdor"}
]

# def f(person):
#     return person["house"]

people.sort(key=lambda person: person["house"])

print(people)