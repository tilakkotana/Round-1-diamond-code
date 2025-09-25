d={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',}
n=int(input())
f=1
for i in range(1,n+1):
    print(" " * (n - f), end='')
    for j in range(1,i+1):
        print(d[j],end=' ')
    print()
    f=f+1
#print(f)
for i in range(n,0,-1):
    print(" " * (n-f+1), end='')
    for j in range(1,i+1):
        print(d[j],end=' ')
    print()
    f=f-1








