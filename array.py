arr = [10, 34, 45, 6 , 8 , 20, 25, 19]
min = arr[0]
max = arr[0]

for num in arr:
    if num < min:
        smin = num
        min = num
    if num > max:
        smax = num
        max = num
    print ("minimum:", min)
    print (" previous minimum:", min)
    print (" maximum:", max)
    print (" previous maximum:", max)