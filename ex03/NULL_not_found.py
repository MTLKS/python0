def NULL_not_found(object: any) -> int:
    """This function print the type of the object passed in parameter"""

    if object is None:
        print("Nothing:", object, type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese:", object, type(object))
    elif isinstance(object, int) and object == 0:
        print("Zero:", object, type(object))
    elif isinstance(object, str) and object == "":
        print("Empty:", object, type(object))
    elif isinstance(object, bool) and not object:
        print("Fake:", object, type(object))
    else:
        print("Type not Found")
        return 1
    return 0
