a1 = float(input("Qual é o valor do primeiro termo ?"))
r = float(input("Qual é o valor da razão?"))
N = int(input("Quantos termos tem a PA?"))
soma = ((a1+(a1 + (N - 1)*r))*N)/2
print(soma)