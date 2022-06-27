import random
from unittest import result

def process_scores():
            
    i = 0
    scores_dict = {}
    
    f = open("scores.txt", "r")
    for line in f:
        key_value = line.rstrip().split(":")
        print("Key_value: ", key_value)
        scores_dict[key_value[i]] = key_value[i + 1]
    
    return scores_dict

def get_action_choice():
     
     print("What would you like to do?")
     print("    1: See ratings for all restaurants")
     print("    2: Add a new restaurant")
     print("    3: Re-rate a random restaurant")
     print("    4: Re-rate a specific restaurant")
     print("    5: Quit")

     return int(input("> "))


def add_restaurant(scores_dict):

    process_scores()

    restaurant = input("Restaurant name> ")
    score = get_score("Rating> ")
    scores_dict[restaurant] = score


def get_score(prompt):

    while True:
        entry = input(prompt)

        if not entry.isdigit():
            continue

        rating = int(entry)

        if rating >=1 and rating <= 5:
            return rating


def rate_random_restaurant(scores_dict):

    process_scores()

    restaurant, rating = random.choice(scores_dict.items())

    print(f"The current rating for {restaurant} is {rating}.")
    new_rating = get_score(f"What is your rating for {restaurant}? ")

    scores_dict[restaurant] = new_rating


def rate_specific_restaurant(scores_dict):

    print_sorted_scores(scores_dict)

    while True:
        print("\nWhich restaurant would you like to update?")
        print("Please enter the name exactly as it appears above.")
        restaurant = input("> ")

        if restaurant in scores_dict:
            rating = scores_dict[restaurant]
            print(f"The current rating for {restaurant} is {rating}.")
            new_rating = get_score(f"What is your rating for {restaurant}? ")
        else:
            print("That's not one of the restaurants above. Please try again.")

        scores_dict[restaurant] = new_rating


def print_sorted_scores(scores_dict):

    process_scores()

    for restaurant, rating in sorted(scores_dict):
        print(f"{restaurant} is rated at {rating}.")


def main():

    scores_dict = {}
 
    while True:

        action = get_action_choice()

        if action == 1:
            print_sorted_scores(scores_dict)

        elif action == 2:
            add_restaurant(scores_dict)

        elif action == 3:
            rate_random_restaurant(scores_dict)

        elif action == 4:
            rate_specific_restaurant(scores_dict)

        elif action == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.") 


main()  