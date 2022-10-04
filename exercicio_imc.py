#Exercício - Cálculo do IMC

peso = eval(input('Entre com o seu peso: '))
altura = eval(input('Entre com a sua altura: '))
imc = peso/(altura**2)
print ('Seu IMC é: ', imc)
#ou print (f'Seu IMC é: {imc}')