def recorde_melhor(novo, atual):
    if atual is None:
        return True

    if novo["tentativas"] < atual["tentativas"]:
        return True

    if novo["tentativas"] == atual["tentativas"]:
        return novo["tempo"] < atual["tempo"]

    return False


def salvar_recorde(caminho_arquivo, tentativas, tempo):
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{tentativas};{tempo}")


def carregar_recorde(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
    except FileNotFoundError:
        return None

    if conteudo == "":
        return None

    partes = conteudo.split(";")
    if len(partes) != 2:
        return None

    try:
        tentativas = int(partes[0])
        tempo = int(partes[1])
    except ValueError:
        return None

    if tentativas <= 0 or tempo < 0:
        return None

    return {"tentativas": tentativas, "tempo": tempo}
