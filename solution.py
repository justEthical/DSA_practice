def hourglassSum(arr):
    # Write your code here
    w = len(arr[0])
    h = len(arr)
    _max = 0
    if w<3 or h<3:
        print("array dimension is not enough for hourGlass implementation")
    else:
        rowLoop = w-2
        columnLoop = h-2
        print(columnLoop)

        #columnLoop---------
        for c in range(0,columnLoop,1):
            print('lajfljdsl')
            #rowloop----------
            for r in range(0,rowLoop,1):
                #matrix columnloop
                print('kkkkkkkk')
                add=0
                for m in range(c,c+3,1):
                    
                    #matrix rowLoop
                    print('internal loop')
                    if m==c+1:
                        add+=arr[m][r+1]
                    else:
                        for n in range(r, r+3,1):
                            add+=arr[m][n]
                            if _max <add:  
                                _max = add
                            
                    print(add)
    return _max
    #print(add)

matrix = [[1, 1, 1],[0,1,0],[0,0,1]]
hourglassSum(matrix)