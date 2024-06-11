hora = int(input('digite a hora: '))
if hora >= 0 and hora<12:
    print('está de manhã')
elif  hora >=12 and hora<18:
    print('está de tarde')
else:
    print('está de noite')
