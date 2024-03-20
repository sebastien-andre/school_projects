# Calendar Display Project

This Python script, `cal.py`, is designed to display the calendar for a specific month and year, provided by the user through command-line arguments.
## Features

- **Custom Calendar Display:** Generates a calendar for any given month and year, displaying it in a traditional format with days aligned under the appropriate weekdays.
- **Command-Line Interface:** Allows users to specify the month and year for the calendar directly through command-line arguments, offering flexibility and ease of use.
- **Error Handling:** Includes basic error handling to catch and print errors, enhancing user experience by providing clear feedback in case of incorrect input.

## Usage

```bash
python cal.py [month] [year]
```

### Example Output

- For example, to display the calendar for April 2003, you would enter:

| Su | Mo | Tu | We | Th | Fr | Sa |
|----|----|----|----|----|----|----|
|    |    |  1 |  2 |  3 |  4 |  5 |
|  6 |  7 |  8 |  9 | 10 | 11 | 12 |
| 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 20 | 21 | 22 | 23 | 24 | 25 | 26 |
| 27 | 28 | 29 | 30 |    |    |    |


## Implementation Details

The script works as follows:

1. It reads the month and year from the command-line arguments.
2. Utilizes the `calendar` module to find out the first weekday of the month and the total number of days in the month.
3. Prints the calendar header, including the month and year centered above the days of the week.
4. Correctly formats and prints each day of the month, aligning days under the appropriate weekday headers.
