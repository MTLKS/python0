from ft_filter import ft_filter


def main():
    """Main function."""

    original = filter.__doc__
    copy = ft_filter.__doc__

    print(copy)  # output: docstring
    print(original == copy)  # output: True

    print(filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(ft_filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    print(list(filter(lambda x: x > 2, [1, 2, 3, 4, 5])))
    print(list(ft_filter(lambda x: x > 2, [1, 2, 3, 4, 5])))

    print(list(filter(None, [0, 1, False, True, [1, 2, 3], "", "Hello"])))
    print(list(ft_filter(None, [0, 1, False, True, [1, 2, 3], "", "Hello"])))


if __name__ == "__main__":
    main()
