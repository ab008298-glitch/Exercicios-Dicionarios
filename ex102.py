def cadastrar_pessoas():
    pessoas = []

    for i in range(10):
        print("\nCadastro da pessoa", i + 1)

        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        pessoa = {
            "nome": nome,
            "idade": idade
        }

        pessoas.append(pessoa)

    print("\nPESSOAS COM MENOS DE 18 ANOS:")

    for pessoa in pessoas:
        if pessoa["idade"] < 18:
            print("Nome:", pessoa["nome"])
            print("Idade:", pessoa["idade"])

    print("\nPESSOAS COM 18 ANOS OU MAIS:")

    for pessoa in pessoas:
        if pessoa["idade"] >= 18:
            print("Nome:", pessoa["nome"])
            print("Idade:", pessoa["idade"])

cadastrar_pessoas()