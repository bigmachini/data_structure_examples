T= int(input())
# 1 <= T <= 30
T = 30

def checkPrimality(num):
    if num == 1: 
        return False
    
    if num ==  2:
        return True

    limit = int(pow(num, 0.5))
    
    for i in range(2,limit+1):
        if num % i == 0:
            return False
    return True

if 1 <= T and T <= 30:
    data = [1
,4
,9
,16
,25
,36
,49
,64
,81
,100
,121
,144
,169
,196
,225
,256
,289
,324
,361
,400
,441
,484
,529
,576
,625
,676
,729
,784
,841
,907]
    # while T  > 0:
    #     n = int(input())
    #     if 1 <= n and n <= (2 * pow(10, 9)):
    #         data.append(n)
    #         T = T - 1

    for i in data:
        if checkPrimality(i):
            print('Prime')
        else:
            print('Not Prime')
else:
    print("Constaint:  1 <= T <= 30")

