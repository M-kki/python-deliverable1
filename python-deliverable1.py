import math
print("Welcome to Mini Golf")

username = input("What is your name? ")

game_option = input(f"Hi {username} would you like to play 3 or 6 holes today?")

list_of_holes = ["Hole 1", "Hole 2", "Hole 3", "Hole 4", "Hole 5", "Hole 6"]

if game_option == "3":
    holeone = input(f"What is your score for {list_of_holes[0]}? (Par is 3) ")

    holetwo = input(f"What is your score for {list_of_holes[1]}? (Par is 3) ")

    holethree = input(f"What is your score for {list_of_holes[2]}? (Par is 3) ")

    holeone = int(holeone)
    holetwo = int(holetwo)
    holethree = int(holethree)

    par = 3

    holeone_score = holeone - par
    holetwo_score = holetwo - par
    holethree_score = holethree - par

    holeone_score = math.ceil(holeone_score)
    holetwo_score = math.ceil(holetwo_score)
    holethree_score = math.ceil(holethree_score)

    total_stroke = holeone_score + holetwo_score + holethree_score

    total_par = 9

    total_score = total_par - total_stroke

    if total_score < 0:

        print(f"Nice try, {username}... Your total par was: +({total_score})")

    elif total_score > 0:

        print(f"Great job {username}! Your total par was: -({total_score})")

    elif total_score == 0:

        print(f"Good game {username}, Your total par was: {total_score}!")

elif game_option == "6":
    holeone = input(f"What is your score for {list_of_holes[0]}? (Par is 3) ")

    holetwo = input(f"What is your score for {list_of_holes[1]}? (Par is 3) ")

    holethree = input(f"What is your score for {list_of_holes[2]}? (Par is 3) ")

    holefour = input(f"What is your score for {list_of_holes[3]}? (Par is 3) ")

    holefive = input(f"What is your score for {list_of_holes[4]}? (Par is 3) ")

    holesix = input(f"What is your score for {list_of_holes[5]}? (Par is 3) ")

    holeone = int(holeone)
    holetwo = int(holetwo)
    holethree = int(holethree)
    holefour = int(holefour)
    holefive = int(holefive)
    holesix = int(holesix)

    holeone_score = holeone
    holetwo_score = holetwo
    holethree_score = holethree
    holefour_score = holefour
    holefive_score = holefive
    holesix_score = holesix

    holeone_score = math.ceil(holeone_score)
    holetwo_score = math.ceil(holetwo_score)
    holethree_score = math.ceil(holethree_score)
    holefour_score = math.ceil(holefour_score)
    holefive_score = math.ceil(holefive_score)
    holesix_score = math.ceil(holesix_score)

    total_stroke = holeone_score + holetwo_score + holethree_score + holefour_score + holefive_score + holesix_score

    total_par = 18

    total_score = total_par - total_stroke

    if total_score < 0:

        print(f"Nice try, {username}... Your total par was: +({total_score})")

    elif total_score > 0:

        print(f"Great job {username}! Your total par was: -({total_score})")

    elif total_score == 0:

        print(f"Good game {username}, Your total par was: {total_score}!")
else:
    print("Please enter 3 or 6")
