import chess
import argparse
from geradorJogadas import proxJogada


def iniciar():

    tabuleiro = chess.Board()
    user_side = (
        chess.WHITE if input("Começar com as [b]rancas ou com as [p]retas:\n") == "b" else chess.BLACK
    )

    if user_side == chess.WHITE:
        tabuleiro.push(obterJogada(tabuleiro))

    while not tabuleiro.is_game_over():
        jogada = proxJogada(get_depth(), tabuleiro)
        tabuleiro.push(jogada)
        print("CPU: " + str(jogada))
        tabuleiro.push(obterJogada(tabuleiro))

    print(f"\nResultado: [b] {tabuleiro.result()} [p]")



def obterJogada(board: chess.Board) -> chess.Move:

    move = input(f"\nA tua jogada (ex: {list(board.legal_moves)[0]}):\n")

    for legal_move in board.legal_moves:
        if move == str(legal_move):
            return legal_move
    return obterJogada(board)


def get_depth() -> int:
    analisarArgs = argparse.ArgumentParser()
    analisarArgs.add_argument("--depth", default=3, help="insere um numero inteiro (ex: 3")
    args = analisarArgs.parse_args()
    return max([1, int(args.depth)])


if __name__ == "__main__":
    try:
        iniciar()
    except KeyboardInterrupt:
        pass