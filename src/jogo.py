import math
import random
import sys

import pygame

from src.config import CAMINHO_RECORDE
from src.dados import carregar_recorde, recorde_melhor, salvar_recorde
from src.desenhos import desenhar_fruta, SIMBOLOS_FRUTAS

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
DELAY_MS = 900

FUNDO_TOPO = (24, 32, 64)
FUNDO_BASE = (44, 58, 110)

COR_COSTAS = (60, 90, 200)
COR_COSTAS_BORDA = (40, 65, 160)
COR_VIRADA = (255, 255, 255)
COR_ACERTADA = (235, 250, 235)
COR_ACERTADA_BORDA = (70, 190, 100)
COR_BORDA = (15, 20, 40)
COR_TEXTO = (20, 20, 30)
COR_HUD = (235, 240, 255)
COR_HUD_SOMBRA = (10, 15, 30)
COR_DESTAQUE = (255, 220, 50)
COR_SOMBRA_CARTA = (10, 14, 30)

COR_BOTAO = (235, 165, 35)
COR_BOTAO_HOVER = (255, 185, 60)
COR_BOTAO_TEXTO = (30, 20, 10)

SIMBOLOS = SIMBOLOS_FRUTAS
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

BOTAO_LARGURA = 230
BOTAO_ALTURA = 46
BOTAO_X = (LARGURA - BOTAO_LARGURA) // 2
BOTAO_Y = ALTURA - 64
BOTAO_RECT = pygame.Rect(BOTAO_X, BOTAO_Y, BOTAO_LARGURA, BOTAO_ALTURA)

BOTAO_MENU_LARGURA = 220
BOTAO_MENU_ALTURA = 56
BOTAO_MENU_X = (LARGURA - BOTAO_MENU_LARGURA) // 2
BOTAO_MENU_Y = ALTURA // 2 + 40
BOTAO_MENU_RECT = pygame.Rect(BOTAO_MENU_X, BOTAO_MENU_Y, BOTAO_MENU_LARGURA, BOTAO_MENU_ALTURA)

ANIM_VIRAR_MS = 160


def criar_baralho(simbolos=None):
    simbolos = simbolos or SIMBOLOS
    return list(simbolos) * 2


def criar_tabuleiro(simbolos=None):
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
                    "anim_inicio": None,
                }
            )
        tabuleiro.append(linha)

    return tabuleiro


def contar_pares_acertados(tabuleiro):
    cartas_acertadas = sum(
        1 for linha in tabuleiro for carta in linha if carta["acertado"]
    )
    return cartas_acertadas // 2


def checar_vitoria(tabuleiro):
    return all(carta["acertado"] for linha in tabuleiro for carta in linha)


def formatar_tempo(segundos):
    minutos = segundos // 60
    restante = segundos % 60
    return f"{minutos:02d}:{restante:02d}"


def formatar_recorde(recorde):
    if recorde is None:
        return "Recorde: --"

    return (
        f"Recorde: {recorde['tentativas']} tent. "
        f"em {formatar_tempo(recorde['tempo'])}"
    )


def get_pos(linha, coluna):
    x = OFFSET_X + coluna * (CARD_W + MARGEM)
    y = OFFSET_Y + linha * (CARD_H + MARGEM)
    return x, y


def carta_clicada(mx, my):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            x, y = get_pos(linha, coluna)
            if x <= mx <= x + CARD_W and y <= my <= y + CARD_H:
                return linha, coluna
    return None


def medir_texto(texto, escala=2):
    return len(texto) * 6 * escala, 7 * escala


def desenhar_texto(surface, texto, cor, posicao, escala=2, sombra=None):
    if sombra is not None:
        x_s, y_s = posicao
        _desenhar_texto_simples(surface, texto, sombra, (x_s + 2, y_s + 2), escala)
    _desenhar_texto_simples(surface, texto, cor, posicao, escala)


def _desenhar_texto_simples(surface, texto, cor, posicao, escala):
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


