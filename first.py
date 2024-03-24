# n=5
# for i in range(n):
#     for j in range(n,i):
#         print(" ",end=' ')
#     for j in range(i,n):
#         print("*",end=' ')
#     print()        
n=5

for i in range(n):
    p=1
    for j in range(i):
        print("",end="")

    for j in range(i,n):
        print(p,end=' ')
        p+=1    
    print()    
