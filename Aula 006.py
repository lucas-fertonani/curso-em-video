#Tipos primitivos
#int=numeros inteiros, ex:1,2,3,4,5,6... -1,-2,-3,-4,-5,-6
#float=numeros flutuantes, ex: 4.5,0.076,-15.223
#bool= Valores boleanos, ex: True,False
#str=strings, ex: 'Olá,Mundo' ,'7.5' ,'' sao textos ou numero que estao em aspas

#comando type=voce recebe a classe da variavel ou seja=str,bool,float,int

#Forma diferente de escrever,print:
#Em vez de : print('a soma vale',s)
#Colocar:print('soma vale{}'.format(s))


n1=int(input('digite um valor'))
n2=int(input('digite um valor'))
#rint('a soma entre',n1,'e',n2,'vale',n1+n2)
print('A soma entre {} e {} vale {}'.format(n1,n2,n1+n2))