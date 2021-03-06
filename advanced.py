import random
from unittest import result

def process_scores():
            
    i = 0
    scores_dict = {}
    
    f = open("scores.txt", "r")
    for line in f:
        (restaurant, score) = line.rstrip().split(":")
        scores_dict[restaurant] = int(score)
    
    print(scores_dict)
    return(scores_dict)

def get_action_choice():

     print("What would you like to do?")
     print("    1: See ratings for all restaurants")
     print("    2: Add a new restaurant")
     print("    3: Re-rate a random restaurant")
     print("    4: Re-rate a specific restaurant")
     print("    5: Quit")

     return int(input("> "))


def add_restaurant():

    scores_dict = process_scores()

    restaurant = input("Restaurant name> ")
    score = input("Rating> ")
    scores_dict[restaurant] = score
    return

def get_score(prompt):

    while True:
        entry = input(prompt)

        if not entry.isdigit():
            continue

        rating = int(entry)

        if rating >=1 and rating <= 5:
            return rating


def rate_random_restaurant():

    scores_dict = process_scores()

    restaurant_list = list(scores_dict)

    random_value = random.choice(restaurant_list)
    print(f"The current restaurant is {random_value}")
    new_score = input(f"What is your rating? ")
    scores_dict[random_value] = new_score


def rate_specific_restaurant():

    process_scores()
    scores_dict = process_scores()

    print("\nWhich restaurant would you like to update?")
    print("Please enter the name exactly as it appears above.")
    restaurant = input("> ")

    if restaurant:
       for restaurant in scores_dict.values():
            new_score = input(f"What is your new rating? ")
            scores_dict[restaurant] = new_score
            return
    else:
        print("That's not one of the restaurants above. Please try again.")

def print_sorted_scores():

    scores_dict = process_scores()
    
    restaurant_list = []

    for tuple in scores_dict.items():
        restaurant_list.append(tuple)

    restaurant_list.sort()
    print(restaurant_list)


def main():

    process_scores()
 
    while True:

        action = get_action_choice()
        
        if action == 1:
            print_sorted_scores()

        elif action == 2:
            add_restaurant()

        elif action == 3:
            rate_random_restaurant()

        elif action == 4:
            rate_specific_restaurant()

        elif action == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.") 


main()  