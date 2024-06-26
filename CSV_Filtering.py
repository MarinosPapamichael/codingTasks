import csv
from datetime import datetime

def read_csv_to_dict(file_path):
    """
    Reads a CSV file into a list of dictionaries.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - list of dict: List containing dictionaries where each dictionary represents a row in the CSV.
    """
    data = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except csv.Error as e:
        print(f"Error reading CSV file '{file_path}': {e}")
    
    return data

def is_numerical_column(data, column_name, threshold=0.9):
    """
    Checks if a column is numerical based on its data type.

    Args:
    - data (list of dict): Data read from CSV.
    - column_name (str): Name of the column to check.
    - threshold (float): Threshold ratio of numerical values required to consider the column numerical.

    Returns:
    - bool: True if the column is numerical, False otherwise.
    """
    try:
        numerical_count = 0
        total_count = len(data)
        
        for row in data:
            value = row[column_name].strip()
            try:
                float(value)
                numerical_count += 1
            except ValueError:
                continue
        
        if numerical_count / total_count >= threshold:
            return True
        else:
            return False
    
    except Exception as e:
        print(f"Error checking column '{column_name}': {e}")
        return False

def is_date_column(data, column_name, date_format='%Y-%m-%d'):
    """
    Checks if a column is a date column based on its data type.

    Args:
    - data (list of dict): Data read from CSV.
    - column_name (str): Name of the column to check.
    - date_format (str): Format of the date string.

    Returns:
    - bool: True if the column is a date column, False otherwise.
    """
    try:
        for row in data:
            value = row[column_name].strip()
            if value:
                datetime.strptime(value, date_format)
                return True
            else:
                continue
        
        return False
    
    except ValueError:
        return False
    except Exception as e:
        print(f"Error checking column '{column_name}': {e}")
        return False

def display_and_choose_columns(data, csv_file_path):
    """
    Displays column names from CSV and prompts user for column selection and filtering options.

    Args:
    - data (list of dict): Data read from CSV.
    - csv_file_path (str): Path to the CSV file.

    Returns:
    - tuple: (list of str, dict, str, str) Selected filter columns, filter options dictionary, sorting column name, sorting order ('asc' or 'desc').
    """
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        print("Here are the column names in your dataset:")
        for i, column in enumerate(header):
            print(f"{i + 1}. {column}")
        
        selected_columns = input("Please enter the column numbers you want to filter on, separated by commas: ")
        sorting_column = input("Please enter the column number you want to sort your data on: ")
        sorting_order = input("Please enter the sorting order ('asc' for ascending, 'desc' for descending): ").lower()
        selected_columns = [int(i) - 1 for i in selected_columns.split(",")]
        
        filter_columns = [header[i] for i in selected_columns]
        sorting_column = int(sorting_column) - 1
        sorting_column_name = header[sorting_column]  # Ensure this is the column name, not index
        
        print("\nYou have chosen to filter on the following columns:")
        for column in filter_columns:
            print(column)
        
        filter_options = {}
        
        for column in filter_columns:
            if is_numerical_column(data, column):
                print(f"Enter the filter range for '{column}':")
                while True:
                    try:
                        min_value = float(input(f"Minimum value for '{column}': ").strip())
                        max_value = float(input(f"Maximum value for '{column}': ").strip())
                        filter_options[column] = (min_value, max_value)
                        break
                    except ValueError:
                        print("Please enter valid numeric values.")
                
            elif is_date_column(data, column):
                print(f"Enter the filter range for '{column}' (date format YYYY-MM-DD):")
                while True:
                    try:
                        start_date = datetime.strptime(input(f"Start date for '{column}': ").strip(), '%Y-%m-%d')
                        end_date = datetime.strptime(input(f"End date for '{column}': ").strip(), '%Y-%m-%d')
                        filter_options[column] = (start_date, end_date)
                        break
                    except ValueError:
                        print("Please enter valid date values in YYYY-MM-DD format.")
            
            else:  # Categorical column
                show_unique_values = input(f"Do you want to see unique values for '{column}'? (yes/no): ").strip().lower() == 'yes'
                
                if show_unique_values:
                    unique_values = set(row[column] for row in data)
                    print(f"Unique values for '{column}': {', '.join(unique_values)}")
                
                selected_values = input(f"Enter the categorical values to filter on for '{column}', separated by commas: ").strip().split(",")
                filter_options[column] = [value.strip() for value in selected_values]
        
        print("\nYou have chosen to sort on the following column:")
        print(sorting_column_name)
        print(f"Sorting order: {sorting_order}")

        return filter_columns, filter_options, sorting_column_name, sorting_order

def filter_and_sort_data(data, filter_columns, filter_options, sorting_column, sorting_order):
    """
    Filters and sorts data based on user-selected columns and filtering options.

    Args:
    - data (list of dict): Data to filter and sort.
    - filter_columns (list of str): Columns to filter on.
    - filter_options (dict): Dictionary of filter options for each column.
    - sorting_column (str): Column to sort data on.
    - sorting_order (str): Sorting order ('asc' or 'desc').

    Returns:
    - list of dict: Filtered and sorted data.
    """
    filtered_data = data
    
    # Apply filters
    for column in filter_columns:
        if column in filter_options:
            if is_numerical_column(data, column):
                min_value, max_value = filter_options[column]
                filtered_data = [row for row in filtered_data if row[column].strip() and min_value <= float(row[column].strip()) <= max_value]
            elif is_date_column(data, column):
                start_date, end_date = filter_options[column]
                filtered_data = [row for row in filtered_data if row[column].strip() and start_date <= datetime.strptime(row[column].strip(), '%Y-%m-%d') <= end_date]
            else:  # Categorical column
                selected_values = filter_options[column]
                filtered_data = [row for row in filtered_data if row[column].strip() in selected_values]
    
    # Sort filtered data based on sorting column and order
    if sorting_order == 'asc':
        filtered_data.sort(key=lambda x: x[sorting_column])
    elif sorting_order == 'desc':
        filtered_data.sort(key=lambda x: x[sorting_column], reverse=True)
    else:
        print(f"Unknown sorting order '{sorting_order}'. Defaulting to ascending.")
        filtered_data.sort(key=lambda x: x[sorting_column])
    
    return filtered_data

def write_to_csv(data, output_file):
    """
    Writes data to a CSV file.

    Args:
    - data (list of dict): Data to be written to the CSV file.
    - output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Filtered data has been successfully written to '{output_file}'.")
    except Exception as e:
        print(f"Error writing to '{output_file}': {e}")

# Example usage
if __name__ == "__main__":
    file = input("Please enter the name of the CSV file: ")
    data = read_csv_to_dict(file)
    
    if data:
        filter_columns, filter_options, sorting_column, sorting_order = display_and_choose_columns(data, file)
        filtered_data = filter_and_sort_data(data, filter_columns, filter_options, sorting_column, sorting_order)
        
        print(f"\nTotal records read: {len(data)}")
        print(f"Filtered and sorted records: {len(filtered_data)}")
        
        for row in filtered_data:
            print(row)
        
        output_file = input("Enter the name for the output CSV file: ") + ".csv"
        write_to_csv(filtered_data, output_file)
    else:
        print("No data found or error occurred while reading the CSV file.")
