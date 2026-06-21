# Testes

Esta pasta contem testes automatizados do projeto.

## Arquivos

- `test_logica.py`: valida regras do tabuleiro, vitoria e recorde.

## Como executar

```bash
python3 -m pytest
```

## Boas praticas

- Crie testes para toda regra de progresso, recorde e condicoes de fim de jogo.
- Prefira funcoes pequenas e testaveis nos modulos `src/jogo.py` e `src/dados.py`.
