"""Loop principal e regras do jogo da memoria Remind."""

import random
import sys

import pygame

from src.config import CAMINHO_RECORDE
from src.dados import carregar_recorde, recorde_melhor, salvar_recorde

LARGURA = 640
ALTURA = 560
FPS = 30

COLUNAS = 4
LINHAS = 4
CARD_W = 100
CARD_H = 100
MARGEM = 15
OFFSET_X = 60
OFFSET_Y = 95
DELAY_MS = 1000

FUNDO = (20, 30, 60)
COR_COSTAS = (30, 50, 120)
COR_VIRADA = (255, 255, 255)
COR_ACERTADA = (50, 180, 80)
COR_BORDA = (0, 0, 0)
COR_TEXTO = (0, 0, 0)
COR_HUD = (255, 255, 255)
COR_DESTAQUE = (255, 220, 50)

SIMBOLOS = ["A", "B", "C", "D", "E", "F", "G", "H"]
TOTAL_PARES = len(SIMBOLOS)

GLIFOS = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "10000", "11110", "00001", "00001", "11110"],
    "6": ["01110", "10000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
    ":": ["00000", "00100", "00100", "00000", "00100", "00100", "00000"],
    "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    "!": ["00100", "00100", "00100", "00100", "00100", "00000", "00100"],
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
}


def criar_baralho(simbolos=None):
    """Cria uma lista com dois cards de cada simbolo."""
    simbolos = simbolos or SIMBOLOS
    return list(simbolos) * 2


def criar_tabuleiro(simbolos=None):
    """Cria o tabuleiro embaralhado usando matriz de dicionarios."""
    pares = criar_baralho(simbolos)
    random.shuffle(pares)

    tabuleiro = []
    for linha_indice in range(LINHAS):
        linha = []
        for coluna_indice in range(COLUNAS):
            simbolo = pares[linha_indice * COLUNAS + coluna_indice]
            linha.append(
                {
                    "simbolo": simbolo,
                    "virado": False,
                    "acertado": False,
                }
            )
        tabuleiro.append(linha)

    return tabuleiro


def contar_pares_acertados(tabuleiro):
    """Conta quantos pares ja foram encontrados."""
    cartas_acertadas = sum(
        1 for linha in tabuleiro for carta in linha if carta["acertado"]
    )
    return cartas_acertadas // 2


def checar_vitoria(tabuleiro):
    """Indica se todas as cartas ja foram acertadas."""
    return all(carta["acertado"] for linha in tabuleiro for carta in linha)


def formatar_tempo(segundos):
    """Formata segundos como mm:ss."""
    minutos = segundos // 60
    restante = segundos % 60
    return f"{minutos:02d}:{restante:02d}"


def formatar_recorde(recorde):
    """Formata o melhor resultado para o HUD."""
    if recorde is None:
        return "Recorde: --"

    return (
        f"Recorde: {recorde['tentativas']} tent. "
        f"em {formatar_tempo(recorde['tempo'])}"
    )


def get_pos(linha, coluna):
    """Retorna a posicao da carta na tela."""
    x = OFFSET_X + coluna * (CARD_W + MARGEM)
    y = OFFSET_Y + linha * (CARD_H + MARGEM)
    return x, y


def carta_clicada(mx, my):
    """Retorna linha e coluna da carta clicada, ou None."""
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            x, y = get_pos(linha, coluna)
            if x <= mx <= x + CARD_W and y <= my <= y + CARD_H:
                return linha, coluna
    return None


def medir_texto(texto, escala=2):
    """Calcula largura e altura do texto bitmap."""
    return len(texto) * 6 * escala, 7 * escala


def desenhar_texto(surface, texto, cor, posicao, escala=2):
    """Desenha texto usando glifos bitmap para evitar dependencia do pygame.font."""
    x_inicial, y_inicial = posicao
    for indice, caractere in enumerate(texto.upper()):
        glifo = GLIFOS.get(caractere, GLIFOS[" "])
        x_base = x_inicial + indice * 6 * escala
        for linha_indice, linha in enumerate(glifo):
            for coluna_indice, pixel in enumerate(linha):
                if pixel == "1":
                    rect = pygame.Rect(
                        x_base + coluna_indice * escala,
                        y_inicial + linha_indice * escala,
                        escala,
                        escala,
                    )
                    pygame.draw.rect(surface, cor, rect)


