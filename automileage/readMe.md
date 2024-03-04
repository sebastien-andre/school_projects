# Python Date and Auto Mileage Analysis Tools

This repository contains Python scripts for managing and analyzing dates and automobile mileage data. The project is divided into two main parts: a date manipulation tool (`driver.py`) and an automobile mileage analysis tool (`AutoMileageAnalysis.py`). Both tools utilize a custom Date class (`Date.py`) for handling date-specific operations.

## Features

### Date Manipulation (`driver.py`)

The `driver.py` script offers a simple interface for performing various operations with dates, including:

- Adding days to a given date
- Calculating the date of the next day (tomorrow)
- Determining the number of days between two dates
- Comparing two dates to check which one comes before or after the other

### Auto Mileage Analysis (`AutoMileageAnalysis.py`)

The `AutoMileageAnalysis.py` script is designed for analyzing automobile mileage data from a `.dat` file. It provides a detailed breakdown of:

- Money spent on gas
- Gallons of gas filled
- Miles driven between gas fills
- Days between gas fills
- Average miles per gallon (MPG) for each fill-up


## Usage

### Date Manipulation

To use the date manipulation tool, simply run:

```bash
python driver.py
```
### Auto Mileage Analysis

To analyze your automobile mileage data, ensure you have a .dat file formatted similar to the included car1.dat example. Then run:
```bash
python AutoMileageAnalysis.py car.dat
```
