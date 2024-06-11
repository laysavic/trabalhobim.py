nome_aluno = input('digite o nome do aluno:')
disciplina = input('digite o nome da disciplina:')

nota1 = int(input('digite a primeira nota:'))
nota2 = int(input('digite a segunda nota:'))
m = (nota1 + nota2)/2
if m >=6:
    situação = 'aprovado'
else:
    situação = 'reprovado'
print(f'{nome_aluno} está {situação} na disciplina {disciplina}.')

