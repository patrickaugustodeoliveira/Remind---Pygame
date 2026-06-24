

import os

import pygame

SIMBOLOS_FRUTAS = ["maca", "banana", "uva", "morango", "laranja", "limao", "cereja", "abacaxi"]

_EMOJI_MAP = {
    "maca": "\U0001F34E",
    "banana": "\U0001F34C",
    "uva": "\U0001F347",
    "morango": "\U0001F353",
    "laranja": "\U0001F34A",
    "limao": "\U0001F34B",
    "cereja": "\U0001F352",
    "abacaxi": "\U0001F34D",
}

_CAMINHO_FONTE = None


def _iniciar_fonte():
    global _CAMINHO_FONTE
    if _CAMINHO_FONTE is not None:
        return
    for caminho in ["C:/Windows/Fonts/seguiemj.ttf", "C:/Windows/Fonts/seguiemj.ttc"]:
        if os.path.exists(caminho):
            _CAMINHO_FONTE = caminho
            return
    _CAMINHO_FONTE = ""


def _renderizar_emoji(surface, emoji, rect):
    global _CAMINHO_FONTE
    _iniciar_fonte()
    if not _CAMINHO_FONTE:
        return
    tamanho = int(min(rect.width, rect.height) * 0.75)
    font = pygame.font.Font(_CAMINHO_FONTE, tamanho)
    surf_emoji = font.render(emoji, True, (255, 255, 255))
    x = rect.centerx - surf_emoji.get_width() // 2
    y = rect.centery - surf_emoji.get_height() // 2
    surface.blit(surf_emoji, (x, y))


def desenhar_maca(surface, rect):
    _renderizar_emoji(surface, _EMOJI_MAP["maca"], rect)


def desenhar_banana(surface, rect):
    _renderizar_emoji(surface, _EMOJI_MAP["banana"], rect)


def desenhar_uva(surface, rect):
    _renderizar_emoji(surface, _EMOJI_MAP["uva"], rect)


def desenhar_morango(surface, rect):
    _renderizar_emoji(surface, _EMOJI_MAP["morango"], rect)


def desenhar_laranja(surface, rect):
    _renderizar_emoji(surface, _EMOJI_MAP["laranja"], rect)


def desenhar_limao(surface, rect):
    _renderizar_emoji(surface, _EMOJI_MAP["limao"], rect)


def desenhar_cereja(surface, rect):
    _renderizar_emoji(surface, _EMOJI_MAP["cereja"], rect)


def desenhar_abacaxi(surface, rect):
    _renderizar_emoji(surface, _EMOJI_MAP["abacaxi"], rect)


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
    funcao = DESENHOS.get(simbolo)
    if funcao:
        funcao(surface, rect)
