# zip() function -> takes two or more lists and returns an object that contains a list of pairs

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

names_and_heights = zip(names, heights)
print(names_and_heights) # Contains the memory location of the object

converted_list = list(names_and_heights) # Convert the object to a list, list contains tuples
print(converted_list)