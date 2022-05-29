vic = float(input())
soma_vic = 0

while vic != -1:
    soma_vic += vic
    vic = float(input())

vic_reais = soma_vic * 2.5

print('VC$ %.2f' % soma_vic)
print('R$ %.2f' % vic_reais)