#Rita LaPlante
#Solutions Lab Week 4

#Part 1: For loops
#1. Print out every number between 10 and 100

for i in range (10, 101):
    print(i)

#2. Print out every other number between 10 and 50

for i in range (10, 51, 2):
    print(i)

#3. Do a countdown backwards from 100 to 50

for i in range (100, 49, -1):
    print(i)

#4. Do a countdown backwards from 100 by 7's

for i in range (100, -1, -7):
    print(i)

#Part 2: And, or, if, while
#You are giving out prizes to people based on their age, name, and number of cats.
#People over 18 whose names begin with "E" and people between 25 and 50 whose
#names contain an "a" win a new car. People with more than 5 cats who are over 60
#get a new house

def getsPrize(age, name, numCats):
    if (numCats > 5 and age > 60):
        prize = "You win a house"
    elif (age > 18 and name[0] == "E") or (25 <= age <= 50 and "a" in name.lower()):
        prize = "You win a new car"
    else:
        prize = "No prize"
    return prize

#Question: Why will getsPrize2 print out the wrong prize?
def getsPrize2(age, name, numCats):
    if (age > 18 and name[0] == "E") or (25 <= age <= 50 and "a" in name.lower()):
        prize = "You win a new car"
    elif (numCats > 5 and age > 60):
        prize = "You win a house"
    else:
        prize = "No prize"
    return prize

prize = getsPrize(75, "Edward", 10)
print(prize)

#Nested if statements: Check if a year is a leap year. A leap year is divisible by 4 except
#for century years. The century year is a leap year only if it is perfectly divisible by 400
#Examples:
#   2017 is not a leap year
#   1900 is not a leap year
#   2012 is a leap year
#   2000 is a leap year

year = 2000

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#You want to make the perfect up of tea. In order to this you want to make sure
#your tea is not too hot and your milk is not too cold. While the temperature
#of the tea is above 180 degrees and the milk is below 40 degrees print "Tea
#is not ready". Once the temperature of the milk and tea are correct, print
#"Tea is just right"

tea = 212
milk = 32

while (tea > 180 or milk < 40):
    print("Tea is not ready")
    tea = tea - 1
    milk = milk + 1

print(milk)
print(tea)
print("Tea is just right")

#Part 3: Modules
#1. Print out a random number using random()

import random

print(random.randint(1, 100))

#2. Use the re module with re.sub to replace a character in a word

import re

string = "Rita"
new_string = re.sub("a", "R", string)
print(new_string)


