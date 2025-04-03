def mergeIntervals(array):
    array.sort(key=lambda x: x[0])
    arr = [array[0]]
    for bgn, end in array[1:]:
        frst_end = arr[-1][1]

        if bgn <= frst_end:
            arr[-1][1] = max(frst_end, end)
        else:
            arr.append([bgn,end])
    return(arr)

merge1 = mergeIntervals([[1,3], [2,6], [8,10], [15,18]])
merge2 = mergeIntervals([[1,4], [4,5]])  
print(merge1)
print(merge2)
