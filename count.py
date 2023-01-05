n=int(input())
if n>0:
    count=0
    while n!=0:
        n=n/10
        count=count+1
        print(count)
else:
    print("not negative")
