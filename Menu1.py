from time import sleep
def menu():
    print('Bem vindo ao menu!')
    opcoes = int(input('Escolha uma das opções:\n'
                       '1 - Calculo de Média\n'
                       '2 - Tabuada\n'
                       '3 - Pares, Impares (soma pares e soma impares\n'
                       '4 - Sair\n'))

    return (opcoes)

def calculo_de_media():
    nome = str(input("Insira seu nome: "))
    nota1 = float(input("Insira sua nota um: "))
    nota2 = float(input("Insira sua nota dois: "))

    media = (nota1 + nota2)/2

    if media >= 6:
        print("Olá {}, você foi aprovado. Sua media foi {}".format(nome, media))
    else:
        print("Olá {}, você foi reprovado. Sua media foi {}".format(nome, media))

def tabuada():
    num = int(input("Digite um numero para ver sua tabuada: "))
    print("{} x {:2} = {}".format(num, 1, num*1))
    print("{} x {:2} = {}".format(num, 2, num*2))
    print("{} x {:2} = {}".format(num, 3, num*3))
    print("{} x {:2} = {}".format(num, 4, num*4))
    print("{} x {:2} = {}".format(num, 5, num*5))
    print("{} x {:2} = {}".format(num, 6, num*6))
    print("{} x {:2} = {}".format(num, 7, num*7))
    print("{} x {:2} = {}".format(num, 8, num*8))
    print("{} x {:2} = {}".format(num, 9, num*9))
    print("{} x {:2} = {}".format(num, 10, num*10))

def pares_e_impares():
    num = float(input("Insira cinco números: "))
    if num % 2 == 0:
        print("Seu numero ({}) é par!".format(num))
    else:
        print("Seu numero ({}) é impar!".format(num))

opcoes = menu()
while opcoes != 0:
    if opcoes == 1:
        calculo_de_media()
        sleep(2)
        print()
        opcoes = menu()
    elif opcoes == 2:
        tabuada()
        print()
        sleep(2)
        opcoes = menu()
    elif opcoes == 3:
        pares_e_impares()
        sleep(2)
        print()
        opcoes = menu()
    elif opcoes == 4:
        print('Saindo')
        sleep(3)
        break
    else:
        print('Opção inválida! Tente novamente.')
        opcoes = menu()