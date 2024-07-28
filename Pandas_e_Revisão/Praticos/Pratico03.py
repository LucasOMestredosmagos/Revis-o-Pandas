def const_pares_e_impares():
    pares = 0
    impares = 0

    for i in range(10):
        num = int(input(f"Digite o {i+1} numero: "))
        if num % 2 == 0:
            pares +=1
        else:
            impares += 1

        print("Quantidade de numeros pares", {pares})

        print("Quantidade de numeros impares", {impares})        
const_pares_e_impares()


