import matplotlib.pyplot as plt
import pandas as pd


def read_input():
    """
    Reads the input data from a CSV file.
    """
    df = pd.read_csv('data/atlantis.csv')
    x = df['year']
    y = df['population']
    return x, y


if __name__ == "__main__":
    x, y = read_input()
    plt.plot(x,y)
    plt.title("Population of Atlantis")
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.savefig('figs/population_plot.png')
    plt.show()
