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

def generate_data():
    age = np.arange(20, 71, 1)
    net_worth = np.random.normal(500000, 200000, len(age))
    for i in range(len(age)):
        if age[i] < 30:
            net_worth[i] = np.random.normal(300000, 100000)
        elif age[i] < 40:
            net_worth[i] = np.random.normal(400000, 150000)
        elif age[i] < 50:
            net_worth[i] = np.random.normal(500000, 200000)
        elif age[i] < 60:
            net_worth[i] = np.random.normal(600000, 250000)
        elif age[i] < 70:
            net_worth[i] = np.random.normal(700000, 300000)
    return age, net_worth


def plot_data(age, net_worth):
    plt.scatter(age, net_worth)
    plt.title('Age vs Net Worth')
    plt.xlabel('Age')
    plt.ylabel('Net Worth')
    plt.gca().xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
    plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    plt.show()


def main():
    age, net_worth = generate_data()
    plot_data(age, net_worth)

if __name__ == '__main__':
    main()