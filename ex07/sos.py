import sys


def main():
    """Main function."""

    try:
        if len(sys.argv) != 2 or \
                not all([x.isalnum() or x.isspace() for x in sys.argv[1]]):
            raise AssertionError("the arguments are bad")

        nested_morse = {
            " ": "/ ",
            "A": ".- ",
            "B": "-... ",
            "C": "-.-. ",
            "D": "-.. ",
            "E": ". ",
            "F": "..-. ",
            "G": "--. ",
            "H": ".... ",
            "I": ".. ",
            "J": ".--- ",
            "K": "-.- ",
            "L": ".-.. ",
            "M": "-- ",
            "N": "-. ",
            "O": "--- ",
            "P": ".--. ",
            "Q": "--.- ",
            "R": ".-. ",
            "S": "... ",
            "T": "- ",
            "U": "..- ",
            "V": "...- ",
            "W": ".-- ",
            "X": "-..- ",
            "Y": "-.-- ",
            "Z": "--.. ",
            "0": "----- ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "----. ",
        }

        print("".join([nested_morse[x] for x in sys.argv[1].upper()]))
    except AssertionError as e:
        print(e.__class__.__name__ + ":", e)


if __name__ == "__main__":
    main()
