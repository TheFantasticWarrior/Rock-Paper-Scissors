# Rock Paper Scissors with genetic algorithm
branch main is the first attempt without much AI knowledge with human interface

branch genetic algorithm attempts to contain all children in 1 bot, follows the rule more but less effective

this branch runs all bots separately and modify the genes after match ends, more effective as bot1 will react differently to each individual

c and c2 is the same but separated the file to reduce human error switching between evaling and training  
`IO2.py` and `dllu.py` are top 2 bots from rpscontest.com leaderboard
## Usage
bot1 is the filename of the opponent  
n is how many children you want in the population  
`-m x` to specify x matches  

### start with randomized population  
`python genetic.py bot1.py c+n.py`

### continue with previous training  
`python genetic.py bot1.py c*n.py`

### evaluate result  
manually copy the genes you want to c2.py  
`python rpsrunner2.py bot1.py c2.py`