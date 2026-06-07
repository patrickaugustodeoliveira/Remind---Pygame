# Remind

Projeto final da disciplina de Introdução a Algoritmos/Programação desenvolvido com Python e Pygame.

## Integrantes do grupo

* Patrick Augusto de Oliveira
* Fernando Rodrigues Figueiredo
* Pedro Arthur de Sena Ribeiro
* Luis Fernando de Sousa Dias

## Estrutura do projeto

* `main.py`: ponto de entrada da aplicação.
* `src/`: código-fonte principal do jogo.
* `assets/`: imagens, fontes e sons.
* `data/`: armazenamento de recordes e configurações.
* `tests/`: testes unitários com pytest.
* `docs/`: documentação e proposta do projeto.

## Descrição do jogo

Remind é um jogo da memória desenvolvido em Python utilizando a biblioteca Pygame.

O jogador deve encontrar todos os pares de cartas escondidas no tabuleiro. As cartas são embaralhadas aleatoriamente no início de cada partida, exigindo atenção e memória para localizar os pares corretos.

O objetivo é concluir o jogo com o menor número possível de tentativas e no menor tempo.

## Objetivo do jogador

Encontrar todos os pares de cartas do tabuleiro antes de finalizar a partida, utilizando o menor número de jogadas possível.

## Regras do jogo

* Todas as cartas iniciam viradas para baixo.
* O jogador pode revelar duas cartas por vez.
* Cartas iguais permanecem abertas.
* Cartas diferentes são ocultadas novamente.
* Cada tentativa é contabilizada.
* O jogo termina quando todos os pares forem encontrados.

## Controles

* Clique esquerdo do mouse: revelar carta.
* ESC: sair do jogo.

## Funcionalidades previstas

* Tela inicial.
* Tabuleiro embaralhado aleatoriamente.
* Sistema de pares.
* Contador de tentativas.
* Cronômetro.
* Tela de vitória.
* Sistema de recordes.
* Salvamento de dados em arquivo.

## Estruturas de dados utilizadas

* Listas.
* Matrizes.
* Dicionários.
* Tuplas.

## Como executar o projeto

### Clonar o repositório

```bash
git clone https://github.com/patrickaugustodeoliveira/Remind---Pygame.git
cd Remind---Pygame
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar o jogo

```bash
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

* [x] Definição do jogo.
* [x] Proposta inicial documentada.
* [x] Protótipo funcional.
* [ ] Sistema de cartas.
* [ ] Sistema de pontuação.
* [ ] Persistência de dados.
* [ ] Testes implementados.

## Cronograma

### Semana 1

Definição da proposta e organização do projeto.

### Semana 2

Implementação do protótipo inicial e tabuleiro.

### Semana 3

Implementação das regras principais e sistema de pontuação.

### Semana 4

Finalização, testes e preparação da apresentação.

## Licença

Projeto acadêmico desenvolvido para a disciplina de Introdução a Algoritmos/Programação da PUC Minas.
