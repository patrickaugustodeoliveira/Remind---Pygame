from collections import Counter

from src.dados import carregar_recorde, recorde_melhor, salvar_recorde
from src.jogo import checar_vitoria, criar_tabuleiro


def test_tabuleiro_tem_16_cartas_e_8_pares():
    tabuleiro = criar_tabuleiro()
    cartas = [carta["simbolo"] for linha in tabuleiro for carta in linha]
    contagem = Counter(cartas)

    assert len(cartas) == 16
    assert len(contagem) == 8
    assert all(total == 2 for total in contagem.values())


def test_checar_vitoria_falso_quando_existem_cartas_nao_acertadas():
    tabuleiro = criar_tabuleiro()

    assert checar_vitoria(tabuleiro) is False


def test_checar_vitoria_verdadeiro_quando_todas_cartas_foram_acertadas():
    tabuleiro = criar_tabuleiro()
    for linha in tabuleiro:
        for carta in linha:
            carta["acertado"] = True

    assert checar_vitoria(tabuleiro) is True


def test_recorde_melhor_prefere_menos_tentativas():
    atual = {"tentativas": 12, "tempo": 80}
    novo = {"tentativas": 10, "tempo": 120}

    assert recorde_melhor(novo, atual) is True


def test_recorde_melhor_usa_tempo_como_desempate():
    atual = {"tentativas": 10, "tempo": 80}
    novo = {"tentativas": 10, "tempo": 60}

    assert recorde_melhor(novo, atual) is True


def test_recorde_melhor_recusa_resultado_pior():
    atual = {"tentativas": 10, "tempo": 80}
    novo = {"tentativas": 11, "tempo": 30}

    assert recorde_melhor(novo, atual) is False


def test_carregar_recorde_invalido_retorna_none(tmp_path):
    caminho = tmp_path / "recorde.txt"
    caminho.write_text("15", encoding="utf-8")

    assert carregar_recorde(caminho) is None


def test_salvar_e_carregar_recorde(tmp_path):
    caminho = tmp_path / "recorde.txt"

    salvar_recorde(caminho, 14, 90)

    assert carregar_recorde(caminho) == {"tentativas": 14, "tempo": 90}
