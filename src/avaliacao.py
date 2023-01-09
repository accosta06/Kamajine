#Autor: André Costa
#Ano: 2023

import chess

#Definir o valor das peças
valor_pecas = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

#Variáveis de material de cada cor
material_branco = 0
material_preto = 0

#Tabelas de valores de casas
peao_branco = [
    0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5, 10, 25, 25, 10,  5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5, -5,-10,  0,  0,-10, -5,  5,
    5, 10, 10,-20,-20, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0
]

peao_preto = list(reversed(peao_branco))

cavalo_branco = [-50,-40,-30,-30,-30,-30,-40,-50,
                 -40,-20,  0,  0,  0,  0,-20,-40,
                 -30,  0, 10, 15, 15, 10,  0,-30,
                 -30,  5, 15, 20, 20, 15,  5,-30,
                 -30,  0, 15, 20, 20, 15,  0,-30,
                 -30,  5, 10, 15, 15, 10,  5,-30,
                 -40,-20,  0,  5,  5,  0,-20,-40,
                 -50,-40,-30,-30,-30,-30,-40,-50,]

cavalo_preto = list(reversed(peao_preto))

bispo_branco = [-20,-10,-10,-10,-10,-10,-10,-20,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -10,  0,  5, 10, 10,  5,  0,-10,
                -10,  5,  5, 10, 10,  5,  5,-10,
                -10,  0, 10, 10, 10, 10,  0,-10,
                -10, 10, 10, 10, 10, 10, 10,-10,
                -10,  5,  0,  0,  0,  0,  5,-10,
                -20,-10,-10,-10,-10,-10,-10,-20]

bispo_preto = list(reversed(bispo_branco))

torre_branca = [
                 0,  0,  0,  0,  0,  0,  0,  0,
                 5, 10, 10, 10, 10, 10, 10,  5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                 0,  0,  0,  5,  5,  0,  0,  0
]

torre_preta = list(reversed(torre_branca))

dama_branca = [
                -20,-10,-10, -5, -5,-10,-10,-20,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -10,  0,  5,  5,  5,  5,  0,-10,
                 -5,  0,  5,  5,  5,  5,  0, -5,
                  0,  0,  5,  5,  5,  5,  0, -5,
                -10,  5,  5,  5,  5,  5,  0,-10,
                -10,  0,  5,  0,  0,  0,  0,-10,
                -20,-10,-10, -5, -5,-10,-10,-20
]

dama_preta = list(reversed(dama_branca))

rei_meio_jogo_branco = [
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -20,-30,-30,-40,-40,-30,-30,-20,
                        -10,-20,-20,-20,-20,-20,-20,-10,
                         20, 20,  0,  0,  0,  0, 20, 20,
                         20, 30, 10,  0,  0, 10, 30, 20
]

rei_meio_jogo_preto = list(reversed(rei_meio_jogo_branco))

rei_fim_jogo_branco = [
                        -50,-40,-30,-20,-20,-30,-40,-50,
                        -30,-20,-10,  0,  0,-10,-20,-30,
                        -30,-10, 20, 30, 30, 20,-10,-30,
                        -30,-10, 30, 40, 40, 30,-10,-30,
                        -30,-10, 30, 40, 40, 30,-10,-30,
                        -30,-10, 20, 30, 30, 20,-10,-30,
                        -30,-30,  0,  0,  0,  0,-30,-30,
                        -50,-30,-30,-30,-30,-30,-30,-50
]

rei_fim_jogo_preto = list(reversed(rei_fim_jogo_branco))

def avaliarPeca(peca: chess.Piece, quadrado: chess.Square, end_game: bool) -> int:

    tipo_peca = peca.piece_type

    mapeamento = []

    if tipo_peca == chess.PAWN:
        mapeamento = peao_branco if peca.color == chess.WHITE else peao_preto
    
    if tipo_peca == chess.KNIGHT:
        mapeamento = cavalo_branco if peca.color == chess.WHITE else cavalo_preto
    
    if tipo_peca == chess.BISHOP:
        mapeamento = bispo_branco if peca.color == chess.WHITE else bispo_preto
    
    if tipo_peca == chess.ROOK:
        mapeamento = torre_branca if peca.color == chess.WHITE else torre_preta
    
    if tipo_peca == chess.QUEEN:
        mapeamento = dama_branca if peca.color == chess.WHITE else dama_preta
    
    if tipo_peca == chess.KING:
        if end_game:
            mapeamento = rei_fim_jogo_branco if peca.color == chess.WHITE else rei_fim_jogo_preto
        
        else:
            mapeamento = rei_meio_jogo_branco if peca.color == chess.WHITE else rei_meio_jogo_preto
    
    return mapeamento[quadrado]

def valorCaptura(tabuleiro: chess.Board, jogada: chess.Move) -> float:

    if tabuleiro.is_en_passant(jogada):
        return valor_pecas[chess.PAWN]

    origem = tabuleiro.piece_at(jogada.from_square)
    destino = tabuleiro.piece_at(jogada.to_square)

    return valor_pecas[destino.piece_type] - valor_pecas[origem.piece_type]

def valorJogada(tabuleiro: chess.Board, jogada: chess.Move, endgame: bool) -> float:
    
    if jogada.promotion is not None:
        return -float("inf") if tabuleiro.turn == chess.BLACK else float("inf")
    
    peca = tabuleiro.piece_at(jogada.from_square)

    if peca:
        valor_origem = avaliarPeca(peca, jogada.from_square, endgame)
        valor_destino = avaliarPeca(peca, jogada.to_square, endgame)
        mudanca_pos = valor_destino - valor_origem
    
    valor_captura = 0.0

    if tabuleiro.is_capture(jogada):
        valor_captura = valorCaptura(tabuleiro, jogada)
    
    valor_jogada_atual = valor_captura + mudanca_pos

    if tabuleiro.turn == chess.BLACK:
        valor_jogada_atual = -valor_jogada_atual
    
    return valor_jogada_atual

def avaliarTabuleiro(tabuleiro: chess.Board) -> float:

    total = 0

    endgame = verificarEndgame

    for quadrado in chess.SQUARES:
        peca = tabuleiro.piece_at(quadrado)
        
        if not peca:
            continue

        valor = valor_pecas[peca.piece_type] + avaliarPeca(peca, quadrado, endgame)
        total += valor if peca.color == chess.WHITE else -valor
    
    return total

def verificarEndgame(tabuleiro: chess.Board) -> bool:

    damas = 0
    cavBis = 0

    for quadrado in chess.SQUARES:
        peca = tabuleiro.piece_at(quadrado)

        if peca and peca.piece_type == chess.QUEEN:
            damas += 1
        
        elif peca and peca.piece_type == chess.BISHOP:
            cavBis += 1
        
        elif peca and peca.piece_type == chess.KNIGHT:
            cavBis += 1
    
    if damas == 0 or (damas == 2 and cavBis <= 1):
        return True
    
    else:
        return False