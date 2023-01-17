m=input("請輸入地圖X:")
n=input("請輸入地圖Y:")
x=int(input("當前位置X"))
y=int(input("當前位置Y"))
t=str(input("當前方向"))

#確認當前方向
if t=="N":
    t=0
elif t=="W":
    t=1
elif t=="S":
    t=2
elif t=="E":
    t=3


cc=[]
cc=input("指令:")
for s in cc:
    if s=="R":
        t-=1
    if s=="L":
        t+=1
    if s=="F":
        #在當前方向"往前"
        if t%4==0:
            y+=1
        if t%4==1:
            x-=1
        if t%4==2:
            y-=1
        if t%4==3:
            x+=1
        #確保在地圖內
        if x>m or x<0 or y>n or y<0:
            ooo="LOST"
            break

if t%4==0:
    t="N"
if t%4==1:
    t="W"
if t%4==2:
    t="S"
if t%4==3:
    t="E"

print(x,y,t,ooo)


    
