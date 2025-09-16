from argparse import ArgumentParser
import sys


# Replace this comment with your implementations of the evaluate() and main()
# functions.
def evaluate(expression):
    """ Evaluate a postfix expression.

    Args:
        expression (str): a string containing a postfix expression.

    Returns:
        float: the value of the expression.
    
    Raises:
        TypeError if expression is not a string
        ValueError if expression is empty
        ValueError if expression is a single character
    """

    if not isinstance(expression, str):
        raise TypeError("expression must be a string")
    if len(expression) == 0:
        raise ValueError("expression must not be empty")
    if len(expression) == 1:
        raise ValueError("expression must not be a single character")

    x = []
    for i in expression:
        if i.isalnum():
            x.append(int(i))
        elif i == " ":
            continue
        else:
            if i == "*":
                y = x.pop()
                z = x.pop()
                x.append(z * y)
            elif i == "/":
                y = x.pop()
                z = x.pop()
                x.append(z / y)
            elif i == "+":
                y = x.pop()
                z = x.pop()
                x.append(z + y)
            elif i == "-":
                y = x.pop()
                z = x.pop()
                x.append(z - y)
    return x[0]

def main(filename):
    """ Read postfix expressions from a file and display the results.

    Args:
        filename (str): the name of the file containing postfix expressions.
    
    Raises:
        TypeError if filename is not a string
    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    with open(filename) as f:
        for line in f:
            line = line.strip()
            value = evaluate(line)
            print(f"{line} = {value}")


def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
