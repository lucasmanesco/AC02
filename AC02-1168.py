INICIO = int(input())
FIM = int(input())
  
primos = 0

for n in range(INICIO, FIM+1): 
  if n>1: 
    for d in range(2,n): 
        if(n % d==0): 
            break
    else: 
        print(n)
        primos +=1

print('primos:',primos)