from sys  import stdin  #讀取鍵盤輸入
def create(n):
    global x,app
    x=1
    while (n!=1 and n>0):

        if n%2==1:
            n=3*n+1
        else:
            n/=2
        x+=1
    return x

for s in stdin:
    app=[]
    m,n=map(int,s.split())  #小括弧內默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
    
    a=m
    b=n
    if m>n:
        m,n=n,m
    for a in range(m,n+1):
        app.append(create(a))
    print(a,b,max(app))