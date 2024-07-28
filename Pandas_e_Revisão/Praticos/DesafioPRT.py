import pandas as pd

def gerenciador_de_compras():
    produtos = []

    while True:
        print("\033[33m\n--=Insira os produtos=--\033[0m")
        nome_produto = input("Nome do produto: ")
        preco_produto = float(input("Preço do produto: "))
        produtos.append({"Nome": nome_produto, "Preço": preco_produto})

        resposta = input("Deseja continuar inserindo produtos? (s/n): \033[0m")
        if resposta.lower() not in ["s", "sim"]:
            break 

    df = pd.DataFrame(produtos)

    total_gasto = df["Preço"].sum()
    produtos_caros = df[df["Preço"] > 1000].shape[0]
    produto_mais_barato = df.loc[df["Preço"].idxmin()]

    print("\n\033[33mCompra Finalizada!\033[0m")
    print(f"\033[31mTotal gasto: \033[92mR$ {total_gasto:.2f}\033[0m")
    print(f"Quantidade de produtos que custam mais de \033[92mR$\033[91m 1000: \033[0m {produtos_caros}")
    print(f"\033[96mProduto mais barato: \033[0m {produto_mais_barato['Nome']}")

gerenciador_de_compras()