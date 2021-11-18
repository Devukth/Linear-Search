# Linear Search
def find_in(arr, item):
    for i in range(len(arr) - 1):
        if(arr[i] == item): return i
    return -1

array = [1, 4, 2, 6, 3, 5, 8, 7, 10, 9]
print(array)
search = int(input("Element to search >>> "))
index = find_in(array, search)
if (index != -1):
    print("Item", search, "found at index ", index)
else:
    print("Item cannot be found")