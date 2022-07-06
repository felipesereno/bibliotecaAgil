import os
from os import listdir
from os.path import isfile, join
import pathlib
import time

PATH_DO_BANCO = str(pathlib.Path(__file__).parent.resolve()) + '\\BD'
PREFIXO_TXT_LIVRO = 'livro'
SUFIXO_TXT_LIVRO = '_biblioteca.txt'

def get_qtd_livros_banco():
    fileDir = r"" + PATH_DO_BANCO
    fileExt = r".txt"
    pegar_livros_banco = [os.path.join(fileDir, a) for a in os.listdir(fileDir) if a.endswith(fileExt)]
    return len(pegar_livros_banco)

def get_livros_banco():
    fileDir = r"" + PATH_DO_BANCO
    fileExt = r".txt"
    pegar_livros_banco = [os.path.join(fileDir, a) for a in os.listdir(fileDir) if a.endswith(fileExt)]
    return pegar_livros_banco

def printa_livros_disponiveis():
    livros_banco = get_livros_banco()

    print('\nOs livros que estão disponíveis para retirada são:\n')
    for path_livro in livros_banco:

        with open(path_livro, "r", encoding="utf-8") as arquivo:
            conteudo_do_arquivo = arquivo.readlines()

            for linha_do_arquivo in conteudo_do_arquivo:
                if "Status" in linha_do_arquivo:
                    if linha_do_arquivo[7] == 'D':
                        with open(path_livro, "r", encoding="utf-8") as arquivo:
                            print(arquivo.read(), '\n')

def printa_livros_indisponiveis():
    livros_banco = get_livros_banco()

    qtd_livros_indisponiveis = 0
    print('\nOs livros que podem ser devolvidos são:\n')
    for path_arquivo_txt in livros_banco:

        with open(path_arquivo_txt, "r", encoding="utf-8") as arquivo:
            conteudo_do_arquivo = arquivo.readlines()

            for linha_do_arquivo in conteudo_do_arquivo:
                if "Status" in linha_do_arquivo:
                    if linha_do_arquivo[7] == 'I':
                        qtd_livros_indisponiveis += 1
                        with open(path_arquivo_txt, "r", encoding="utf-8") as arquivo:
                            print(arquivo.read(), '\n')

    if qtd_livros_indisponiveis == 0:
        print('Não há livros a serem devolvidos nessa biblioca.\n')

    return qtd_livros_indisponiveis

def loca_livro(numb_livro, nome_da_pessoa):
    arquivo_txt = PATH_DO_BANCO + '\\' + PREFIXO_TXT_LIVRO + str(numb_livro) + SUFIXO_TXT_LIVRO

    with open(arquivo_txt, "r", encoding="utf-8") as arquivo:
        conteudo_do_arquivo = arquivo.readlines()

    with open(arquivo_txt, "a", encoding="utf-8") as arquivo:
        conteudo_do_arquivo.pop()
        conteudo_do_arquivo.pop()

        open(arquivo_txt, 'w')
        for linha in conteudo_do_arquivo:
                arquivo.write(linha)

    with open(arquivo_txt, "a", encoding="utf-8") as arquivo:
        arquivo.write('Status:Indisponivel\n')
        arquivo.write('Emprestado para:' + nome_da_pessoa + '\n')

    with open(arquivo_txt, "r", encoding="utf-8") as arquivo:
        conteudo_do_arquivo = arquivo.read()
        print(conteudo_do_arquivo)

def repor_livro(numb_livro):
    arquivo_txt = PATH_DO_BANCO + '\\' + PREFIXO_TXT_LIVRO + str(numb_livro) + SUFIXO_TXT_LIVRO

    with open(arquivo_txt, "r", encoding="utf-8") as arquivo:
        conteudo_do_arquivo = arquivo.readlines()

        with open(arquivo_txt, "a", encoding="utf-8") as arquivo:
            conteudo_do_arquivo.pop()
            conteudo_do_arquivo.pop()

        with open(arquivo_txt, 'w') as arquivo:

            for linha in conteudo_do_arquivo:
                arquivo.write(linha)

    with open(arquivo_txt, "a", encoding="utf-8") as arquivo:
        arquivo.write('Status:Disponivel\n')
        arquivo.write('Emprestado para:')

    with open(arquivo_txt, "r", encoding="utf-8") as arquivo:
        conteudo_do_arquivo = arquivo.read()
        print(conteudo_do_arquivo)

def retirar_livro(nome_da_pessoa):
    printa_livros_disponiveis()

    numb_livro = int(input('Digite o número correspondente ao livro que gostaria de retirar: '))
    os.system('cls')
    print('\nO livro selecionado para retirada foi:\n')

    loca_livro(numb_livro, nome_da_pessoa)

    print('O livro foi locado com sucesso!\n')

def devolver_livro():
    qtd_livros_indisponiveis = printa_livros_indisponiveis()
    if qtd_livros_indisponiveis != 0:
        numb_livro = int(input('Digite o número correspondente ao livro que gostaria de devolver: '))
        print('\nO livro selecionado para devolução foi:\n')

        repor_livro(numb_livro)

        print('\nO livro foi devolvido com sucesso!\n')

def doar_livro():
    qtd_arquivos = str(get_qtd_livros_banco()+1)
    arquivo_txt = PATH_DO_BANCO + '\\' + PREFIXO_TXT_LIVRO + qtd_arquivos + SUFIXO_TXT_LIVRO

    with open(arquivo_txt, "w+", encoding="utf-8") as arquivo:

        with open(arquivo_txt, "a", encoding="utf-8") as arquivo:
            arquivo.write('Numero:' + qtd_arquivos)
            titulo = input('Digite o título do livro: ')
            autor = input('Digite o nome do autor do livro: ')
            ano = input('Digite o ano de lançamento do livro: ')
            arquivo.write('\nTitulo:' + titulo + '\n')
            arquivo.write('Autor:' + autor + '\n')
            arquivo.write('Ano:' + ano + '\n')
            arquivo.write('Status:Disponivel\n')
            arquivo.write('Emprestado para:\n')

    print('\nObrigado ' + nome_da_pessoa + ' pela sua doação.\n')


if __name__ == '__main__':

    print('\nBEM-VINDO À BIBLIOTECA ÁGIL!\n')
    nome_da_pessoa = input('Qual é o seu nome? ')
    os.system('cls')

    print('\nOlá, ' + nome_da_pessoa + '!\n')
    while(True):
        print('1. Retirar um livro')
        print('2. Devolver um livro')
        print('3. Doar um livro')
        print('0. Sair')
        option = int(input('\nPor favor, digite o número correspondente à opção desejada: '))
        os.system('cls')

        if option == 1:
            retirar_livro(nome_da_pessoa)
        elif option == 2:
            devolver_livro()
        elif option == 3:
            doar_livro()
        elif option == 0:
            print('Obrigado por contribuir com a propagação do hábito de leitura!\nVolte sempre!')
            time.sleep(1)
            exit()
        else:
            print('O número inserido não corresponde às opções disponíveis. Tente novamente.')