import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) < 2:
        exit(0)

    try:
        num = int(sys.argv[1])
        print(["I'm Even.", "I'm Odd."][num % 2])
    except ValueError:
        raise AssertionError("argument is not an integer")
except AssertionError as e:
    print(e.__class__.__name__ + ":", e)
