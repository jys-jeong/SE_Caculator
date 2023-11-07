def add(a,b):
    return a+b    

def sub(a,b):
    return a-b

def mul(a,b):
    


res=int(input())
while True:
    
    operator=input()
    if(operator=='='):
        print(res)
        break
    num2=int(input())
    if(operator=='+'):
        res = add(res,num2)
    elif(operator=='-'):
        res = sub(res,num2)
    elif(operator=='*'):
        res = mul(res,num2)

