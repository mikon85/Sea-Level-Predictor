import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_sea_level_plot():
    # Import data from CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # Perform linear regression for all data
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050 using all data
    years_2050 = range(1880, 2051)
    sea_level_2050 = slope * years_2050 + intercept
    plt.plot(years_2050, sea_level_2050, color='red', label='All Data')

    # Perform linear regression for data from 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050 using data from 2000 onwards
    years_2050_2000 = range(2000, 2051)
    sea_level_2050_2000 = slope_2000 * years_2050_2000 + intercept_2000
    plt.plot(years_2050_2000, sea_level_2050_2000, color='green', label='2000 onwards')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add legend
    plt.legend()

    # Save the plot as an image
    plt.savefig('sea_level_plot.png')

    # Show the plot
    plt.show()

    # Return the plot
    return plt.gca().get_figure()

    # Test the functions
draw_sea_level_plot()
