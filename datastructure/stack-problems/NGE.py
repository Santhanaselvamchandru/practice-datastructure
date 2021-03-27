# NGE -- Next Greater Element
def NGE(arr):
    for i in range(0,len(arr),1):
        next = -1
        for j in range(i,len(arr),1):
            if(arr[i] < arr[j]):
                next = arr[j]
                break
        print(arr[i],'---',next)




arr = [6,8,9,10,11,13]
NGE(arr)