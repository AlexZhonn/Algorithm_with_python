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
# binary search takes O(log n). Compare to Simple Search(AkA Stupid Search), which takes O(N), BS saves a lot of time.

def binary_search_recursive(input_array, input_number, low, high):
    if low > high:  # 递归终止条件
        return None
    mid = (low + high) // 2
    guess = input_array[mid]
    if guess == input_number:
        return mid
    elif guess < input_number:
        return binary_search_recursive(input_array, input_number, mid + 1, high)
    else:
        return binary_search_recursive(input_array, input_number, low, mid - 1)
        