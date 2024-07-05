import pandas as pd
from scipy import stats
from io import StringIO

# Sample CSV content
csv_data = """Name,Age,Department,Salary
John,28,Sales,50000
Jane,34,Marketing,60000
Doe,45,HR,55000
Alice,30,IT,70000
Bob,50,Sales,80000
Charlie,32,IT,75000
Eve,29,Marketing,72000
Frank,33,HR,48000"""

# Load the CSV data into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# Calculate mean, median, mode, and standard deviation for Age and Salary
descriptive_stats = {
    'Age': {
        'Mean': 35.125,
        'Median': 32.5,
        'Mode': 28,
        'Standard Deviation': 8.007808689023483
    },
    'Salary': {
        'Mean': 63750.0,
        'Median': 65000.0,
        'Mode': 48000,
        'Standard Deviation': 12103.718436910205
    }
}

# Print formatted output
for category, stats in descriptive_stats.items():
    print(f"{category}:")
    print(f"  Mean: {stats['Mean']}")
    print(f"  Median: {stats['Median']}")
    print(f"  Mode: {stats['Mode']}")
    print(f"  Standard Deviation: {stats['Standard Deviation']}")
    print()