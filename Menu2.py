from time import sleep
def menu():
    print('Bem vindo ao menu!')
    opcoes = int(input('Escolha uma das opções:\n'
                       '1 - Radar\n'
                       '2 - Conversor de Temperatura\n'
                       '3 - Lista para pessoas maiores e menores de idade\n'
                       '4 - "Mercadinho"\n'
                       '5 - Sair\n'))

    return (opcoes)

def mercadinho():
    produtos = []
    preco = []
    desejo = 'S'.upper()
    maior_valor = 0000000000000000000000000000000
    menor_valor = 999999999999999999999999999999
    maior_produto = str()
    menor_produto = str()

    while desejo == 'S':
        nome = input('Digite o nome do produto: ')
        produtos.append(nome)
        valor = float(input('Digite o valor desse produto: '))
        preco.append(valor)
        desejo = input('Deseja adicionar mais algum produto? (S/N)').upper()
        while desejo not in 'S' 'N':
            desejo = input('Opção inválida.\nDeseja adicionar mais algum produto? (S/N)').upper()

    for ma in range(len(preco)):
        if preco[ma] > maior_valor:
            maior_valor = preco[ma]
            maior_produto = produtos[ma]


    for i in range(len(preco)):
        if preco[i] < menor_valor:
            menor_valor = preco[i]
            menor_produto = produtos[i]


    print('A quantidade de produtos adicionados foi: {}'.format(len(produtos)))
    print('{} foi o produto mais caro adicionado custando R${:.2f}'.format(maior_produto, maior_valor))
    print('{} foi o produto mais barato adicionado custando R${:.2f}'.format(menor_produto, menor_valor))


def maiores_e_menores():
    pessoas = []
    nascimento = []
    maiores = []
    menores = []

    for i in range(5):
        nome = input('Qual o nome da {}° pessoa? '.format(i+1))
        pessoas.append(nome)
        ano = int(input('Em que ano {} nasceu? '.format(nome)))
        nascimento.append(2023-ano)

    for i in range(len(nascimento)):
        if nascimento[i] >= 18:
            maiores.append(pessoas[i])
        else:
            menores.append(pessoas[i])

    if maiores:
        mais_velha = pessoas[nascimento.index(max(nascimento))]
        print('Maiores de idade: {}'.format(len(maiores)))
        print('A pessoa mais velha é {} com {} anos.'.format(mais_velha, max(nascimento)))
    else:
        print('Não há pessoas maiores de idade.')

    if menores:
        mais_nova = pessoas[nascimento.index(min(nascimento))]
        print('Menores de idade: {}'.format(len(menores)))
        print('A pessoa masis nova é {} com {} anos.'.format(mais_nova, min(nascimento)))

    else:
        print('Não há pessoas menores de idade.')




def conversor_de_temperatura():
    temperatura = float(input("Insira a temperatura: "))
    farenheit = (temperatura * 9/5) + 32
    kelvin = temperatura + 273.15

    print("A temperatura ({}°) transformada para Farenheit e Kelvin, respectivamente"
          " são: {:.1f}° e {:.1f}°.".format(temperatura,farenheit,kelvin))



def radar():
    velocidade = float(input("Velocidade "))
    diferenca = velocidade - 60
    taxa1 = 7 * diferenca
    taxa2 = 14 * diferenca
    taxa3 = 39 * diferenca
    soma1 = taxa1 + 129
    soma2 = taxa2 + 129
    soma3 = taxa3 + 129


    if velocidade > 60 <= 80:
        print("Você foi multado em R$129,90 mais a taxa de {} totalizando {}".format(taxa1,soma1))
    elif velocidade > 80 <= 100:
        print("Você foi multado em R$129,90 mais a taxa de {} totalizando {}".format(taxa2,soma2))
    elif velocidade > 100:
        print("Você foi multado em R$129,90 mais a taxa de {} totalizando {}".format(taxa3,soma3))
    else:
        print("Muito bem! Você está no limite de velocidade.")



opcoes = menu()
while opcoes != 0:
    if opcoes == 1:
        radar()
        sleep(3)
        opcoes = menu()
    elif opcoes == 2:
        conversor_de_temperatura()
        sleep(3)
        opcoes = menu()
    elif opcoes == 3:
        maiores_e_menores()
        sleep(3)
        opcoes = menu()
    elif opcoes == 4:
        mercadinho()
        sleep(3)
        opcoes = menu()
    elif opcoes == 5:
        print('Saindo')
        sleep(3)
        break
    else:
        print('Opção inválida! Tente novamente.')
        opcoes = menu()