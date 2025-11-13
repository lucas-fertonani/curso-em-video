#ex102
#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro show, que será um valor lógico
#(opcional) indicando se será mostrado ou na tela o processo de cálculo do fatorial.


def  calcular_fatorial(fatorial: int, show: bool = False):
    """
    -> Calcula o fatorial de um número.
    :param n: o numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um número n.
    """

    result = fatorial

    for num in range(fatorial-1,0,-1):
        result = result * num
        
        if show:
            print('Percorrento o número: ', num, '| Resultado até o momento: ', result)
    
    return result



res = calcular_fatorial(7, True)

