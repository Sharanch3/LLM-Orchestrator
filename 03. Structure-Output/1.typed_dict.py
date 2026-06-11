from typing import TypedDict

class Person(TypedDict):
    name : str
    age: int
    

new_person : Person = {'name': "Nitish", 'age':'24'}

print(new_person)

