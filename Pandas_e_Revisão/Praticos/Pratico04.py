def calcular_media_idade():
    n = int(input("Digite o número de pessoas: "))
    idades = []

    for i in range(n):
        idade = int(input(f"Digite a idade da {i+1} pessoa: "))
        idades.append(idade)

    media_idade = sum(idades) / n

    jovens = [idade for idade in idades if idade >= 0 and idade <= 25]
    adultos = [idade for idade in idades if idade >= 26 and idade <= 60]
    idosos = [idade for idade in idades if idade > 60]

    media_jovens = sum(jovens) / len(jovens) if jovens else 0
    media_adultos = sum(adultos) / len(adultos) if adultos else 0
    media_idosos = sum(idosos) / len(idosos) if idosos else 0

    print(f"Média de idade da turma: {media_idade:.2f}")
    print(f"Média de idade dos jovens (0-25):{media_jovens:.2f}")
    print(f"Média de idade dos adultos (26-60):{media_adultos:.2f}")
    print(f"Média de idade dos idosos (>60):{media_idosos:.2f}")

    if media_idade <=25:
        print("A turma é jovem.")
    if media_idade <= 60:
        print("A turma é adulta.")
    else:
        print("A turma é idosa.")

calcular_media_idade()                

