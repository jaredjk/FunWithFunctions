# for i in range(1,2001):
#     if i%2 !=0:
#         print "Number is {}. This is an odd Nnumber".format(i)
#     else:    
#         print "Number is {}. This is an even Nnumber".format(i)


def multiply(arr,num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr

a = [2,4,10,15]

b = multiply(a,5)

print b

def layered_multiples(arr):
    for i in range(len(arr)):
        arr[i] = [1]*arr[i]


    return arr
x = layered_multiples(multiply([2,4,5],3))
print x