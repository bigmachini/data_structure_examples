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


# T= int(input())
# if 1 <= T and T <= 30:
#     data = []
#     while T  > 0:
#         n = int(input())
#         if 1 <= n and n <= (2 * pow(10, 9)):
#             data.append(n)
#             T = T - 1

#     for i in data:
#         if checkPrimality(i):
#             print('{} : Prime'.format(i))
#         else:
#             print('{} : Not Prime'.format(i))
# else:
#     print("Constaint:  1 <= T <= 30")

