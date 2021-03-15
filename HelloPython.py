#Finding maximum and minimum element in an array

def maxAndMin():

    #Sample Array
    arr = [10, 24,2222, 115, 890]

    #Varible for maximum and minimum element
    max = arr[0]
    min = arr[0]

    #loop for finding max & min element
    for i in arr:
        if max<i:
            max = i
        if i<min:
            min = i
    
    print "maximum element is: " ,max
    print "Minimum element is: " ,min
        
maxAndMin()