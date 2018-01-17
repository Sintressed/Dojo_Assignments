name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict():
    #name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
    #name = dict(name)
    #favorite_animal = dict(favorite_animal)
    new_dict = {}
    for val in name:
        new_dict.update(val)
        print name.items()

make_dict()