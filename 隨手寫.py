from sys  import stdin
 
def f(nn):
    arr1=[nn]
    while(nn!=1):
        if(nn%2==1):nn=nn*3+1#奇數
        else:nn=nn//2#偶數
        arr1.append(nn)
    return len(arr1)
 
 
for s in stdin:
 
    m,n=map(int,s.split())
    print(f'{m} {n}',end=' ')
    arr=[]
    #確保小到大
    if (m>n):m,n=n,m
 
    for i in range(m,n+1):
        arr.append(f(i))
    #print(arr)
    print(max(arr))

#lambda
 
 