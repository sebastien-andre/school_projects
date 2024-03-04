# VoteScheme Project

The VoteScheme project comprises two Python scripts designed to process and determine the outcome of elections based on different voting schemes. The first script handles simple vote counting where each vote equals one point for the named candidate, while the second script implements a ranked-choice voting system.

## Scripts Overview

### votescheme1.py

This script reads a file containing names and votes, counts the votes for each candidate, and declares the winner. In the event of a tie, all tied candidates are declared winners.

- **Usage Example:** `python votescheme1.py v1.dat`

### votescheme2.py

Implements ranked voting where each ballot lists candidates in order of preference. The script eliminates candidates with the lowest number of first-choice votes in each round until a single candidate remains or a tie occurs, in which case all remaining candidates are declared winners.

- **Usage Example:**

bash```python votescheme2.py v2.dat```

## Features

- **Simple Vote Counting:** (`votescheme1.py`) Counts direct votes for each candidate and supports multiple winners in case of a tie.
- **Ranked Choice Voting:** (`votescheme2.py`) Processes ballots with ranked preferences, eliminating the lowest-ranking candidates iteratively until a winner is determined or a tie is declared.
- **File Input:** Both scripts take the name of a `.dat` file as a command-line argument, which contains the votes or ranked ballots.

## File Formats

- **v1.dat for votescheme1.py:** Contains one name (vote) per line.
- **v2.dat for votescheme2.py:** Contains comma-separated ranked choices per line, representing a single ballot.

## How It Works

### votescheme1.py

1. Reads votes from a specified file.
2. Tallies votes for each candidate.
3. Declares the candidate(s) with the most votes as winner(s).

### votescheme2.py

1. Reads ranked ballots from a specified file.
2. Counts first-choice votes for each candidate.
3. Eliminates the candidate(s) with the fewest first-choice votes.
4. Repeats the process until a clear winner is found or a tie occurs among the remaining candidates.
