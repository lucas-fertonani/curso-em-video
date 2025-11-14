#Aula 023
#Tratamento de Erros e Exceções

#Exception -> exceção
#Para tratar execeções no python usaremos o comando: try: , except:         try->tente
try:
    operação
except:
    falhou

#Se eu tentar a operação de cima e falhar o que vai acontecer é assim que funciona o try e except
#e se dar certo usaremos outro comando que é:
try:
    operation
except:
    error
else:
    print(operation)

#O finally eu uso quando não importa se deu certo ou falhou veja:
try:
    operation
except:
    error
else:
    print(operation)
finally:
    print('<<<Foi bom sua companinha na calculadora!>>>')

#Para mostrar o erro eu uso o 'Exception as erro':
try:
    operation
except Exception as erro:
    error {erro.__cause__}
else:
    print(operation)
finally:
    print('<<<Foi bom sua companinha na calculadora!>>>')

#Eu posso ter varios tipos de except pra um try e cada um deles vai ter sua bloco, erro e mensagem
