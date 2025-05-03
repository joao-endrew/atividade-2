
while True:
    nota1 = float(input("Digite a primera nota: "))
    if 0 <= nota1 <= 10:
        break
    else:
        print("por favor, digite um numero valido.")

while True:
    nota2 = float(input("Digite a segunda nota: "))
    if 0 <= nota2 <= 10:
        break
    else:
        print("por favor, digite um numero valido.")

media = (nota1 + nota2) / 2
print("A média do aluno é: ", media)

if media >= 6:
    print("Parabéns! Você foi aprovado.")
else:
    print("Infelizmente, você foi reprovado.")
