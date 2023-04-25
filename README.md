# Nba Game Analysis App

## Task
The task was to write a program that analyzes the flow of data recorded during a NBA game and present the result in specific format.

## Description
The solution of the problem consisted of several steps:
1. Fetching the data from `.txt` file
2. Search for the key words in the 'Description' section using regular expressions
3. Using separate functions for different categories of NBA stats
4. Formatting the output using `.format()` function

## Installation
Download the `my_nba_game_analysis.py` file

## Usage
Example of usage:
```
python my_nba_game_analysis.py
Input the name of file to analyze (without quotes): nba_game_blazers_lakers_20181018.txt
```

## Example Output
```
TEAM NAME:  LOS_ANGELES_LAKERS
Players              FG       FGA      FG%      3P       3PA      3P%      FT       FTA     FT%      ORB      DRB      TRB      AST      STL      BLK      TOV      PF       PTS     
J. McGee             5        6        0.833    0        0                 3        4       0.750    3        5        8        1        1        3        0        0        13      
B. Ingram            7        15       0.467    0        4        0.000    2        4       0.500    1        3        4        1        2        1        1        0        16      
R. Rondo             6        13       0.462    1        2        0.500    0        0                0        4        4        11       1        0        3        0        13      
L. James             9        16       0.562    0        4        0.000    8        9       0.889    2        10       12       6        1        0        6        0        26      
Shooting foul        0        0                 0        0                 0        0                0        0        0        0        0        0        0        9        0       
Personal foul        0        0                 0        0                 0        0                0        0        0        0        0        0        0        14       0       
K. Kuzma             5        15       0.333    1        7        0.143    4        5       0.800    0        5        5        0        1        0        1        0        15      
J. Hart              8        12       0.667    3        5        0.600    1        3       0.333    0        4        4        1        3        2        2        0        20      
L. Stephenson        2        6        0.333    0        3        0.000    0        0                0        2        2        2        0        0        1        0        4       
M. Beasley           0        0                 0        0                 0        0                0        1        1        0        0        0        0        0        0       
L. Ball              2        7        0.286    1        4        0.250    2        2       1.000    2        2        4        1        1        0        1        0        7       
Loose ball foul      0        0                 0        0                 0        0                0        0        0        0        0        0        0        3        0       
K. Caldwell-Pope     1        3        0.333    1        1        1.000    2        2       1.000    0        2        2        0        0        0        0        0        5       
Team Totals          45       93       0.484    7        30       0.233    22       29      0.759    8        38       46       23       10       6        15       26       119     

TEAM NAME:  PORTLAND_TRAIL_BLAZERS
Players              FG       FGA      FG%      3P       3PA      3P%      FT       FTA     FT%      ORB      DRB      TRB      AST      STL      BLK      TOV      PF       PTS     
A. Aminu             1        10       0.100    0        6        0.000    3        4       0.750    0        6        6        0        1        0        1        0        5       
D. Lillard           9        21       0.429    2        7        0.286    8        8       1.000    1        5        6        4        1        1        3        0        28      
J. Layman            1        4        0.250    1        4        0.250    0        0                0        2        2        0        1        0        1        0        3       
J. Nurkić            7        14       0.500    0        1        0.000    2        2       1.000    6        3        9        0        2        0        2        0        16      
C. McCollum          6        17       0.353    3        6        0.500    6        6       1.000    1        4        5        1        0        0        2        0        21      
Personal foul        0        0                 0        0                 0        0                0        0        0        0        0        0        0        8        0       
Offensive foul       0        0                 0        0                 0        0                0        0        0        0        0        0        0        5        0       
Shooting foul        0        0                 0        0                 0        0                0        0        0        0        0        0        0        13       0       
E. Turner            5        8        0.625    0        0                 3        4       0.750    1        2        3        6        2        0        3        0        13      
M. Harkless          3        5        0.600    1        2        0.500    0        0                2        4        6        2        0        3        1        0        7       
Z. Collins           3        4        0.750    0        1        0.000    0        0                1        5        6        2        0        6        1        0        6       
S. Curry             2        6        0.333    1        2        0.500    0        0                1        4        5        0        0        0        1        0        5       
M. Leonard           0        0                 0        0                 0        0                1        3        4        4        1        0        1        0        0       
N. Stauskas          7        11       0.636    5        8        0.625    5        5       1.000    0        2        2        2        1        0        0        0        24      
Team Totals          44       100      0.440    13       37       0.351    27       29      0.931    14       40       54       21       9        10       16       26       128  
```
