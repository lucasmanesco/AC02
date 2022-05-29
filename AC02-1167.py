inicio = int(input())
fim = int(input())

cont = 0

for bissexto in range(inicio, fim+1, 1):
    if bissexto % 4 == 0 and bissexto % 100 != 0 or bissexto % 400 == 0:
        print(bissexto)
        cont += 1

print('bissextos:', cont)