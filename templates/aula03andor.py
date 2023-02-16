idade = int(input("Digite a sua idade: "))
dinheiro = int(input("Digite o seu dinheiro"))
carteira = input("Você tem a carteira de motorista? (s/n)")

if (idade >=18 and dinheiro >= 50) or carteira == " s ":
    print ("Você pode alugar o carro.")
else:
    print("Você não pode alugar o carro.")