

intro= ("aqui está os números selecionados: ")
print(intro)

for par in range(0, 31, 2):
    if par in [10, 20, 30]:
        continue
    print(par)