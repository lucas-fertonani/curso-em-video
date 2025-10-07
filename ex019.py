#ex019
#Um professor quer sortear um dos seus alunos para apagar um quadro faca um programa que ajude,lendo um nome deles
#e  escrevendo o nome que foi escolhido
import random
nome = ['lucas','enzo','miguel','pietro']
print('O nome sorteado para apagar o quadro foi {}'.format(random.choice(nome)))