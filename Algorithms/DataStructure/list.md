# list comprehesion

**newList = [expression(i) for i in oldList if filter(i)]**

1. Remove even integers from the list
```
def remove_even(lst):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in lst if number % 2 != 0]
```

2. Merge two sorted lists
In-place solution

