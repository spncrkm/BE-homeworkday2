# problem #1 task 1 The adventure game
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


# task 2
place = input("Choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action_two = input("Do you want to 'light a torch' or 'proceed in the dark'")
    if action_two == "light a torch":
        print("You've discovered a mysterious path!")
    else:
        print("You find a hidden treasure!")

# task 3
place = input("Choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action_two = input("Do you want to 'light a torch' or 'proceed in the dark'")
    if action_two == "light a torch":
        print("You've discovered a mysterious path!")
    elif action_two == "proceed in the dark":
        print("You found the hidden treasure")
    else:
        pass    # instruct user to type in valid answer


# problem #2 Task 1
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2
audio_system = "You want a bigger audio system" if attendees > 100 else "Would you like a projector to use?"
print(audio_system)

# Task 3
food_choice = input("Would you like vegetarian food? yes or no  ")
if food_choice == "yes":
    print("We have Veggie Delight Caterers")
else:
    print("We have Gourmet Meals Caterers.")