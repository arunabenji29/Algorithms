def eating_cookies(n):

    if(n==0):
        return 1
    elif(n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return eating_cookies(n-3)+eating_cookies(n-2)+eating_cookies(n-1)    

print(eating_cookies(10))                        


# def eating_cookies(n):
#     # a=[[1],[1,2]]
#     # b=[[1,1,1],[3]]

#     result = [[0]]
#     count = 3
#     # for i in range(0,len(n)):
#     #     n[i].append(1)

    

#     # if(n==0):
#     #     result = [[0]]
#     if(n==1):
#         # result[0] = 1
#         result.append([1])
#         # result[n-1] = result[n-1].append(1)
#         # result[n-2] = result[n-2].append(2)
#         # result[n-3] = result[n-3].append(3)
#         # eating_cookies(n-1)
#     # a=[[] for _ in range(n)]
#     if(n>1):
#         result[n-1].append(1)
#         # if(count==3):
#         #     result.append(3)
#         #     eating_cookies(n-1).append(count)

#     return result

# print(eating_cookies(2))