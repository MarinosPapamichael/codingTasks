# CSV Data Filter and Sort

This repository contains a Python script designed to read, filter, and sort CSV data. This script is designed to handle CSV data efficiently by allowing users to filter and sort the data based on specific criteria. It reads a CSV file into a list of dictionaries, providing the flexibility to filter numerical, date, or categorical columns and sort the data accordingly. Learning to manipulate CSV data is crucial for data analysis and processing tasks, as CSV is a common format for storing and exchanging data. Mastering these skills enhances your ability to handle real-world data effectively.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Example](#example)
- [Contributing](#contributing)
- [Author](#author)

## Features

- **Read CSV**: Convert CSV file into a list of dictionaries.
- **Column Type Detection**: Automatically determine if a column is numerical or date.
- **Interactive Filtering**: Prompt the user to select columns and define filters.
- **Sorting**: Sort the filtered data based on user-defined criteria.
- **Output**: Write the filtered and sorted data to a new CSV file.

## Requirements

- Python 3.x
- CSV file for processing

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MarinosPapamichael/codingTasks.git

2. **Navigate to the project directory:**

   ```bash
   cd csv-data-filter-and-sort

## Usage
1. **Run the script:**

   ```bash
   python script.py

2. **Follow the prompts:**

- Enter the name of the CSV file to process.
- Select columns for filtering and sorting.
- Define filter criteria for numerical, date, and categorical columns.
- Specify the sorting order (ascending or descending).
- Provide a name for the output CSV file.

3. **Review the output:**

- The script will output the filtered and sorted data to the specified file.

## Functions

**'read_csv_to_dict(file_path)'**
Reads a CSV file into a list of dictionaries.

**'is_numerical_column(data, column_name, threshold=0.9)'**
Checks if a column is numerical based on its data type.

**'is_date_column(data, column_name, date_format='%Y-%m-%d')'**
Checks if a column is a date column based on its data type.

**'display_and_choose_columns(data, csv_file_path)'**
Displays column names from CSV and prompts user for column selection and filtering options.

**'filter_and_sort_data(data, filter_columns, filter_options, sorting_column, sorting_order)'**
Filters and sorts data based on user-selected columns and filtering options.

**'write_to_csv(data, output_file)'**
Writes data to a CSV file.

## Example

Here is an example of how to use the script with the `Tesla Dataset.csv`:

1. **Run the script:**
   ```bash
   python script.py

2. **Follow the prompts:**

- **Enter the name of the CSV file:** `Tesla Dataset.csv`
- **Please enter the column numbers you want to filter on, separated by commas:** Enter the numbers corresponding to `Date` and `Close`, for example `1, 4` (ensure you replace with actual numbers based on the prompt).
- **Enter the filter range for `Date`:**
  - **Start date:** `2011-01-01`
  - **End date:** `2011-03-01`
- **Enter the filter range for `Close`:**
  - **Minimum value:** `1.5`
  - **Maximum value:** `1.6`
- **Please enter the column number you want to sort your data on:** Enter the number corresponding to `Date`, for example `1` (ensure you replace with actual number based on the prompt).
- **Please enter the sorting order ('asc' for ascending, 'desc' for descending):** `asc`
- **Enter the name for the output CSV file:** `output.csv`

 3. **Review the output:**

- The filtered and sorted data will be saved in the output.csv file in the same directory.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author
Marinos Papamichael - marinos.papamichael1@gmail.com
