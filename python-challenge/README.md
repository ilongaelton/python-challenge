# Python Challenge

## PyBank Script

### Input File

The input file for the PyBank script is located at `Starter_Code/PyBank/Resources/budget_data.csv`. This CSV file contains the following columns:
- Date
- Profit/Losses

### Output File

The output file is generated at `Starter_Code/PyBank/analysis/budget_analysis.txt`. This file contains the results of the financial analysis.

### Script Details

The script performs the following tasks:
1. Reads the CSV file containing the financial data.
2. Calculates the total number of months included in the dataset.
3. Calculates the net total amount of "Profit/Losses" over the entire period.
4. Calculates the average change in "Profit/Losses" between months over the entire period.
5. Identifies the greatest increase in profits (date and amount) over the entire period.
6. Identifies the greatest decrease in losses (date and amount) over the entire period.
7. Prints the analysis to the terminal.
8. Exports the analysis to a text file.

### How to Run

1. Ensure you have Python installed on your machine.
2. Navigate to the `Starter_Code/PyBank` directory.
3. Run the script using the following command:
    ```sh
    python PyBank_starter.py
    ```

### Example Output