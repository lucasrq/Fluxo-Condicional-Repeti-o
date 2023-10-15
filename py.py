conteudo = []
idades = []
with open(file='banco.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()
    linha = arquivo.readline()
    while linha:
        LinhaSeparada = linha.split(sep=',')
        idade = LinhaSeparada[0]
        idade = int(idade)
        idades.append(idade)
        linha = arquivo.readline()
print(idades)


with open(file='idades.csv' , mode='w', encoding='utf8') as fp:
    linha = 'idade' + '\n'
    fp.write(linha)
    for idade in idades:
        linha = str(idade) + '\n'
        fp.write(linha)

with open(file='idades.csv' , mode='a', encoding='utf8') as fp:
    linha = "idade x2" + '\n'
    fp.write(linha)
    for idade in idades:
        linha = str(idade * 2) + '\n'
        fp.write(linha)