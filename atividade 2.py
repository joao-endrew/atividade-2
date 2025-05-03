intro= ("aqui está os números selecionados: ")
print(intro)

for par in range(0, 30, 2):
    if par in [10, 20, 30]:
        continue
    print(par)
