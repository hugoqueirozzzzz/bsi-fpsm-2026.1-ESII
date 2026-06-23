# Documento de Requisitos
## Sistema de Pedidos — Lanchonete (UFRA São Miguel)

**Versão:** 1.0

## 1. Requisitos Funcionais
- **RF01 — Novo pedido:** registrar um pedido para um cliente.
- **RF02 — Adicionar item:** adicionar um item do cardápio (com quantidade) a um pedido aberto.
- **RF03 — Fechar pedido:** calcular o total e marcar o pedido como fechado.
- **RF04 — Listar pedidos:** exibir os pedidos com cliente, estado e total.

### Regras de negócio
- **RN01:** o total do pedido é a soma de (preço × quantidade) de cada item.
- **RN02:** um pedido fechado não pode receber novos itens.

## 2. Requisitos Não Funcionais (RNF)

> Estes RNF são o **critério para a decisão de arquitetura** (Atividade 2).

- **RNF01 — Desempenho:** responder a qualquer operação em menos de 1 segundo.
- **RNF02 — Usabilidade:** menu textual claro, mensagens de erro descritivas.
- **RNF03 — Manutenibilidade:** adicionar uma nova saída (ex.: um relatório de vendas)
  não deve exigir mexer em todo o sistema.
  > **Observação do analista:** não atendido na v1.0 (tudo está acoplado num arquivo).
- **RNF04 — Testabilidade:** as regras de negócio (ex.: cálculo do total) devem poder
  ser testadas sem depender da entrada do usuário.
  > **Observação do analista:** não atendido na v1.0 (a regra está dentro do `input()`).
- **RNF05 — Extensibilidade:** trocar a forma de guardar os dados (lista → arquivo → banco)
  não deve impactar as regras de negócio.
  > **Observação do analista:** não atendido na v1.0 (regra e dados estão grudados).
