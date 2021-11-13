# reverse rotation

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def leftRotate(arr, d, n):
    if d == 0:
        return 
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    leftRotate(arr, 2, len(arr))
    print(arr)
