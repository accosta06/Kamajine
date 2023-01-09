import chess
from avaliacao import avaliarTabuleiro, valorJogada, verificarEndgame

PONT_MATE     = 1000000000
MATE_THRESHOLD =  999000000


def proxJogada(depth: int, board: chess.Board, debug=True) -> chess.Move:

    jogada = minimax_base(depth, board)
    return jogada


def jogadasOrdem(tabuleiro: chess.Board):

    end_game = verificarEndgame(tabuleiro)

    def ordenador(move):
        return valorJogada(tabuleiro, move, end_game)

    in_order = sorted(
        tabuleiro.legal_moves, key=ordenador, reverse=(tabuleiro.turn == chess.WHITE)
    )
    return list(in_order)


def minimax_base(depth: int, tabuleiro: chess.Board) -> chess.Move:

    maximizar = tabuleiro.turn == chess.WHITE
    best_move = -float("inf")
    if not maximizar:
        melhorJogada = float("inf")

    jogadas = jogadasOrdem(tabuleiro)
    melhorJogadaEncontrada = jogadas[0]

    for jogada in jogadas:
        tabuleiro.push(jogada)

        if tabuleiro.can_claim_draw():
            valor = 0.0
        else:
            value = minimax(depth - 1, tabuleiro, -float("inf"), float("inf"), not maximizar)
        tabuleiro.pop()
        if tabuleiro and value >= best_move:
            best_move = value
            best_move_found = jogada
        elif not tabuleiro and value <= best_move:
            best_move = value
            best_move_found = jogada

    return best_move_found


def minimax(
    depth: int,
    tabuleiro: chess.Board,
    alpha: float,
    beta: float,
    maximizar: bool,
) -> float:

    if tabuleiro.is_checkmate():
        
        return -PONT_MATE if maximizar else PONT_MATE
    
    elif tabuleiro.is_game_over():
        return 0

    if depth == 0:
        return avaliarTabuleiro(tabuleiro)

    if maximizar:
        melhorJogada = -float("inf")
        moves = jogadasOrdem(tabuleiro)
        for move in moves:
            tabuleiro.push(move)
            jogadaAtual = minimax(depth - 1, tabuleiro, alpha, beta, not maximizar)

            if jogadaAtual > MATE_THRESHOLD:
                jogadaAtual -= 1
            elif jogadaAtual < -MATE_THRESHOLD:
                jogadaAtual += 1
            melhorJogada = max(
                melhorJogada,
                jogadaAtual,
            )
            tabuleiro.pop()
            alpha = max(alpha, melhorJogada)
            if beta <= alpha:
                return melhorJogada
        return jogadaAtual
    else:
        melhorJogada = float("inf")
        jogadas = jogadasOrdem(tabuleiro)
        for jogada in jogadas:
            tabuleiro.push(jogada)
            jogadaAtual = minimax(depth - 1, tabuleiro, alpha, beta, not maximizar)
            if jogadaAtual > MATE_THRESHOLD:
                jogadaAtual -= 1
            elif jogadaAtual < -MATE_THRESHOLD:
                jogadaAtual += 1
            melhorJogada = min(
                melhorJogada,
                jogadaAtual,
            )
            tabuleiro.pop()
            beta = min(beta, melhorJogada)
            if beta <= alpha:
                return melhorJogada
        return melhorJogada