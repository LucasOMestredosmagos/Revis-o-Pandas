def maior_menor_soma():
    n = int(input("Digite o número de valores: "))
    valores = []

    for i in range(n):
        valor = float(input(f"Digite o {i+1} valor: "))
        valores.append(valor)

        maior = max(valores)
        menor = min(valores)
        soma = sum(valores)

        print(f"Maior valor: {maior}")
        print(f"Menor valor: {menor}")
        print(f"Soma dos valores: {soma}")
maior_menor_soma()        
