from modelos.pedido import Pedido


class PedidoRepo:
    """Camada de persistência: guarda e busca pedidos (em memória)."""

    def __init__(self) -> None:
        self._pedidos: list[Pedido] = []

    def salvar(self, pedido: Pedido) -> None:
        for i, p in enumerate(self._pedidos):
            if p.id == pedido.id:
                self._pedidos[i] = pedido
                return
        self._pedidos.append(pedido)

    def buscar(self, pedido_id: int):
        for p in self._pedidos:
            if p.id == pedido_id:
                return p
        return None

    def listar(self) -> list:
        return list(self._pedidos)

    def proximo_id(self) -> int:
        return len(self._pedidos) + 1