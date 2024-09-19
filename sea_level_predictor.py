import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    ling1 = linregress(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    arange1 = np.arange(df.Year[0], 2051, 1)
    plt.plot(arange1, ((arange1*ling1.slope) + ling1.intercept), 'r')

    # Create second line of best fit
    arange2 = np.arange(2000, 2051, 1)
    ling2 = linregress(df.loc[df.Year >= 2000]['Year'], df.loc[df.Year >= 2000]['CSIRO Adjusted Sea Level'])
    plt.plot(arange2, ((arange2*ling2.slope) + ling2.intercept), 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
