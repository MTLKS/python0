def count_in_list(lst, elem_to_count) -> int:
    """Count the number of occurrences of elem_to_count in lst."""
    return len([elem for elem in lst if elem == elem_to_count])
