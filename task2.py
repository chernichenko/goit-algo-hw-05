def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    upper_bound = left if left < len(arr) else None
    return (iterations, arr[upper_bound] if upper_bound is not None else None)

# Тестуємо двійковий пошук
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5]
target_value = 3.3
result = binary_search(sorted_array, target_value)
print(result)  # Виведе: (кількість ітерацій, 3.3)

target_value = 4.0
result = binary_search(sorted_array, target_value)
print(result)  # Виведе: (кількість ітерацій, 4.4)