"""Desenhos vetoriais (frutinhas) usados nas cartas do jogo da memoria.

Cada funcao recebe a surface, o retangulo da carta e desenha a fruta
centralizada usando apenas formas geometricas do pygame (sem precisar
de nenhuma imagem externa).
"""

import math

import pygame

# Um simbolo (fruta) para cada uma das 8 cartas do jogo
SIMBOLOS_FRUTAS = ["maca", "banana", "uva", "morango", "laranja", "limao", "cereja", "abacaxi"]


def _centro(rect):
    return rect.centerx, rect.centery


def desenhar_maca(surface, rect):
    cx, cy = _centro(rect)
    raio = rect.width // 3
    cor_corpo = (220, 40, 50)
    cor_sombra = (180, 25, 35)

    # Corpo (dois circulos sobrepostos pra parecer uma maca)
    pygame.draw.circle(surface, cor_corpo, (cx - raio // 3, cy + 2), raio)
    pygame.draw.circle(surface, cor_corpo, (cx + raio // 3, cy + 2), raio)
    pygame.draw.circle(surface, cor_sombra, (cx, cy + raio - 4), raio - 6, width=0)
    pygame.draw.circle(surface, cor_corpo, (cx, cy), raio + 2)

    # Cabinho
    pygame.draw.line(surface, (90, 60, 30), (cx, cy - raio), (cx + 4, cy - raio - 10), 3)
    # Folha
    folha = [(cx + 4, cy - raio - 8), (cx + 18, cy - raio - 14), (cx + 8, cy - raio - 2)]
    pygame.draw.polygon(surface, (60, 150, 60), folha)


def desenhar_banana(surface, rect):
    cx, cy = _centro(rect)
    cor = (245, 210, 40)
    cor_ponta = (110, 80, 30)

    pontos_externos = []
    pontos_internos = []
    largura = rect.width // 2.6

    for t in range(0, 101, 5):
        frac = t / 100
        angulo = math.pi * 0.75 * frac - math.pi * 0.05
        x = cx - largura + frac * largura * 2.1
        y = cy + math.sin(frac * math.pi) * -largura * 0.9 + largura * 0.3
        pontos_externos.append((x, y - 8))
        pontos_internos.append((x, y + 8))

    polig = pontos_externos + pontos_internos[::-1]
    pygame.draw.polygon(surface, cor, polig)
    pygame.draw.polygon(surface, (200, 170, 20), polig, width=2)

    # pontas escuras
    pygame.draw.circle(surface, cor_ponta, pontos_externos[0], 5)
    pygame.draw.circle(surface, cor_ponta, pontos_internos[-1], 5)


def desenhar_uva(surface, rect):
    cx, cy = _centro(rect)
    cor = (130, 80, 180)
    cor_clara = (160, 110, 205)
    raio = rect.width // 9

    offsets = [
        (0, -raio * 2.1),
        (-raio * 1.7, -raio * 0.6), (raio * 1.7, -raio * 0.6),
        (-raio * 0.9, raio * 0.8), (raio * 0.9, raio * 0.8),
        (-raio * 2.4, raio * 0.9), (raio * 2.4, raio * 0.9),
        (0, raio * 2.3),
    ]
    for ox, oy in offsets:
        pygame.draw.circle(surface, cor, (cx + ox, cy + oy), raio)
        pygame.draw.circle(surface, cor_clara, (cx + ox - raio * 0.3, cy + oy - raio * 0.3), raio * 0.35)

    # cabinho
    pygame.draw.line(surface, (60, 130, 50), (cx, cy - raio * 3), (cx, cy - raio * 3.6), 3)


def desenhar_morango(surface, rect):
    cx, cy = _centro(rect)
    cor = (230, 30, 60)
    raio = rect.width // 3

    pontos = [
        (cx - raio, cy - raio * 0.3),
        (cx, cy + raio * 1.1),
        (cx + raio, cy - raio * 0.3),
    ]
    # corpo em forma de coracao/triangulo arredondado
    pygame.draw.polygon(surface, cor, pontos)
    pygame.draw.circle(surface, cor, (cx - raio * 0.55, cy - raio * 0.35), raio * 0.55)
    pygame.draw.circle(surface, cor, (cx + raio * 0.55, cy - raio * 0.35), raio * 0.55)

    # sementinhas
    for sx, sy in [(-0.35, -0.05), (0.35, -0.05), (0, 0.35), (-0.2, 0.55), (0.2, 0.55)]:
        pygame.draw.circle(surface, (250, 230, 140), (cx + sx * raio, cy + sy * raio), 2)

    # folhinhas verdes no topo
    for ang in (-40, 0, 40):
        rad = math.radians(ang)
        ponta = (cx + math.sin(rad) * raio * 0.6, cy - raio * 1.0 - math.cos(rad) * 6)
        pygame.draw.polygon(
            surface, (70, 160, 70),
            [(cx, cy - raio * 0.55), (ponta[0], ponta[1]), (cx + math.sin(rad) * raio * 0.2, cy - raio * 0.7)]
        )


def desenhar_laranja(surface, rect):
    cx, cy = _centro(rect)
    raio = rect.width // 3
    pygame.draw.circle(surface, (245, 140, 30), (cx, cy), raio)
    pygame.draw.circle(surface, (220, 115, 15), (cx, cy), raio, width=2)

    # gomos (linhas saindo do centro)
    for ang in range(0, 360, 45):
        rad = math.radians(ang)
        ponta = (cx + math.cos(rad) * raio, cy + math.sin(rad) * raio)
        pygame.draw.line(surface, (220, 115, 15), (cx, cy), ponta, 1)

    # folhinha
    pygame.draw.circle(surface, (250, 165, 50), (cx, cy - raio - 4), 4)


def desenhar_limao(surface, rect):
    cx, cy = _centro(rect)
    raio_x = rect.width // 3
    raio_y = rect.height // 3.4
    cor = (190, 220, 60)

    oval = pygame.Rect(0, 0, raio_x * 2, raio_y * 2)
    oval.center = (cx, cy)
    pygame.draw.ellipse(surface, cor, oval)
    pygame.draw.ellipse(surface, (150, 180, 40), oval, width=2)

    # pontinhas do limao
    pygame.draw.circle(surface, cor, (cx - raio_x, cy), 4)
    pygame.draw.circle(surface, cor, (cx + raio_x, cy), 4)


def desenhar_cereja(surface, rect):
    cx, cy = _centro(rect)
    raio = rect.width // 7
    cor = (200, 20, 40)

    c1 = (cx - raio * 1.4, cy + raio * 1.4)
    c2 = (cx + raio * 1.4, cy + raio * 1.6)

    # hastes
    pygame.draw.line(surface, (70, 140, 50), (cx, cy - raio * 3), c1, 3)
    pygame.draw.line(surface, (70, 140, 50), (cx, cy - raio * 3), c2, 3)

    pygame.draw.circle(surface, cor, c1, raio)
    pygame.draw.circle(surface, cor, c2, raio)
    pygame.draw.circle(surface, (235, 90, 100), (c1[0] - 3, c1[1] - 3), raio * 0.35)
    pygame.draw.circle(surface, (235, 90, 100), (c2[0] - 3, c2[1] - 3), raio * 0.35)

    # folhinha
    folha = [(cx, cy - raio * 3), (cx + 14, cy - raio * 3 - 8), (cx + 4, cy - raio * 2.6)]
    pygame.draw.polygon(surface, (70, 150, 60), folha)


def desenhar_abacaxi(surface, rect):
    cx, cy = _centro(rect)
    raio_x = rect.width // 3.2
    raio_y = rect.height // 3.2

    corpo = pygame.Rect(0, 0, raio_x * 2, raio_y * 1.9)
    corpo.center = (cx, cy + raio_y * 0.45)
    pygame.draw.ellipse(surface, (240, 195, 60), corpo)
    pygame.draw.ellipse(surface, (210, 165, 40), corpo, width=2)

    # textura em losango
    for i in range(-1, 2):
        for j in range(-1, 2):
            px = cx + i * raio_x * 0.5
            py = cy + raio_y * 0.45 + j * raio_y * 0.4
            if corpo.collidepoint(px, py):
                pygame.draw.circle(surface, (210, 165, 40), (px, py), 2)

    # coroa de folhas (mais alta e destacada, acima do corpo)
    topo_y = corpo.top
    for ang in (-35, -15, 0, 15, 35):
        rad = math.radians(ang)
        base = (cx, topo_y + 4)
        ponta = (cx + math.sin(rad) * raio_x * 0.8, topo_y - raio_y * 1.1)
        lado_esq = (cx - 4 + math.sin(rad) * raio_x * 0.3, topo_y - raio_y * 0.3)
        lado_dir = (cx + 4 + math.sin(rad) * raio_x * 0.3, topo_y - raio_y * 0.3)
        pygame.draw.polygon(surface, (65, 145, 60), [lado_esq, ponta, lado_dir])


DESENHOS = {
    "maca": desenhar_maca,
    "banana": desenhar_banana,
    "uva": desenhar_uva,
    "morango": desenhar_morango,
    "laranja": desenhar_laranja,
    "limao": desenhar_limao,
    "cereja": desenhar_cereja,
    "abacaxi": desenhar_abacaxi,
}


def desenhar_fruta(surface, simbolo, rect):
    """Desenha a fruta correspondente ao simbolo dentro do retangulo informado."""
    funcao = DESENHOS.get(simbolo)
    if funcao:
        funcao(surface, rect)