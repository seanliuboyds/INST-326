from argparse import ArgumentParser
import sys


# Replace this comment with your implementations of the evaluate() and main()
# functions.
def evaluate(expression):
    """ Evaluate a postfix expression based on reverse polish notation

    Args:
        expression (list): a list containing a postfix expression. A list is required for double digit numbers. It is a split stripped string
        of line from main

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
        return float(expression)
    if len(expression) == 2:
        if expression[0] == "-":
            return float(expression)
    y = expression.strip().split(" ")
    if len(y) == 1:
        return float(y[0])

    x = []
    for i in y:
        if i.lstrip('-').replace('.', '').isdigit():
            x.append(float(i))
        elif i == " ":
            continue
        else:
            if i == "*":
                b = x.pop()
                a = x.pop()
                x.append(a * b)
            elif i == "/":
                b = x.pop()
                a = x.pop()
                x.append(a / b)
            elif i == "+":
                b = x.pop()
                a = x.pop()
                x.append(a + b)
            elif i == "-":
                b = x.pop()
                a = x.pop()
                x.append(a - b)
    return float(x[0])

def main(filename):
    """ Read postfix expressions from a file and display the results.

    Args:
        filename (str): the name of the file containing postfix expressions.
    
    Side effects:
        prints: line in file followed by equals sign and then final value of line after evaluate called 
    
    Raises:
        TypeError if filename is not a string
    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    with open(filename) as f:
        for line in f:
            value = evaluate(line)
            print(f"{line.strip()} = {value}")


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
