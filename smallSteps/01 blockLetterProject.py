# Create ASCII art - displays initials of a name in block letters
# Complete alphabet: https://content.codecademy.com/courses/learn-cpp/hello-world/block-letters-hint.png?_gl=1*1cb6iy*_ga*NTMyMDk0ODM5Ni4xNjgyNjQ5MzM1*_ga_3LRZM6TM9L*MTcwNTY5NzkwMy4xMC4xLjE3MDU2OTg2MzMuMC4wLjA.

# Print "RC" in block letters
initialsR = '''
RRRR
R   R
R   R
RRRR
R R
R  R
R   R
'''
initialsC = '''
 CCC
C   C
C
C
C
C   C
 CCC
'''

print(initialsR+initialsC)

# Alternative
print("RRRR")
print("R   R")
print("R   R")
print("RRRR")
print("R R")
print("R  R")
print("R   R")

print(" CCC")
print("C   C")
print("C")
print("C")
print("C")
print("C   C")
print(" CCC")

# Could automate this with a function to also print other initials depending on input, I'll leave that for when I'm more familiar with Python
