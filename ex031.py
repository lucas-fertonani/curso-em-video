#ex031
#Desenvolva um programa que pergunte a distância de uma viagem.Calcule o preço da passagem,cobrando
#0.50 por km para viagens de até 200km e 0.45 para viagens mais longas

numf = float(input('Quanto deu a sua viagem em km: '))


if numf < 200:
    km_nao_passado = (200 - numf) * 0.50
    print(f'Você terá que pagar na passagem do ônibus {km_nao_passado} R$')

if numf >= 200:
    km_passado = (numf - 200) * 0.45
    print(f'Voce terá que pagar na passagem do ônibus para viagens mais longas {km_passado} R$')
