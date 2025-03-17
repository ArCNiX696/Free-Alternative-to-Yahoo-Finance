# Free Alternative to Yahoo Finance

## Overview
This repository provides a simple Python script that serves as a free alternative to Yahoo Finance. The script preprocesses stock data obtained from Nasdaq.com by cleaning and formatting the dataset. Key operations include renaming columns, converting data types, sorting dates, and reordering columns. The processed data is then saved to an output folder for further analysis.

First of all you should donwload the dataset from ---> https://www.nasdaq.com/
then save it in input folder of this repository.

This script preprocesses stock data obtained from Nasdaq.com by performing several cleaning and formatting operations:
  - It loads a CSV file using a file dialog.
  - It renames the "Close/Last" column to "Adj Close" and cleans price columns by removing '$' symbols.
  - It optionally converts the "Volume" column from int64 to float64.
  - It optionally sorts the dataset by date in ascending order (oldest date first).
  - It optionally moves the "Adj Close" column to the end of the DataFrame.
  - Finally, it saves the processed dataset to the specified output path.
  
 Adjustable hyperparameters via argparse:
  - --verbose: (int) Controls the level of console output for visualization.
  - --revert_order: (bool) If True, sorts the dataset by date in ascending order.
  - --convert_to_float: (bool) If True, converts the "Volume" column to float64 to avoid future warnings.
  - --move_col: (bool) If True, moves the "Adj Close" column to the end of the DataFrame.
  - --output_path: (str) Specifies the directory where the processed CSV will be saved.

## Requirements
- **Python 3.x**
- **Required Libraries:**
  - [pandas](https://pandas.pydata.org/) – install with `pip install pandas`
  - argparse – (included in the Python standard library)
  - tkinter – (included in the Python standard library)
  - os – (included in the Python standard library)

## Installation
1. **Install Python 3.x** if you haven't already.
2. **Install the required library:**
   ```bash
   pip install pandas





# Free-Alternative-to-Yahoo-Finance
