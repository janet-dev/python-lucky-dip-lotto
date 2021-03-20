# python-lucky-dip-lotto
Simulation of a continuous weekly lucky dip lottery

Created using PyCharm 2020.3.3 (Community Edition)

Program simulates a continuous weekly lucky dip lottery. [UK lottery uses numbers 0-59]
Each play represents one ticket bought per week.

The program has a list of seven numbers that represent a lottery ticket.
It generates two sets of seven random numbers on each run:
- the official draw ticket
- your ticket

After comparing the two sets of numbers for that week,
the program outputs a prize based on the number of matches:<br>
● £20 for three matching numbers<br>
● £40 for four matching numbers<br>
● £100 for five matching numbers<br>
● £10000 for six matching numbers<br>
● £1,000,000 for seven matching numbers<br><br>
Program then asks (y/n), if you wish to play again for another week.
This is similar to an continuous online Lotto Entry by Direct Debit;
to stop playing enter anything other than 'y'.

Each ticket costs £2 and running total for how much you spent over the simulated weeks,
against how much you have won.

https://www.begambleaware.org/
