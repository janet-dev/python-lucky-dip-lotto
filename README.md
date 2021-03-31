# python-lucky-dip-lotto
Simulation of a continuous weekly lucky dip lottery<br>
https://github.com/janet-dev/python-lucky-dip-lotto
<br>

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

Comments from a reviewer - thank you Rabia
------------------------------------------
Looks great JanetD. Very well done. Great comments and can follow the logic of your code well. I especially like the bit which warns the user about the times they have played and the money they have spent.
Just the tiniest change I would suggest is display that message not only on if play != 'y': but by checking if the player has not won anything say after x amount of goes so they don't carry on playing.
Also on line 58, Instead of 'Go to', I would just say 'Run the function', because that's what Python is actually doing.
Have a great rest of the weekend.
P.S I didn't win anything after 7 goes
