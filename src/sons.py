"""Efeitos sonoros do jogo, sintetizados por codigo (sem arquivos externos).

Gera pequenas formas de onda (bipes) usando numpy e as converte em
pygame.mixer.Sound. Isso evita depender de arquivos .wav/.mp3 externos,
que poderiam faltar ou ter problemas de licenca.

Se o mixer de audio nao estiver disponivel no sistema (ex: sem placa de
som), o jogo continua funcionando normalmente, apenas sem sons.
"""

import numpy as np
import pygame

TAXA_AMOSTRAGEM = 44100


def _gerar_tom(frequencia, duracao_s, volume=0.4, fade_out=True):
    """Gera uma onda senoidal simples como array numpy estereo int16."""
    n_amostras = int(TAXA_AMOSTRAGEM * duracao_s)
    t = np.linspace(0, duracao_s, n_amostras, endpoint=False)
    onda = np.sin(2 * np.pi * frequencia * t)

    if fade_out:
        # Aplica um fade-out suave para evitar "clique" no final do som
        envelope = np.linspace(1, 0, n_amostras) ** 1.5
        onda = onda * envelope

    onda = (onda * volume * 32767).astype(np.int16)
    estereo = np.column_stack([onda, onda])
    return np.ascontiguousarray(estereo)


def _gerar_glissando(freq_inicial, freq_final, duracao_s, volume=0.4):
    """Gera um tom que sobe ou desce de frequencia (efeito de 'whoosh')."""
    n_amostras = int(TAXA_AMOSTRAGEM * duracao_s)
    t = np.linspace(0, duracao_s, n_amostras, endpoint=False)
    freq_atual = np.linspace(freq_inicial, freq_final, n_amostras)
    fase = np.cumsum(2 * np.pi * freq_atual / TAXA_AMOSTRAGEM)
    onda = np.sin(fase)

    envelope = np.linspace(1, 0, n_amostras) ** 1.2
    onda = onda * envelope

    onda = (onda * volume * 32767).astype(np.int16)
    estereo = np.column_stack([onda, onda])
    return np.ascontiguousarray(estereo)


def _concatenar(*arrays):
    """Concatena varios arrays de som em sequencia."""
    return np.concatenate(arrays, axis=0)


class GerenciadorSons:
    """Carrega (sintetiza) e reproduz os efeitos sonoros do jogo."""

    def __init__(self):
        self.disponivel = False
        self.sons = {}
        self._inicializar()

    def _inicializar(self):
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=TAXA_AMOSTRAGEM, size=-16, channels=2)
            self._criar_sons()
            self.disponivel = True
        except pygame.error:
            # Sem dispositivo de audio disponivel no sistema: jogo continua sem som
            self.disponivel = False

    def _criar_sons(self):
        # Virar carta: bipe curto e agudo, sutil
        self.sons["virar"] = pygame.sndarray.make_sound(
            _gerar_tom(700, 0.07, volume=0.25)
        )

        # Acertar par: dois tons ascendentes (efeito de "sucesso")
        tom1 = _gerar_tom(523, 0.09, volume=0.3)   # Do
        tom2 = _gerar_tom(784, 0.14, volume=0.3)   # Sol
        self.sons["acertar"] = pygame.sndarray.make_sound(_concatenar(tom1, tom2))

        # Errar par: tom descendente curto (efeito sutil, nao punitivo)
        self.sons["errar"] = pygame.sndarray.make_sound(
            _gerar_glissando(330, 200, 0.18, volume=0.25)
        )

        # Vitoria: pequena sequencia de notas ascendentes (fanfarra simples)
        notas = [523, 659, 784, 1047]  # Do Mi Sol Do(8va)
        partes = [_gerar_tom(f, 0.13, volume=0.32) for f in notas]
        self.sons["vitoria"] = pygame.sndarray.make_sound(_concatenar(*partes))

        # Clique de botao (menu / jogar novamente): bipe neutro
        self.sons["clique"] = pygame.sndarray.make_sound(
            _gerar_tom(440, 0.06, volume=0.28)
        )

    def tocar(self, nome):
        """Toca o som pelo nome, se o audio estiver disponivel."""
        if not self.disponivel:
            return
        som = self.sons.get(nome)
        if som:
            som.play()


# Instancia unica reaproveitada pelo jogo inteiro
_gerenciador = None


def obter_gerenciador():
    """Retorna a instancia global do gerenciador de sons (cria na 1a chamada)."""
    global _gerenciador
    if _gerenciador is None:
        _gerenciador = GerenciadorSons()
    return _gerenciador