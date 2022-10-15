def time_pass(text):  # to print and wait for 2s
    import time
    print(text)
    time.sleep(2)


def entro(place):  # to random from my list to entro function
    import random
    place_luck = random.choice(place)
    time_pass("when you was follow a monky, you lost\n" "you search in the " +
              place_luck + "!")


def try_again():
    # this function ask the player to play again
    playQ = input("Do you want to play again? (y/n)\n")
    if playQ == "y":
        time_pass("you start a new game!")
        game_runner()
    if playQ == "n":
        time_pass("Thank you for playing!")
    if playQ != "y" and playQ != "n":
        try_again()


def secound_discion():
    # choose from input and if input don't right run the function again
    adescion2 = input("you must do something \n"
                      " 1.You have to run faster\n"
                      " 2.you scream to make a sound"
                      " that your father will hear you\n")
    if adescion2 == "1":
        time_pass("Game over!\n"
                  "you have been eaten becouse the animal faster than you\n")
    if adescion2 == "2":
        time_pass("Congratulations "
                  "Your dad come and scare the animal "
                  "and the animal run away\n")
    if adescion2 != "2" and adescion2 != "1":
        secound_discion()


def choose_number():
    # choose from input and if input don't right run the function again
    choose_now = input("enter 1 to kill the animal with your weapon\n"
                       "enter 2 to run and try to escape from the animal\n")
    if choose_now == "1":
        time_pass("Congratulations You have killed the animal "
                  "but you must go home before more animals come")
    if choose_now == "2":
        secound_discion()
    if choose_now != "2" and choose_now != "1":
        choose_number()


def descion(weapon, animal):
    # random weapon and animal and run choose_now function
    import random
    weapon_luck = random.choice(weapon)
    animal_luck = random.choice(animal)
    time_pass("you found a " + weapon_luck + "!")
    time_pass("a hungry " + animal_luck + " attack you!")
    choose_number()


def game_runner():  # run all codes from this function
    entro(["forst", "desert"])
    descion(["gun", "sword"], ["wolf", "lion"])
    try_again()


game_runner()  # finally run our code
