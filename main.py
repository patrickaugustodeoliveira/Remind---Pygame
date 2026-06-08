"""
Jogo da Memória - Protótipo Inicial
Semana 2 – Ponto de controle 04
Usando Pygame
"""

import pygame
import random
import sys

# --- Configurações ---
LARGURA  = 640
ALTURA   = 520
FUNDO    = (20, 30, 60)       # "#141e3c"
COLUNAS  = 4
LINHAS   = 4
CARD_W   = 100
CARD_H   = 100
MARGEM   = 15
OFFSET_X = 60
OFFSET_Y = 80
FPS      = 30

COR_COSTAS   = (30, 50, 120)   # "#1e3278"
COR_VIRADA   = (255, 255, 255) # "#ffffff"
COR_ACERTADA = (50, 180, 80)   # "#32b450"
COR_BORDA    = (0, 0, 0)
COR_TEXTO    = (0, 0, 0)
COR_HUD      = (255, 255, 255)

SIMBOLOS = ["A", "B", "C", "D", "E", "F", "G", "H"]


# --- Funções ---

def criar_tabuleiro():
    pares = SIMBOLOS * 2
    random.shuffle(pares)
    tabuleiro = []
    for i in range(LINHAS):
        linha = []
        for j in range(COLUNAS):
            linha.append({
                "simbolo":  pares[i * COLUNAS + j],
                "virado":   False,
                "acertado": False,
            })
        tabuleiro.append(linha)
    return tabuleiro


def get_pos(linha, col):
    x = OFFSET_X + col * (CARD_W + MARGEM)
    y = OFFSET_Y + linha * (CARD_H + MARGEM)
    return x, y


def carta_clicada(mx, my):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            x, y = get_pos(i, j)
            if x <= mx <= x + CARD_W and y <= my <= y + CARD_H:
                return i, j
    return None


def desenhar_tabuleiro(surface, tabuleiro, fonte_simbolo):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            carta = tabuleiro[i][j]
            x, y  = get_pos(i, j)
            rect  = pygame.Rect(x, y, CARD_W, CARD_H)

            if carta["acertado"]:
                cor = COR_ACERTADA
            elif carta["virado"]:
                cor = COR_VIRADA
            else:
                cor = COR_COSTAS

            pygame.draw.rect(surface, cor, rect, border_radius=6)
            pygame.draw.rect(surface, COR_BORDA, rect, width=2, border_radius=6)

            if carta["virado"] or carta["acertado"]:
                texto  = fonte_simbolo.render(carta["simbolo"], True, COR_TEXTO)
                tr     = texto.get_rect(center=(x + CARD_W // 2, y + CARD_H // 2))
                surface.blit(texto, tr)


def desenhar_hud(surface, fonte_hud, tentativas, vitoria):
    msg = f"Tentativas: {tentativas}"
    texto = fonte_hud.render(msg, True, COR_HUD)
    surface.blit(texto, (10, 10))

    if vitoria:
        fonte_win = pygame.font.SysFont("Arial", 28, bold=True)
        win_texto = fonte_win.render("Parabéns! Você venceu!", True, (255, 220, 50))
        wr = win_texto.get_rect(center=(LARGURA // 2, ALTURA - 30))
        surface.blit(win_texto, wr)


def checar_vitoria(tabuleiro):
    return all(carta["acertado"] for linha in tabuleiro for carta in linha)


# --- Loop principal ---

def main():
    pygame.init()
    screen  = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo da Memória")
    clock   = pygame.time.Clock()

    fonte_simbolo = pygame.font.SysFont("Arial", 32, bold=True)
    fonte_hud     = pygame.font.SysFont("Arial", 16, bold=True)

    tabuleiro    = criar_tabuleiro()
    selecionadas = []
    tentativas   = 0
    bloqueado    = False
    tempo_bloqueo = 0   # tick em que o bloqueio começou
    DELAY_MS     = 1000
    vitoria      = False

    while True:
        # --- Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not bloqueado and not vitoria:
                mx, my = event.pos
                pos = carta_clicada(mx, my)
                if not pos:
                    continue

                i, j  = pos
                carta = tabuleiro[i][j]

                if carta["virado"] or carta["acertado"] or (i, j) in selecionadas:
                    continue

                carta["virado"] = True
                selecionadas.append((i, j))

                if len(selecionadas) == 2:
                    tentativas += 1
                    i1, j1 = selecionadas[0]
                    i2, j2 = selecionadas[1]

                    if tabuleiro[i1][j1]["simbolo"] == tabuleiro[i2][j2]["simbolo"]:
                        tabuleiro[i1][j1]["acertado"] = True
                        tabuleiro[i2][j2]["acertado"] = True
                        selecionadas = []
                        vitoria = checar_vitoria(tabuleiro)
                    else:
                        bloqueado     = True
                        tempo_bloqueo = pygame.time.get_ticks()

        # --- Fechar cartas após delay ---
        if bloqueado and pygame.time.get_ticks() - tempo_bloqueo >= DELAY_MS:
            for i, j in selecionadas:
                tabuleiro[i][j]["virado"] = False
            selecionadas = []
            bloqueado    = False

        # --- Desenho ---
        screen.fill(FUNDO)
        desenhar_tabuleiro(screen, tabuleiro, fonte_simbolo)
        desenhar_hud(screen, fonte_hud, tentativas, vitoria)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()