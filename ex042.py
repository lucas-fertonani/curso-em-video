#ex041
#Refaça o desafio 035 dos triangulos acresecentando o recurso de mostrar que tipo de triangulo sera
#formado:
#equilatero:todos os lados iguais
#isoceles: dois lados iguais
#escaleno:todos os lados diferentes

primeiro_cm_triangulo = float(input('Digite o comprimento da primeira linha reta: '))
segundo_cm_triangulo = float(input('Digite um comprimento da segunda linha reta: '))
terceira_cm_triangulo = float(input('Digite um comprimento da terceira linha reta: '))


if primeiro_cm_triangulo == segundo_cm_triangulo != terceira_cm_triangulo:
    print('Da para formar um isoceles')
elif primeiro_cm_triangulo == terceira_cm_triangulo != segundo_cm_triangulo:
    print('Da para formar um isoceles')
elif segundo_cm_triangulo == terceira_cm_triangulo != primeiro_cm_triangulo:
    print('Da para formar um isoceles')
elif segundo_cm_triangulo == primeiro_cm_triangulo != terceira_cm_triangulo:
    print('Da para formar um isoceles')
elif terceira_cm_triangulo == primeiro_cm_triangulo != segundo_cm_triangulo:
    print('Da para formar um isoceles')
elif terceira_cm_triangulo == segundo_cm_triangulo != primeiro_cm_triangulo:
    print('Da para formar um isoceles')
elif primeiro_cm_triangulo == terceira_cm_triangulo and segundo_cm_triangulo:
    print('Da para formar um equilatero')
elif primeiro_cm_triangulo != terceira_cm_triangulo != segundo_cm_triangulo:
    print('Da para formar um escaleno')