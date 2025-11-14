import inspect
def aumentar(num: float, aum: int, show: bool = False):
    calculo = num + (num * aum / 100)
    if show:
        return moeda(calculo)
    return calculo

def diminuir(num: float, aum: int, show: bool = False):
    calculo = num - (num * aum / 100)
    if show:
        return moeda(calculo)
    return calculo
    
def dobro(n: float, show: bool = False):
    calculo = n * 2
    if show:
        return moeda(calculo)
    return calculo

def metade(n: float, show: bool = False):
    calculo =  n / 2
    if show:
        return moeda(calculo)
    return calculo

def moeda(num):
    moeda_formatada = float(num)
    moeda_formatada = f'{moeda_formatada:.2f}'
    moeda_formatada = str(moeda_formatada).replace('.',',')

    return f'R${moeda_formatada}'

def resumo():
    modulo = __import__(__name__)

    funcoes = inspect.getmembers(modulo, inspect.isfunction)

    print("Funções encontradas:\n")

    for nome, _ in funcoes:
        if nome != "resumo":
            print(f"- {nome}")


if __name__ == "__main__":
    resumo()