def desenhar_fundo(surface):
    for y in range(ALTURA):
        frac = y / ALTURA
        r = int(FUNDO_TOPO[0] + (FUNDO_BASE[0] - FUNDO_TOPO[0]) * frac)
        g = int(FUNDO_TOPO[1] + (FUNDO_BASE[1] - FUNDO_TOPO[1]) * frac)
        b = int(FUNDO_TOPO[2] + (FUNDO_BASE[2] - FUNDO_TOPO[2]) * frac)
        pygame.draw.line(surface, (r, g, b), (0, y), (LARGURA, y))


def _largura_animada(carta, agora):
    if carta["anim_inicio"] is None:
        return 1.0
    decorrido = agora - carta["anim_inicio"]
    if decorrido >= ANIM_VIRAR_MS:
        return 1.0
    progresso = decorrido / ANIM_VIRAR_MS
    return abs(math.cos(progresso * math.pi))


def desenhar_carta(surface, carta, rect, agora):
    sombra_rect = rect.move(3, 4)
    pygame.draw.rect(surface, COR_SOMBRA_CARTA, sombra_rect, border_radius=12)

    escala_x = _largura_animada(carta, agora)
    largura_atual = max(int(rect.width * escala_x), 6)
    rect_animado = pygame.Rect(0, 0, largura_atual, rect.height)
    rect_animado.center = rect.center

    mostrar_frente = carta["virado"] or carta["acertado"]

    if carta["acertado"]:
        cor_fundo = COR_ACERTADA
        cor_borda = COR_ACERTADA_BORDA
    elif mostrar_frente:
        cor_fundo = COR_VIRADA
        cor_borda = COR_BORDA
    else:
        cor_fundo = COR_COSTAS
        cor_borda = COR_COSTAS_BORDA

    pygame.draw.rect(surface, cor_fundo, rect_animado, border_radius=12)
    pygame.draw.rect(surface, cor_borda, rect_animado, width=3, border_radius=12)

    if escala_x > 0.35:
        if mostrar_frente:
            desenhar_fruta(surface, carta["simbolo"], rect_animado)
        else:
            _desenhar_padrao_costas(surface, rect_animado)


def _desenhar_padrao_costas(surface, rect):
    cx, cy = rect.center
    pontos = [
        (cx, rect.top + 14),
        (rect.right - 14, cy),
        (cx, rect.bottom - 14),
        (rect.left + 14, cy),
    ]
    if rect.width > 20:
        pygame.draw.polygon(surface, (255, 255, 255), pontos, width=2)
        pygame.draw.circle(surface, (255, 255, 255), (cx, cy), 6, width=2)


def desenhar_tabuleiro(surface, tabuleiro, agora):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            carta = tabuleiro[linha][coluna]
            x, y = get_pos(linha, coluna)
            rect = pygame.Rect(x, y, CARD_W, CARD_H)
            desenhar_carta(surface, carta, rect, agora)


def desenhar_painel_hud(surface):
    painel = pygame.Surface((LARGURA, 70), pygame.constants.SRCALPHA)
    painel.fill((10, 14, 30, 110))
    surface.blit(painel, (0, 0))


def desenhar_botao_jogar_novamente(surface, mouse_pos):
    hover = BOTAO_RECT.collidepoint(mouse_pos)
    cor = COR_BOTAO_HOVER if hover else COR_BOTAO

    sombra = BOTAO_RECT.move(2, 3)
    pygame.draw.rect(surface, (10, 14, 30), sombra, border_radius=10)
    pygame.draw.rect(surface, cor, BOTAO_RECT, border_radius=10)
    pygame.draw.rect(surface, (140, 90, 10), BOTAO_RECT, width=2, border_radius=10)

    texto = "JOGAR NOVAMENTE"
    largura, altura = medir_texto(texto, escala=2)
    desenhar_texto(
        surface,
        texto,
        COR_BOTAO_TEXTO,
        (
            BOTAO_RECT.x + (BOTAO_RECT.width - largura) // 2,
            BOTAO_RECT.y + (BOTAO_RECT.height - altura) // 2,
        ),
        escala=2,
    )
    return BOTAO_RECT


