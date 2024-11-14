def binary_search(input_array , input_number):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = input_array[mid]
        if guess < input_number:
            low  = mid + 1
        if guess > input_number:
            high = mid - 1
        if guess == input_number:
            return mid
    return None
