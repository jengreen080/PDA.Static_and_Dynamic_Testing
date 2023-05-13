

dictionary_of_animals = {"elephant" : 3,
                        "monkey" : 12,
                        "lion": 2,
                        "tiger" : 2, 
                        "alligator" : 4}

def add_type_of_animal(animal):
    return dictionary_of_animals.update(animal)
print(dictionary_of_animals)

add_type_of_animal({"giraffe" : 5})

print(dictionary_of_animals)