def desenhar_tabuleiro(surface, tabuleiro):
    """Desenha todas as cartas do tabuleiro."""
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            carta = tabuleiro[linha][coluna]
            x, y = get_pos(linha, coluna)
            rect = pygame.Rect(x, y, CARD_W, CARD_H)

            if carta["acertado"]:
                cor = COR_ACERTADA
            elif carta["virado"]:
                cor = COR_VIRADA
            else:
                cor = COR_COSTAS

            pygame.draw.rect(surface, cor, rect, border_radius=6)
            pygame.draw.rect(surface, COR_BORDA, rect, width=2, border_radius=6)

            if carta["virado"] or carta["acertado"]:
                largura, altura = medir_texto(carta["simbolo"], escala=7)
                desenhar_texto(
                    surface,
                    carta["simbolo"],
                    COR_TEXTO,
                    (x + (CARD_W - largura) // 2, y + (CARD_H - altura) // 2),
                    escala=7,
                )


def desenhar_hud(surface, estado):
    """Desenha tentativas, tempo, progresso, recorde e mensagem final."""
    desenhar_texto(
        surface,
        f"Tentativas: {estado['tentativas']}",
        COR_HUD,
        (10, 10),
        escala=2,
    )
    desenhar_texto(
        surface,
        f"Tempo: {formatar_tempo(estado['tempo'])}",
        COR_HUD,
        (180, 10),
        escala=2,
    )
    desenhar_texto(
        surface,
        f"Pares: {estado['pares_acertados']}/{TOTAL_PARES}",
        COR_HUD,
        (330, 10),
        escala=2,
    )
    desenhar_texto(
        surface,
        formatar_recorde(estado["recorde"]),
        COR_HUD,
        (10, 38),
        escala=2,
    )

    if estado["vitoria"]:
        mensagem = "Parabens! Voce venceu!"
        largura, altura = medir_texto(mensagem, escala=3)
        desenhar_texto(
            surface,
            mensagem,
            COR_DESTAQUE,
            ((LARGURA - largura) // 2, ALTURA - altura - 18),
            escala=3,
        )


def executar_jogo():
    """Executa o loop principal do jogo."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Remind - Jogo da Memoria")
    relogio = pygame.time.Clock()

    tabuleiro = criar_tabuleiro()
    selecionadas = []
    tentativas = 0
    bloqueado = False
    tempo_bloqueio = 0
    vitoria = False
    inicio_ticks = pygame.time.get_ticks()
    tempo_final = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)

    while True:
        tempo_atual = tempo_final
        if not vitoria:
            tempo_atual = (pygame.time.get_ticks() - inicio_ticks) // 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not bloqueado and not vitoria:
                pos = carta_clicada(*event.pos)
                if pos is None:
                    continue

                linha, coluna = pos
                carta = tabuleiro[linha][coluna]

                if carta["virado"] or carta["acertado"] or pos in selecionadas:
                    continue

                carta["virado"] = True
                selecionadas.append(pos)

                if len(selecionadas) == 2:
                    tentativas += 1
                    linha_1, coluna_1 = selecionadas[0]
                    linha_2, coluna_2 = selecionadas[1]
                    carta_1 = tabuleiro[linha_1][coluna_1]
                    carta_2 = tabuleiro[linha_2][coluna_2]

                    if carta_1["simbolo"] == carta_2["simbolo"]:
                        carta_1["acertado"] = True
                        carta_2["acertado"] = True
                        selecionadas = []
                        vitoria = checar_vitoria(tabuleiro)

                        if vitoria:
                            tempo_final = tempo_atual
                            novo_recorde = {
                                "tentativas": tentativas,
                                "tempo": tempo_final,
                            }
                            if recorde_melhor(novo_recorde, recorde):
                                salvar_recorde(
                                    CAMINHO_RECORDE,
                                    novo_recorde["tentativas"],
                                    novo_recorde["tempo"],
                                )
                                recorde = novo_recorde
                    else:
                        bloqueado = True
                        tempo_bloqueio = pygame.time.get_ticks()

        if bloqueado and pygame.time.get_ticks() - tempo_bloqueio >= DELAY_MS:
            for linha, coluna in selecionadas:
                tabuleiro[linha][coluna]["virado"] = False
            selecionadas = []
            bloqueado = False

        estado = {
            "tentativas": tentativas,
            "tempo": tempo_atual,
            "pares_acertados": contar_pares_acertados(tabuleiro),
            "recorde": recorde,
            "vitoria": vitoria,
        }

        tela.fill(FUNDO)
        desenhar_tabuleiro(tela, tabuleiro)
        desenhar_hud(tela, estado)
        pygame.display.flip()
        relogio.tick(FPS)

from src.jogo import executar_jogo


if __name__ == "__main__":
    executar_jogo()
