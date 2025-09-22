"""Convert numbers from digits to words in _____."""


from argparse import ArgumentParser
import sys


LANGUAGES = [
    # uncomment "est" below if you implement Estonian numbers,
    # or "eus" if you implement Basque numbers
    
    # "est",
    "eus",
]


# replace this comment with your implementations of est() or eus() and main()
# (along with any helper functions, constants, etc. that you want to write)

def eus(number):
    """Convert numbers from digits to words in Basque.

    Args:
        number (int): a number to be converted to words.

    Returns:
        str: the number converted to words in Basque.
    
    Raises:
        TypeError: if argument given is not int
        ValueError: if argument given is negative
    """

    if number < 0:
        raise ValueError("Number is not an integer.")
    if not isinstance(number, int):
        raise TypeError("Number is not an integer")

    sh = fh = mid = ""
    stored = number
    basque_1_to_19 = [
        "bat", "bi", "hiru", "lau", "bost", "sei", "zazpi", "zortzi", "bederatzi",
        "hamar", "hamaika", "hamabi", "hamairu", "hamalau", "hamabost", 
        "hamasei", "hamazazpi", "hamazortzi", "hemeretzi"
    ]
    
    basque_tens = ["hogei", "berrogei", "hirurogei", "laurogei"]
    basque_hundreds = ["ehun", "berrehun", "hirurehun", "laurehun", "bostehun", 
                      "seiehun", "zazpiehun", "zortziehun", "bederatziehun"]
    
    checkDigit = str(number)
    if checkDigit[0] == "1" and len(checkDigit) == 4:
        mid = "mila"
        temp = checkDigit[1:].lstrip("0")
        if temp:
            sh = "eta " + str(eus(int(temp)))
            return mid + " " + sh
        else:
            return "mila"
        # sh = eus(checkDigit.lstrip("0"))

    if len(checkDigit) >= 4:
        l = len(checkDigit) - 3
        mid = "mila"
        temp = checkDigit[l:].lstrip("0")
        fh = eus(int(checkDigit[:l]))
        if temp:
            sh = eus(int(temp))

    if number == 0:
        return "zero"
    elif number < 20:
        return basque_1_to_19[number - 1]
    elif number < 100:
        twenties = number // 20
        remainder = number % 20
        if remainder == 0:
            return basque_tens[twenties - 1]
        else:
            return basque_tens[twenties - 1] + "ta " + basque_1_to_19[remainder - 1]
    elif number < 1000:
        hundreds = number // 100
        remainder = number % 100
        if remainder == 0:
            return basque_hundreds[hundreds - 1]
        else:

            return basque_hundreds[hundreds - 1] + " eta " + eus(remainder)
    else:
        if len(str(number)) == 4 and str(number)[1] == "0" and int(str(number)[1:]) > 0:
            sh = "eta " + str(sh)
        return (str(fh)  + " " + mid + " " + str(sh)).strip(" ")
                
            
            
        
def main(lang, input_file):
    with open(input_file) as f:
        for line in f:
            number = int(line.strip())
            if lang == "eus":
                print(number)
                print(eus(number))
            else:
                print("Language not supported")




def parse_args(arglist):
    """Parse command-line arguments.
    
    Three arguments are required, in the following order:
    
        lang (str): the ISO 639-3 language code of the language the user wants
            to convert numbers into.
        input_file (str): path to a file containing numbers expressed as digits.
        output_file (str): path to a file where numbers will be written as words
            in the target language.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments as a namespace. The following attributes
        will be defined: lang, input_file, and output_file. See above for
        details.
    """
    parser = ArgumentParser()
    parser.add_argument("lang", help="ISO 639-3 language code")
    parser.add_argument("input_file", help="input file containing numbers")
    # parser.add_argument("output_file", help="file where output will be stored")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.lang, args.input_file)
    # , args.output_file
