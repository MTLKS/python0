import sys


def main():
    """Main function."""

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        elif len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()

        count = dict.fromkeys(["upper", "lower", "punctuation", "spaces",
                                        "digits"], 0)

        for c in text:
            if c.isupper():
                count["upper"] += 1
            elif c.islower():
                count["lower"] += 1
            elif c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                count["punctuation"] += 1
            elif c.isspace():
                count["spaces"] += 1
            elif c.isdigit():
                count["digits"] += 1

        print(f"The text contains {len(text)} characters:")
        print(f"{count['upper']} upper letters")
        print(f"{count['lower']} lower letters")
        print(f"{count['punctuation']} punctuation marks")
        print(f"{count['spaces']} spaces")
        print(f"{count['digits']} digits")
    except AssertionError as e:
        print(e.__class__.__name__ + ":", e)


if __name__ == "__main__":
    main()
