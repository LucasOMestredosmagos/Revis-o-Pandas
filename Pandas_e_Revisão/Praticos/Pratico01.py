def classificar_idade(idade):
    if idade < 0:
        return "Idade Inválida"
    elif idade < 12:
        return "Criança"
    elif 12 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    
    idade = int(input("Digite Sua Idade: "))
    print("vocé é", classificar_idade(idade))
   