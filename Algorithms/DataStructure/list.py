
# List Comprehension

def remove_even(lst):
    """
        Remove even integers from the list
    """
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in lst if number % 2 != 0]




