"""Restaurant rating lister."""


def process_scores():

    scores_txt = open('scores.txt')

    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)

    return scores


def add_restaurant(scores):

    print("Please add a rating for your favorite restaurant!")
    restaurant = input("Restaurant name> ")
    rating = int(input("Rating> "))

    scores[restaurant] = rating


def print_sorted_scores(scores):

    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")


scores = process_scores()

add_restaurant(scores)

print_sorted_scores(scores)