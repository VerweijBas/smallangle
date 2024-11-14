import click
import numpy as np
from numpy import pi
import pandas as pd


def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)




@click.command()
@click.argument('function', type=click.Choice(['sin', 'tan']))
@click.option('-n', default=10, help='gives tan values between 0 and 2pi')
def generate_values(function, n):
    if function == 'sin':
        sin(n)
    elif function == 'tan':
        tan(n)
    


if __name__ == "__main__":
    generate_values()