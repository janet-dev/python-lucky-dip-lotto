"""
Program simulates a weekly luck dip lottery. [UK lottery use numbers 0-59]
The program has a list of seven numbers that represent a lottery ticket.
It generates seven random numbers.
After comparing the two sets of numbers,
the program outputs a prize based on the number of matches:
● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1,000,000 for seven matching numbers

A ticket costs £2
"""
import random


def compare():
    # FUNCTION to compare the 2 tickets

    for each_num in uk_lottery:
        if each_num in your_ticket:
            win_ticket.append(each_num)
            # matching numbers added to new list: win_ticket[]

    # Really want a switch-case here!!
    # Outputting the winning or losing messages using if-elif-else
    if len(win_ticket) == 3:
        print('\nYou WIN £20 for three matching numbers\n')
    elif len(win_ticket) == 4:
        print('\nYou WIN £40 for four matching numbers\n')
    elif len(win_ticket) == 5:
        print('\nYou WIN £100 for five matching numbers\n')
    elif len(win_ticket) == 6:
        print('\nYou WIN £10000 for six matching numbers\n')
    elif len(win_ticket) == 7:
        print('\nYou WIN £1,000,000 for seven matching numbers!\n')
    else:
        print('\nYou win nothing. Try again!\n')

    return win_ticket


# initialise before first play
uk_lottery = []
your_ticket = []
win_ticket = []
tickets = 0
play = 'y'

while True:
    # Generate the tickets.
    # list = random sample of 7 unique numbers, in range 1-59.
    uk_lottery = random.sample(range(1, 59), 7)
    your_ticket = random.sample(range(1, 59), 7)
    # Note: random.randint() function can produce duplicate numbers
    # so used random.sample(range(min, max), samples) instead

    compare()  # Go to the function which compares the tickets
    print('Official UK Lottery Draw is {}'.format(sorted(uk_lottery)))
    print('Your Lucky Dip Ticket is    {}'.format(sorted(your_ticket)))
    print('Your matching numbers are   {}'.format(sorted(win_ticket)))
    tickets += 1  # Keep count of the tickets bought

    # Reset the lottery.
    uk_lottery = []
    your_ticket = []
    win_ticket = []

    # Python version of a do-while loop:
    # Keep playing whilst 'y' is entered but
    # any other character will end the session.
    play = (input('Play again? y/n: '))
    if play != 'y':
        break
        # End play

# A bit of a wake-up call if you buy lottery tickets.
# The odds are stacked against you.
print('You have already played for {} week/s & spent £{}.'.format(tickets, tickets*2))
