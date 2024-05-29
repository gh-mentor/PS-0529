"""
Python 3.x application using the pandas library to generate random data points and save them in a CSV file.

This script first generates 20 random data points. It then creates a pandas DataFrame from this data. Finally, it saves the DataFrame to a CSV file named 'sample_data.csv'. 
"""

# Import the required libraries
import pandas as pd
import numpy as np
import random

def generate_sample_data(size):
    # Generate sample data using list comprehension
    data = [[random.randint(0, 100), random.randint(0, 100)] for _ in range(size)]

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=['x', 'y'])
    
    return df

# Call the function with the desired size
df = generate_sample_data(20)

# Save the DataFrame to a CSV file
df.to_csv('sample_data.csv', index=False)

print('Data saved to sample_data.csv')