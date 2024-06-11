nome = input('digite o nome do cidadão:')
idade = int(input('digite a idade do cidadão:'))
if idade >= 16:
    situação= 'pode emitir o título de eleitor.'
else:
    situação= 'não pode emitir o título de eleitor'

print(nome,situação)