
# make the game's varibels ready .

# main variables
guesses = 8
guesses_counter = 0
secret_word = "samuel"
user_guesses = ""
# hint variables .
want_a_hint = ""
hint = "samuel"
# make the point counter's variables . 
points = 10

# game main loop .
print("you have { \n 10 points \n 8 guesses \n 1 hint at your 6th try \n \
    [for any try you lose , you will lose a point for] } ")
while secret_word != user_guesses and guesses_counter != guesses :
    
        # make the guesses counter for user .
        user_guesses = input("pleas enter your guess:- ")
        guesses_counter += 1
        Remaining_guesses = ( guesses - guesses_counter )

        # make the hint .
        if guesses_counter == 6:
            want_a_hint = input("if u wanna take a hint say (yes) if not say (no) if you take the hint you will lose 2 points :- ")
            if want_a_hint == "yes" :
                print("secret word is :-" ,hint)
            else:
                print("as you want")
        # make the points conter .
        if want_a_hint != "yes":
            points -= 1
        if want_a_hint == "yes":
            points -= 2
            want_a_hint = "pla pla"
        print("guesses remaining:-",Remaining_guesses)
        print("points remaining :-",points)

# make sure if the user winner or loser .
if guesses_counter == guesses and secret_word != user_guesses:
    print("sorry but you lose")
else:
    print("you win!")
    print("with points:-",points)
    print("& Remaining guesses :-",Remaining_guesses)


