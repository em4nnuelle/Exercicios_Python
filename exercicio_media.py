soma_pares = 0
contagem_pares = 0

for numero in range(1,11,1):
    if numero%2 == 0:
        soma_pares = soma_pares + numero
        contagem_pares += 1
    else:
        continue

print(f'A soma acumulada foi {soma_pares} e a quantidade de pares foi {contagem_pares}')
print(f'A média dos números pares foi {soma_pares/contagem_pares}')