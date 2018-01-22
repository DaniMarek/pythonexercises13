# Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings.
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(name, animal):
  new_dict = zip(name, animal)
  print new_dict

make_dict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])

#   Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

def make_dict(name, animal):
  new_dict = zip(animal, name)
  print new_dict
  
make_dict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])