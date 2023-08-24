# método para receber e validar o input
def get_numero(posi):
    while True:
        print(f'Digite o número na posição {posi}: (use 0 para o espaço vazio)')
        try:
            num = int(input())
        except:
            print('Erro, por favor use um número')  # Exceção caso um caractere que não seja um número seja utilizado
            continue
        if num < 0 or num > 8:
            print('Erro, por favor use um número entre 0 e 8')  # Exceção:um número menor que 0/maior que 8 foi utilizado
            continue
        break
    return num
# método para instanciar o tabuleiro inicial
def input_tabuleiro():
    board = [[get_numero(0), get_numero(1), get_numero(2)],
             [get_numero(3), get_numero(4), get_numero(5)],
             [get_numero(6), get_numero(7), get_numero(8)]]
    return board

#para testar o método input_tabuleiro (remover depois)
print(input_tabuleiro()[0][0])
