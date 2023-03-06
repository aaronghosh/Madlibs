print("Welcome to the Pirate Madlibs Game!")

# Get user inputs
name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
place = input("Enter a place: ")
body_part = input("Enter a body part: ")

# Print the story with user inputs
print("----------------------------------")
print("Once upon a time, there was a boy named " + name + ".")
print(name + " dreamed of becoming the " + adjective1 + " pirate king, and sailing the " + adjective2 + " seas.")
print("He spent years building his ship, the " + noun1 + ", and gathering a crew of " + noun2 + "s.")
print("Finally, the day came when " + name + " set sail to " + place + ", with his eyes set on the horizon.")
print("As the ship sailed on, " + name + " couldn't help but feel a thrill in every " + body_part + ".")
print("He knew that adventure and danger awaited him, but he was ready to " + verb1 + " his way through any obstacle.")
print("And so, " + name + " and his crew " + verb2 + "ed off into the unknown, determined to make their mark on the world.")
print("Thanks for playing Pirate Madlibs! We hope you enjoyed the adventure.")
