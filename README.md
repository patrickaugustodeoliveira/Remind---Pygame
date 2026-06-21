# Remind

Projeto final da disciplina de Introducao a Algoritmos/Programacao desenvolvido com Python e Pygame.

## Integrantes do grupo

* Patrick Augusto de Oliveira
* Fernando Rodrigues Figueiredo
* Pedro Arthur de Sena Ribeiro
* Luis Fernando de Sousa Dias

## Descricao do jogo

Remind e um jogo da memoria. O jogador deve encontrar todos os pares de cartas escondidas no tabuleiro. As cartas sao embaralhadas no inicio de cada partida, exigindo atencao e memoria para localizar os pares corretos.

O objetivo e vencer com o menor numero de tentativas possivel. Em caso de empate nas tentativas, o menor tempo fica como melhor recorde.

## Regras do jogo

* Todas as cartas iniciam viradas para baixo.
* O jogador pode revelar duas cartas por vez.
* Cartas iguais permanecem abertas.
* Cartas diferentes sao ocultadas novamente apos um pequeno intervalo.
* Cada par de cartas revelado conta como uma tentativa.
* O progresso mostra quantos pares ja foram encontrados.
* O jogo termina com vitoria quando todos os pares forem encontrados.
* Nao ha condicao de derrota nesta versao; a condicao de encerramento e a vitoria.

## Controles

* Clique esquerdo do mouse: revelar carta.
* ESC: sair do jogo.
* Fechar janela: sair do jogo.

## Sistemas implementados

* Tabuleiro 4x4 embaralhado.
* Sistema de pares.
* Contador de tentativas.
* Cronometro.
* Indicador de progresso.
* Tela/mensagem de vitoria.
* Recorde salvo em arquivo.
* Testes automatizados da logica principal.

## Estruturas de dados utilizadas

* Listas.
* Matrizes.
* Dicionarios.
* Tuplas.

## Estrutura do projeto

* `main.py`: ponto de entrada da aplicacao.
* `src/jogo.py`: loop principal, eventos, renderizacao e regras do jogo.
* `src/dados.py`: leitura, escrita e comparacao de recordes.
* `src/config.py`: caminhos e constantes compartilhadas.
* `data/recorde.txt`: melhor resultado salvo em texto.
* `tests/`: testes unitarios com pytest.
* `docs/`: documentacao e proposta do projeto.

## Como executar o projeto

### Instalar dependencias

```bash
python3 -m pip install -r requirements.txt
```

### Executar o jogo

```bash
python3 main.py
```

## Como executar os testes

```bash
python3 -m pytest
```

## Formato do recorde

O arquivo `data/recorde.txt` usa o formato:

```text
tentativas;tempo_em_segundos
```

Exemplo:

```text
12;75
```

## Checklist minimo para entrega

* [x] Implementacao das principais interacoes.
* [x] Sistema de pontuacao/progresso com tentativas, tempo e pares encontrados.
* [x] Condicao de vitoria/encerramento.
* [x] Uso de estruturas de dados.
* [x] Leitura e escrita de dados em arquivo.
* [x] Primeira versao dos testes.
* [x] README atualizado com informacoes do jogo.

## Cronograma

### Semana 1

Definicao da proposta e organizacao do projeto.

### Semana 2

Implementacao do prototipo inicial e tabuleiro.

### Semana 3

Implementacao das regras principais, progresso, recorde e testes.

### Semana 4

Finalizacao, testes e preparacao da apresentacao.

## Licenca

Projeto academico desenvolvido para a disciplina de Introducao a Algoritmos/Programacao da PUC Minas.
