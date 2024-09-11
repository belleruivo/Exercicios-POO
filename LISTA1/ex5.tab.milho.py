'''5. Fazer um programa que calcule e escreva o número de grãos de milho que podem ser
colocados em um tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros
seguintes o dobro do quadro anterior. Obs.: esse número cresce muito rápido, tenha
o cuidado de testar se ele não sofre um overflow.'''

def calcular_graos():
    n_quadrados = 64
    n = 1
    total = 0
   
    for c in range(n_quadrados):

        print(f"Quadro {c}: {n} grãos")
        total = total + n
        n = n*2


    return total


def main():
    print("-="*40)
    print("Quntos grãos de milho cabem no tabuleiro?\n")
    try:
        resultado = calcular_graos()
        print(f"\nO total de grãos de milho no tabuleiro é: {resultado}")
   
    except OverflowError:
        print("\nO calculo excedeu o limite de capacidade de armazenamento.")

    print("-="*40)
       
main()

'''

def calcular_graos():
    num_quadrados = 64
    graos = 1
    total_graos = 0
    
    for i in range(num_quadrados):
        total_graos += graos
        print(f"Quadrado {i + 1}: {graos} grãos")
        graos *= 2
    
    return total_graos

def main():
    print("Número de grãos de milho no tabuleiro de xadrez:")
    total_graos = calcular_graos()
    print(f"\nTotal de grãos de milho em todo o tabuleiro: {total_graos}")

main()
'''




