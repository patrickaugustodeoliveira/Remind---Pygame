from pathlib import Path

LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Projeto Final - Pygame"

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)

_RAIZ_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_RECORDE = str(_RAIZ_PROJETO / "data" / "recorde.txt")
