def busca_infos_arquivo():
    infos = {}

    arquivo = open("moedas.csv", mode="r", encoding="utf8")
    try:
        for linha in arquivo:
            partes = linha.split(",")
            if len(partes) == 4:
                codigo = partes[0]
                nome_moeda = partes[2]
                valor_conversão = partes[3]
            dados[codigo] = (nome_moeda, valor_conversão)
    finally:
        arquivo.close()
    return infos


