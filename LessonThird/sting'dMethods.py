products = 'skovorodka skovorodki chainick kniga shkaf sigara pampersi istoria'
arrProducts = products.split()
skovorodki = []

for word in arrProducts:
    # if word.startswith('sko') == True:
        skovorodki.append(word)
print(skovorodki)
print(len(arrProducts))