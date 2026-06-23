# Documento de Projeto
## Sistema de Pedidos — Lanchonete (UFRA São Miguel)

**Versão:** 1.0

## 1. Estrutura atual (v1.0)
```
aula02/
└── pedidos.py        ← tela + regras + dados, tudo num arquivo só
```

## 2. Decisão pendente
A v1.0 é um **monolito**: funciona, mas não atende os RNF de manutenibilidade,
testabilidade e extensibilidade (ver `requisitos.md`).

**Qual estilo de arquitetura adotar?** Essa é a decisão da Atividade 2 — a ser
registrada em um **ADR** (Architecture Decision Record). O esqueleto em camadas para
você completar está em `template/`.
