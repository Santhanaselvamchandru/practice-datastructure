# Using temp array
"""
def rotation(arr, d, n):
    for i in range(d):
        leftRotate(arr, n)
    return arr

def leftRotate(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
"""
def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    return arr

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    n = len(arr)
    print(leftRotate(arr, d, n))