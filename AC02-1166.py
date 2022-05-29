divida_total = int(input())
valor_pagar = int(input())

i = 1
   
while divida_total > 0:     
    print('pagamento:', i)
    print('antes =', divida_total)
       
    if divida_total <= valor_pagar:
        divida_total = 0
    else:
        divida_total -= valor_pagar
    
    i += 1

    print('depois =', divida_total)
    print('-----')