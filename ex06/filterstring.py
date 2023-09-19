from ft_filter import ft_filter
import sys


def main():
    """Main function."""

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = sys.argv[1].split()
        if [word for word in words if not word.isalnum()]:
            raise AssertionError("the arguments are bad")

        print(list(ft_filter(lambda word: len(word) > n, words)))
    except AssertionError as e:
        print(e.__class__.__name__ + ":", e)


if __name__ == "__main__":
    main()
