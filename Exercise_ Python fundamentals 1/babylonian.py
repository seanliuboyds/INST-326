"""Use the Babylonian method to approximate the square root of a positive
number."""
from argparse import ArgumentParser
import sys

def sqrt_b(S, p = 1e-10):
    """
    Approximate square root of any positive number using Babylonian method

    Args:
        S (float): the positive number which square root will be calculated from
        p (float, optional): the degree of precision to which square root is calculated
    
    Returns:
        float: the approximated square root of S
    
    Raises:
        TypeError: if S is not an integer or float
        TypeError: if p is not a float
        ValueError: if p is equal to or below 0
    """
    if not isinstance(S, (float, int)):
        raise TypeError("S is not an integer or float")
    if not isinstance(p, float):
        raise TypeError("p is not a float")
    if p <= 0:
        raise ValueError("p cannot be 0 or a negative")
    

    x = S/2

    while True:
        y = (x + (S/x))/2
        e = abs(y-x)
        if e < p:
            return y
        else:
            x = y

    
        







def parse_args(arglist):
    """Parse command-line arguments.
    Expect one required argument (a positive number whose square root the user
    wants to calculate) and one optional parameter (a precision, specified by
    the short flag -p or the long flag --precision). Both values
    are floats. The default precision is 0.0000000001 (1e-10).

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: a namespace with attributes "number" and "precision". The
        value of each of these attributes will be a float.
    """
    parser = ArgumentParser()
    parser.add_argument("number", type=float,
                help="number to compute the square root of")
    parser.add_argument("-p", "--precision", type=float, default=0.0000000001)
    return parser.parse_args(arglist)
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print(f"The square root of {args.number} is approximately"
        f" {sqrt_b(args.number, args.precision)}")
    
