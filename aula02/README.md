# Aula 2 — Arquitetura, ADR, UML e Princípios de Projeto

**Domínio desta aula:** sistema de pedidos de uma lanchonete (CLI).

> **Ponto de partida:** este código faz o controle de pedidos, mas está **todo num arquivo só** (tela + regras + dados). **O problema a tratar hoje:** que arquitetura dar a ele, como justificá-la (pelos RNF) e que classes/fronteiras moram em cada camada.

## Como rodar (o ponto de partida)

No terminal do **GitHub Codespaces**:

```bash
cd aula02
python pedidos.py
```

Menu: `1-Novo  2-Adicionar item  3-Fechar  4-Listar  0-Sair`.

## Conteúdo

- `pedidos.py` — o **ponto de partida**: o sistema inteiro num arquivo só (monolito).
- `docs/` — visão e requisitos (com os requisitos não funcionais que justificam a arquitetura).
- `template/` — o **esqueleto em camadas para você completar** (a Parte B da atividade).

> O roteiro da atividade, o questionário e os slides estão no **SIGAA**. Aqui no GitHub fica só o código.
