from modelos.pedido import Pedido


class PedidoRepo:
    """Camada de persistência: guarda e busca pedidos (em memória)."""

    def __init__(self) -> None:
        self._pedidos: list[Pedido] = []

    def salvar(self, pedido: Pedido) -> None:
        # TODO: guardar o pedido na lista (sem duplicar)
        ...

    def buscar(self, pedido_id: int):
        # TODO: devolver o pedido com esse id (ou None se não achar)
        ...

    def listar(self) -> list:
        # TODO: devolver todos os pedidos guardados
        ...

    def proximo_id(self) -> int:
        # TODO: devolver o próximo id (ex.: quantidade atual + 1)
        ...
