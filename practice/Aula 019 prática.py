#Aula 019 prática
#Variáveis compostas (Dicionários)

pais = {'País': 'Brazil', 'População': 210000000, 'lugar mais famoso': 'Cristo Redentor'}
print(pais['População'])
print(pais['País'])
print(pais['lugar mais famoso'])
print(f'O {pais["País"]} tem seu lugar mais famoso como o {pais["lugar mais famoso"]} e sua população e de {pais["População"]} milhões')
print(pais.keys())
print()
print(pais.values())
print()
print(pais.items())
for t in pais.values():
    print(t)
for i,t in pais.items():
    print(f'O {i} tem como {t}')

pais['População'] = 4000
for i,t in pais.items():
    print(f'O {i} tem como {t}')

pais['Segurança'] = 'média'
for i,t in pais.items():
    print(f'O/A {i} tem como {t}')

#Criar um dicionário dentro de uma lista
politica = []
presidente_governo = {'Presidente': 'Luiz Inacio Lula da Silva','Governo':'Cláudio Castro'}
Partido = {'Partido do presidente-atual':'Partido dos Trabalhadores','Partido do Governo-atual': 'Partido Liberal'}
politica.append(presidente_governo)
politica.append(Partido)
print(politica)
print(politica[1])

#Contar
federacao = {}
pais_ = []
for o in range(0,4):
    federacao['Governo'] = str(input('Governo: '))
    federacao['Presidente'] = str(input('Presidente: '))
    pais_.append(federacao.copy())
print(pais_)
for e in pais_:
    print(e)
    for v in e.values():
        print(v,end=(' '))
    print()