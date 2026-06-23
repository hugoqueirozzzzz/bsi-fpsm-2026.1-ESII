# Documento de Visão
## Sistema de Pedidos — Lanchonete (UFRA São Miguel)

**Versão:** 1.0

## 1. Problema
O atendente anota os pedidos no papel; some pedido, erra conta, e não há histórico.

## 2. Solução proposta
Um sistema de linha de comando (CLI) para registrar pedidos, adicionar itens do
cardápio, fechar o pedido com o total calculado e listar os pedidos do dia.

## 3. Escopo (v1.0)
- Registro de pedidos e itens; cálculo do total; listagem.
- **Fora do escopo:** pagamento, estoque, impressão fiscal, múltiplas mesas.

## 4. Premissas
- Dados em memória (não há persistência entre execuções na v1.0).
- Cardápio fixo no código.
