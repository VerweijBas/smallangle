import click
import numpy as np
from numpy import pi
import pandas as pd


def sin(number):
    """this function calculates the sin values between
    0 and 2pi

    Args:
        number (int): the amount of steps the sin value is
        calculated between 0 and 2pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


def tan(number):
    """this function calculates the tan values between
    0 and 2pi

    Args:
        number (int): the amount of steps the tan value is
        calculated between 0 and 2pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)



@click.group(help='this will give you values of sin or tan in amount of steps you choose within range 0 tot 2pi')
def smallangle():
    '''defines the function to be able to determine tan or sin based on choise'''
    pass

@click.command()
@click.option('-n', default=10, help='gives sin values between 0 and 2pi')
def sin_values(n):
    ''''generates sin values in certain amount of steps'''
    sin(n)

@click.command()
@click.option('-n', default=10, help='gives tan values between 0 and 2pi')
def tan_values(n):
    ''''generates tan values in certain amount of steps'''
    tan(n)


smallangle.add_command(sin_values, 'sin')
smallangle.add_command(tan_values, 'tan')



if __name__ == "__main__":
    smallangle()