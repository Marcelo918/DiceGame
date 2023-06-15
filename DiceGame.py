'''
Description: This program simulates a dice game. It generates two random dice values between
             1 and 6 for the user, and 2 for the computer. The user gets to roll as many times
             as the user likes, while the computer only rolls once, after the user have decided
             what two dices has liked. 
'''

'''
# ******************************************************************************
# *                               COPYRIGHT NOTICE                             *
# ******************************************************************************
# *                                                                            *
# *  This code is authored by Marcelo Villalobos Diaz                          *
# *  You are free to use, modify, and distribute this code, provided           *
# *  you give appropriate credit by including the author's name.               *
# *                                                                            *
# *  Copyright (c) 2023 Marcelo Villalobos Diaz                                *
# *                                                                            *
# ******************************************************************************
'''

import random
print("Beat the computer!")

play = 'n'

while play == 'n':
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    sumAB = a + b

    print("You rolled a " + str(a) + " and a " +
          str(b) + " (total = " + str(sumAB) + ")")
    play = input("Do you want to keep those? (y or n) ")

    if play == 'n':
        print("Rolling again....")

    c = random.randint(1, 6)
    d = random.randint(1, 6)
    sumCD = c + d

    if play == 'y':
        print("The computer rolled a " + str(c) + " and a " +
              str(d) + " (total = " + str(sumCD) + ")")

        if sumAB == sumCD:
            print("That is a tie!")
        elif sumAB > sumCD:
            print("You win!")
        else:
            print("You lose!")
        break