def desenhar_hud(surface, estado, mouse_pos):
    desenhar_painel_hud(surface)

    desenhar_texto(
        surface,
        f"Tentativas: {estado['tentativas']}",
        COR_HUD,
        (10, 10),
        escala=2,
        sombra=COR_HUD_SOMBRA,
    )
    desenhar_texto(
        surface,
        f"Tempo: {formatar_tempo(estado['tempo'])}",
        COR_HUD,
        (200, 10),
        escala=2,
        sombra=COR_HUD_SOMBRA,
    )
    desenhar_texto(
        surface,
        f"Pares: {estado['pares_acertados']}/{TOTAL_PARES}",
        COR_HUD,
        (370, 10),
        escala=2,
        sombra=COR_HUD_SOMBRA,
    )
    desenhar_texto(
        surface,
        formatar_recorde(estado["recorde"]),
        COR_HUD,
        (10, 38),
        escala=2,
        sombra=COR_HUD_SOMBRA,
    )

    if estado["vitoria"]:
        painel = pygame.Surface((LARGURA, ALTURA - BOTAO_Y + 64), pygame.constants.SRCALPHA)
        painel.fill((10, 14, 30, 150))
        surface.blit(painel, (0, BOTAO_Y - 64))

        mensagem = "PARABENS! VOCE VENCEU!"
        largura, altura = medir_texto(mensagem, escala=3)
        desenhar_texto(
            surface,
            mensagem,
            COR_DESTAQUE,
            ((LARGURA - largura) // 2, BOTAO_Y - altura - 16),
            escala=3,
            sombra=(60, 40, 0),
        )
        desenhar_botao_jogar_novamente(surface, mouse_pos)


def desenhar_botao_generico(surface, rect, texto, mouse_pos, cor_normal, cor_hover, cor_texto, cor_borda):
    hover = rect.collidepoint(mouse_pos)
    cor = cor_hover if hover else cor_normal

    sombra = rect.move(2, 3)
    pygame.draw.rect(surface, (10, 14, 30), sombra, border_radius=10)
    pygame.draw.rect(surface, cor, rect, border_radius=10)
    pygame.draw.rect(surface, cor_borda, rect, width=2, border_radius=10)

    largura, altura = medir_texto(texto, escala=2)
    desenhar_texto(
        surface,
        texto,
        cor_texto,
        (rect.x + (rect.width - largura) // 2, rect.y + (rect.height - altura) // 2),
        escala=2,
    )


def desenhar_menu(surface, mouse_pos, recorde, agora):
    desenhar_fundo(surface)

    decoracoes = [
        ("maca", 90, 70), ("banana", 200, 60), ("uva", 310, 75),
        ("morango", 420, 60), ("laranja", 530, 72),
    ]
    for simbolo, x, y_base in decoracoes:
        offset = math.sin((agora / 450) + x) * 6
        rect = pygame.Rect(0, 0, 70, 70)
        rect.center = (x, y_base + offset)
        desenhar_fruta(surface, simbolo, rect)

    titulo = "REMIND"
    largura, altura = medir_texto(titulo, escala=6)
    desenhar_texto(
        surface,
        titulo,
        COR_DESTAQUE,
        ((LARGURA - largura) // 2, 150),
        escala=6,
        sombra=(60, 40, 0),
    )

    subtitulo = "JOGO DA MEMORIA"
    largura_sub, _ = medir_texto(subtitulo, escala=2)
    desenhar_texto(
        surface,
        subtitulo,
        COR_HUD,
        ((LARGURA - largura_sub) // 2, 210),
        escala=2,
        sombra=COR_HUD_SOMBRA,
    )

    texto_recorde = formatar_recorde(recorde)
    largura_rec, _ = medir_texto(texto_recorde, escala=2)
    desenhar_texto(
        surface,
        texto_recorde,
        COR_HUD,
        ((LARGURA - largura_rec) // 2, BOTAO_MENU_Y - 40),
        escala=2,
        sombra=COR_HUD_SOMBRA,
    )

    desenhar_botao_generico(
        surface, BOTAO_MENU_RECT, "JOGAR",
        mouse_pos, COR_BOTAO, COR_BOTAO_HOVER, COR_BOTAO_TEXTO, (140, 90, 10),
    )

    dica = "ESC PARA SAIR"
    largura_dica, _ = medir_texto(dica, escala=1)
    desenhar_texto(
        surface,
        dica,
        (160, 175, 220),
        ((LARGURA - largura_dica) // 2, ALTURA - 30),
        escala=1,
    )


def novo_jogo_estado(recorde):
    return {
        "tabuleiro": criar_tabuleiro(),
        "selecionadas": [],
        "tentativas": 0,
        "bloqueado": False,
        "tempo_bloqueio": 0,
        "vitoria": False,
        "inicio_ticks": pygame.time.get_ticks(),
        "tempo_final": 0,
        "recorde": recorde,
    }


def _processar_par(jogo, recorde, agora):
    linha_1, coluna_1 = jogo["selecionadas"][0]
    linha_2, coluna_2 = jogo["selecionadas"][1]
    carta_1 = jogo["tabuleiro"][linha_1][coluna_1]
    carta_2 = jogo["tabuleiro"][linha_2][coluna_2]

    if carta_1["simbolo"] == carta_2["simbolo"]:
        carta_1["acertado"] = True
        carta_2["acertado"] = True
        jogo["selecionadas"] = []
        jogo["vitoria"] = checar_vitoria(jogo["tabuleiro"])

        if jogo["vitoria"]:
            jogo["tempo_final"] = (agora - jogo["inicio_ticks"]) // 1000
            novo_recorde = {
                "tentativas": jogo["tentativas"],
                "tempo": jogo["tempo_final"],
            }
            if recorde_melhor(novo_recorde, recorde):
                salvar_recorde(CAMINHO_RECORDE, novo_recorde["tentativas"], novo_recorde["tempo"])
                recorde = novo_recorde
                jogo["recorde"] = novo_recorde
    else:
        jogo["bloqueado"] = True
        jogo["tempo_bloqueio"] = agora

    return recorde


def executar_jogo():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Remind - Jogo da Memoria")
    relogio = pygame.time.Clock()

    recorde = carregar_recorde(CAMINHO_RECORDE)
    estado_app = "menu"
    jogo = None

    while True:
        agora = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            sair = event.type == pygame.QUIT
            sair = sair or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
            if sair:
                pygame.quit()
                sys.exit()

            if event.type != pygame.MOUSEBUTTONDOWN:
                continue

            if estado_app == "menu":
                if BOTAO_MENU_RECT.collidepoint(event.pos):
                    jogo = novo_jogo_estado(recorde)
                    estado_app = "jogando"
                continue

            if jogo["vitoria"]:
                if BOTAO_RECT.collidepoint(event.pos):
                    jogo = novo_jogo_estado(recorde)
                continue

            if jogo["bloqueado"]:
                continue

            pos = carta_clicada(*event.pos)
            if pos is None:
                continue

            linha, coluna = pos
            carta = jogo["tabuleiro"][linha][coluna]
            if carta["virado"] or carta["acertado"] or pos in jogo["selecionadas"]:
                continue

            carta["virado"] = True
            carta["anim_inicio"] = agora
            jogo["selecionadas"].append(pos)

            if len(jogo["selecionadas"]) == 2:
                jogo["tentativas"] += 1
                recorde = _processar_par(jogo, recorde, agora)

        if estado_app == "menu":
            desenhar_menu(tela, mouse_pos, recorde, agora)
            pygame.display.flip()
            relogio.tick(FPS)
            continue

        tabuleiro = jogo["tabuleiro"]
        tempo_atual = jogo["tempo_final"] if jogo["vitoria"] else (agora - jogo["inicio_ticks"]) // 1000

        if jogo["bloqueado"] and agora - jogo["tempo_bloqueio"] >= DELAY_MS:
            for linha, coluna in jogo["selecionadas"]:
                tabuleiro[linha][coluna]["virado"] = False
                tabuleiro[linha][coluna]["anim_inicio"] = agora
            jogo["selecionadas"] = []
            jogo["bloqueado"] = False

        estado = {
            "tentativas": jogo["tentativas"],
            "tempo": tempo_atual,
            "pares_acertados": contar_pares_acertados(tabuleiro),
            "recorde": jogo["recorde"],
            "vitoria": jogo["vitoria"],
        }

        desenhar_fundo(tela)
        desenhar_tabuleiro(tela, tabuleiro, agora)
        desenhar_hud(tela, estado, mouse_pos)
        pygame.display.flip()
        relogio.tick(FPS)


        