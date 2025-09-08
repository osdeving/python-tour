print('Cálculo de IMC')

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura em (m): '))

imc = peso / (altura ** 2)

print(f'O IMC para altura={altura} e peso={peso} é {imc:2f}')

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc > 25:
    print("Você está acima do peso")
else:
    print('Vocẽ está com o peso normal')

           