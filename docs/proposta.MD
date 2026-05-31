# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

Remind - Memory Game

---

## 2. Integrantes do grupo

* Nome 1: Patrick Augusto de Oliveira
* Nome 2: Fernando Rodrigues Figueiredo
* Nome 3: Pedro Arthur de Sena Ribeiro
* Nome 4: Luis Fernando de Sousa Dias

---

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Jogo da memória

---

## 4. Descrição geral do jogo

O jogo Remind é um jogo da memória desenvolvido com Python e Pygame.

Na tela, será exibido um tabuleiro com cartas viradas para baixo. O jogador interage com o jogo utilizando o mouse, clicando nas cartas para revelá-las.

O objetivo é encontrar os pares corretos de cartas iguais. Cada jogada permite virar duas cartas. Se forem iguais, permanecem abertas; se forem diferentes, voltam a ser escondidas.

---

## 5. Objetivo do jogador

O objetivo é encontrar todos os pares de cartas do tabuleiro no menor número possível de tentativas e no menor tempo possível.

---

## 6. Regras principais

* O jogador pode virar duas cartas por vez.
* Cartas iguais permanecem abertas.
* Cartas diferentes são viradas novamente.
* Cada tentativa é contabilizada.
* O jogo termina quando todos os pares forem encontrados.

---

## 7. Condição de vitória

O jogador vence quando encontrar todos os pares de cartas do tabuleiro.

---

## 8. Condição de derrota ou encerramento

O jogo é encerrado quando todos os pares forem encontrados.

Opcionalmente, poderá existir um limite de tempo para aumentar a dificuldade.

---

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

O jogador interage com o jogo utilizando o mouse para selecionar cartas no tabuleiro.

---

### Obstáculos, inimigos ou desafios

Não há inimigos. O principal desafio é a memória do jogador para lembrar a posição das cartas.

---

### Itens, alvos ou objetos de interação

Cartas do jogo, que devem ser viradas para encontrar pares iguais.

---

### Pontuação, vidas, tempo ou progresso

* Contador de tentativas
* Cronômetro opcional
* Sistema de recorde (melhor tempo e/ou menor número de tentativas)

---

## 10. Controles previstos

* Clique esquerdo do mouse: virar carta
* ESC: sair do jogo

---

## 11. Organização inicial do código

* `main.py`: ponto de entrada do jogo
* `src/game.py`: loop principal e lógica do jogo
* `src/cards.py`: criação e lógica das cartas
* `src/config.py`: configurações do jogo
* `src/utils.py`: funções auxiliares
* `data/records.json`: armazenamento de recordes

---

## 12. Recursos externos previstos

* Imagens simples para cartas (banco gratuito ou criação própria)
* Sons simples para acerto/erro (opcional)
* Fontes padrão do Pygame

---

## 13. Principais dificuldades esperadas

* Controle do estado das cartas (virada e comparação)
* Implementação do delay para esconder cartas diferentes
* Embaralhamento correto do tabuleiro
* Salvamento de recordes em arquivo
* Organização da lógica do jogo em funções

---

## 14. Escopo mínimo para a entrega final

A versão mínima do jogo terá:

* Tabuleiro funcional com cartas embaralhadas
* Sistema de virar cartas
* Verificação de pares
* Contador de tentativas
* Tela de vitória
* Estrutura organizada em arquivos
* Salvamento simples de recorde

---

## 15. Possíveis melhorias, caso haja tempo

* Sistema de ranking
* Diferentes níveis de dificuldade
* Mais cartas e tamanhos de tabuleiro
* Sons e animações
* Tela inicial com menu
* Sistema de tempo (timer)
