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



@click.group()
def smallangle():
    pass

@click.command()
@click.option('-n', default=10, help='gives sin values between 0 and 2pi')
def sin_values(n):
    sin(n)

@click.command()
@click.option('-n', default=10, help='gives tan values between 0 and 2pi')
def tan_values(n):
    tan(n)


smallangle.add_command(sin_values, 'sin')
smallangle.add_command(tan_values, 'tan')



if __name__ == "__main__":
    smallangle()