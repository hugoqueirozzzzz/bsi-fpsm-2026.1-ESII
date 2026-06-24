# pedidos.py — Sistema de Pedidos (v1.0) — TUDO num arquivo só (monolito)
# Tela (CLI), regras de negócio e dados moram juntos. Funciona — mas é frágil.

# --- estado global (dados) ---
cardapio = [
    {"nome": "X-Burguer",     "preco": 18.0},
    {"nome": "Refrigerante",  "preco": 6.0},
    {"nome": "Batata frita",  "preco": 12.0},
]
pedidos = []  # cada pedido: {"id", "cliente", "itens": [...], "fechado": bool}


def novo_pedido():
    cliente = input("Cliente: ")
    pedido = {"id": len(pedidos) + 1, "cliente": cliente, "itens": [], "fechado": False}
    pedidos.append(pedido)
    print(f"Pedido {pedido['id']} criado para {cliente}.")


def adicionar_item():
    pid = int(input("ID do pedido: "))
    pedido = None
    for p in pedidos:               # acessa a lista global direto
        if p["id"] == pid:
            pedido = p
    if pedido is None or pedido["fechado"]:
        print("Pedido inválido ou já fechado")
        return
    for i, item in enumerate(cardapio, 1):
        print(f"{i}- {item['nome']} (R${item['preco']:.2f})")
    escolha = int(input("Item: ")) - 1
    qtd = int(input("Quantidade: "))
    item = cardapio[escolha]
    pedido["itens"].append({"nome": item["nome"], "preco": item["preco"], "qtd": qtd})
    print("Item adicionado.")


def fechar_pedido():
    pid = int(input("ID do pedido: "))
    pedido = None
    for p in pedidos:
        if p["id"] == pid:
            pedido = p
    if pedido is None:
        print("Pedido inválido")
        return
    # cálculo do total (regra de negócio) no meio da interface:
    total = 0.0
    for item in pedido["itens"]:
        total += item["preco"] * item["qtd"]
    pedido["fechado"] = True
    print(f"Pedido {pid} fechado. Total: R${total:.2f}")


def listar_pedidos():
    for p in pedidos:
        total = sum(i["preco"] * i["qtd"] for i in p["itens"])   # regra repetida aqui
        estado = "fechado" if p["fechado"] else "aberto"
        print(f"#{p['id']} {p['cliente']} — {estado} — R${total:.2f}")


def main():
    while True:
        print("\n1-Novo  2-Adicionar item  3-Fechar  4-Listar  0-Sair")
        op = input("Opção: ")
        if op == "1":   novo_pedido()
        elif op == "2": adicionar_item()
        elif op == "3": fechar_pedido()
        elif op == "4": listar_pedidos()
        elif op == "0": break


if __name__ == "__main__":
    main()
