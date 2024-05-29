"""
This is a Python app which generates a scatter plot of age vs net worth.
Details:
- Uses the numpy library to generate the data and matplotlib to plot the data. 
- Has functions to generate and plot the data.
- The data is generated based on a normal distribution with the probability of having a high net worth increasing with age.
- The data is plotted as a scatter plot with the x-axis representing age and the y-axis representing net worth.
- The plot has a title 'Age vs Net Worth', x-axis label 'Age', and y-axis label 'Net Worth'.
- The x-axis is formatted as an integer.
- The y-axis is formatted as currency with a $ sign and commas.
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

"""
The selected Python code defines a function generate_data() that simulates a dataset of ages and their corresponding net worths.

The function starts by generating an array of ages from 20 to 70 using np.arange(20, 71, 1). This creates an array where each element is an age, starting from 20 and ending at 70, with a step of 1.

Next, it initializes the net_worth array with random values drawn from a normal distribution with a mean of 500,000 and a standard deviation of 200,000. The size of this array is the same as the age array, as specified by len(age).

The function then iterates over the age array using a for loop. For each age, it checks which age range the current age falls into (less than 30, less than 40, and so on). Depending on the age range, it assigns a net worth to the corresponding index in the net_worth array. The net worth is a random value drawn from a normal distribution, with the mean and standard deviation varying based on the age range. For example, if the age is less than 30, the net worth is drawn from a normal distribution with a mean of 300,000 and a standard deviation of 100,000.

Finally, the function returns the age and net_worth arrays. The purpose of this function is to generate a synthetic dataset that might represent the relationship between age and net worth in a population.
"""

def generate_data():
    age = np.arange(20, 71, 1)
    net_worth = np.random.normal(500000, 200000, len(age))

    for i, a in enumerate(age):
        if a < 30:
            net_worth[i] = np.random.normal(300000, 100000)
        elif a < 40:
            net_worth[i] = np.random.normal(400000, 150000)
        elif a < 50:
            net_worth[i] = np.random.normal(600000, 200000)
        elif a < 60:
            net_worth[i] = np.random.normal(800000, 250000)
        else:
            net_worth[i] = np.random.normal(1000000, 300000)

    return age, net_worth

# Create a function 'plot_data'
# Arguments: Two numpy arrays, age and net worth.
# Returns: None
# Details:
# The plot has a title 'Age vs Net Worth', x-axis label 'Age', and y-axis label 'Net Worth'.
# The y-axis should be in currency format, in increments of  1/10 the range of the data rounded to the nearest 10000.
def plot_data(age, net_worth):
    plt.scatter(age, net_worth)
    plt.title('Age vs Net Worth')
    plt.xlabel('Age')
    plt.ylabel('Net Worth')
    plt.gca().xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
    plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    plt.show()

"""
The selected Python code defines a main function that generates synthetic data for age and net worth, and then plots this data on a scatter plot.
"""
def main():
    age, net_worth = generate_data()
    plot_data(age, net_worth)

# Call the main function if the script is run directly
if __name__ == '__main__':
    main()