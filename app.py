import os
from modelos.restaurante import Restaurante


def finalizar_app():
    os.system("cls")
    print("Finalizando o app\n")


def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")


def mostrar_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def escolher_opcoes():
    mostrar_subtitulo("""ℜ𝔢𝔰𝔱𝔞𝔲𝔯𝔞𝔫𝔱𝔢 𝔈𝔵𝔭𝔯𝔢𝔰𝔰𝔬 𝔏𝔲𝔠𝔞𝔰 & 𝔍𝔬𝔞̃𝔬""")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurantes")
    print("3 - Ativar/Desativar restaurante")
    print("4 - Avaliar Restaurante")
    print("5 - Sair\n")


def opcao_invalida():
    mostrar_subtitulo("Opção inválida\n".ljust(20))
    voltar_menu_principal()


def listar_restaurantes():
    mostrar_subtitulo("Listando os Restaurantes".ljust(20))
    Restaurante.listar_restaurantes()
    voltar_menu_principal()


def alternar_estado_restaurante():
    mostrar_subtitulo("Alterando o estado do restaurante".ljust(20))
    Restaurante.listar_restaurantes()
    nome_restaurante = input(
        "Digite o nome do Restaurante que desejas alterar: ")
    restaurante = Restaurante.encontrar_restaurante(nome_restaurante)

    if restaurante:
        restaurante.alternar_status()
        print(f"O restaurante {restaurante.nome} foi {'ativado' if restaurante._ativo else 'desativado'} com "
              f"sucesso.")
    else:
        print("O restaurante não foi encontrado.")

    voltar_menu_principal()


def avaliacao():
    mostrar_subtitulo("Avaliar Restaurante\n".ljust(20))
    Restaurante.listar_restaurantes()

    nome_restaurante = input(
        "Digite o nome do restaurante que deseja avaliar: ")
    cliente = input("Digite seu nome: ")
    restaurante = Restaurante.encontrar_restaurante(nome_restaurante)

    if restaurante:
        while True:
            try:
                nota = int(
                    input("Digite uma nota de 1 a 5 para avaliar este restaurante: "))
                if 1 <= nota <= 5:
                    restaurante.receber_avaliacao(cliente, nota)
                    print(f"Você avaliou o restaurante {nome_restaurante} com a nota {nota}.")
                    break
                else:
                    print("Por favor, digite uma nota válida (entre 1 e 5).")
            except ValueError:
                print("Por favor, digite um número válido.")
    else:
        print("Restaurante não encontrado.")

    voltar_menu_principal()


def cadastrar_novo_restaurante():
    os.system("cls")
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    Restaurante(nome_do_restaurante, categoria)
    print(f"Você cadastrou o restaurante: {nome_do_restaurante}")


def main():
    while True:
        try:
            escolher_opcoes()
            opcao_digitada = int(input("Digite a opção desejada: "))
            if opcao_digitada == 1:
                print("Você escolheu cadastrar restaurante\n")
                cadastrar_novo_restaurante()
            elif opcao_digitada == 2:
                listar_restaurantes()
            elif opcao_digitada == 3:
                alternar_estado_restaurante()
            elif opcao_digitada == 4:
                avaliacao()
            elif opcao_digitada == 5:
                print("Você escolheu sair do aplicativo\n")
                finalizar_app()
                break
            else:
                opcao_invalida()
        except:
            print("Por favor, digite um número válido.")


class Programa:
    # * Exemplos.
    def __init__(self):
        self.restaurantes = [
            Restaurante("Veneza", "Comida Italiana"),
            Restaurante("Pedra Chata", "Buffet Livre"),
            Restaurante("Banha Banhenta", "Petiscaria"),
            Restaurante("Pura Bucha", "Churrascaria")
        ]
        self.restaurantes[0].alternar_status()
        self.restaurantes[0].receber_avaliacao("João", 3)
        self.restaurantes[0].receber_avaliacao("Paulo", 5)
        self.restaurantes[0].receber_avaliacao("Daniel", 2)
        self.restaurantes[0].receber_avaliacao("Lucas", 3.6)


if __name__ == "__main__":
    programa = Programa()
    main()
