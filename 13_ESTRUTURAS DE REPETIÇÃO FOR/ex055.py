maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa:'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print('O maior peso lido foi {}Kg e o menor foi {}Kg'.format(maior, menor)) 
    