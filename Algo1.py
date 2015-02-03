def maxSubArray(ar):
    tempSum=maxSum=ar[0]
    first=last=0

    for i in range(len(ar)):
        for j in range(i,len(ar)):
            tempSum=sum(ar[i:j+1])
            if tempSum > maxSum:
                first=i
                last=j
                maxSum=tempSum

#    print ("Alg1: ", ar , ar[first:last+1], maxSum)

'''
#Instructor-supplied tests:
maxSubArray([1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -1])    
maxSubArray([2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2])
maxSubArray([10, -11, -1, -9, 33,-45, 23, 24, -1, -7 -8, 19])
maxSubArray([31,-41, 59, 26, -53, 58, 97, -93, -23, 84 ])
maxSubArray([3, 2, 1, 1,-8, 1,1,2, 3])
maxSubArray([12, 99, 99, -99, -27, 0, 0, 0, -3,10 ])
maxSubArray([-2, 1,-3, 4, -1, 2, 1,-5, 4 ])
maxSubArray([-1, -3, -5 ])

#Jen-supplied tests:
maxSubArray([1, 2, 4, -1, 4, -10, 4, -19, 18, -1, -3, -4, 11, 3, -20, 19, -33, 50, 66, -22, -4, -55, 91, 100, -102, 9, 10, 19, -10, 10, 11, 11, -10, -18, 50, 90])
maxSubArray([12, 12, 14, -88, -1, 45, 6, 8, -33, 2, 8, -9, -33, -8, -23, -77, -89, 1, 9, 10, 92, 87])
maxSubArray([565, 78, 33, 9, 10, 84, 71, -4, -22, -55, -10, 76, -9, -9, -11, 76, 89, 11, 10, -33, 9])
maxSubArray([2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
maxSubArray([2])
maxSubArray([-1, -1, -1, -1, -1, -100, -10, -10, 100, 100, 100, 100, -100, 100, 10, -10, -1])
maxSubArray([12, 23, 44, -17, 12, 14, -88, -1, 45, 6, 8, -33, 2, 8, -9, -33, -8, -23, -77, -89, 1, 9, 13, -25, 10, 92, 57, 99, -22])
'''
