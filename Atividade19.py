#levy
altura = bool (input("Digite sua altura "))
peso = int (input("Digite seu peso "))
imc = peso * altura / 2

if(imc <18,5):
    print("Abaixo do peso")
elif(imc <24,9):
    print("Peso normal")
elif(imc <29,9):
    print("Sobrepeso")
else:
    print("Obesidade")