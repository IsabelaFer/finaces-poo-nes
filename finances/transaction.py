from datetime import datetime

CATEGORIES: int = {
    1: "Pagamento", 
    2: "Deposito",
    3: "Transferência"
}

class Transaction:
    """ Classe para representar transações financeiras. """
    def __init__(self, amount: float, category: int, description: str = "") -> None:
        """
        Inicializa uma instância de Transaction.

        Args:
            amount (float): Valor da transação.
            category (int): Identificador da categoria (deve estar em `CATEGORIES`).
            description (str, opcional): Descrição da transação. Default é "".

        Raises:
            ValueError: Se a categoria não for válida.
        """
        if category not in CATEGORIES.keys():
            raise ValueError("Categoria inválida.")
        self.amount = amount
        self.date = datetime.now()
        self.category = category
        self.description = description

    def __str__(self) -> str:
        """
        Retorna uma representação textual da transação.

        Returns:
            str: Representação formatada da transação.
        """
        return f"Transação: {self.description} R$ {self.amount:.2f} ({CATEGORIES[self.category]})"

    def update(
        self,
        amount: float | None = None,
        category: int | None = None,
        description: str | None = None,
        date: datetime | None = None
    ) -> None:
        """
        Atualiza os atributos da transação.

        Args:
            amount (float, opcional): Novo valor da transação.
            category (int, opcional): Nova categoria da transação.
            description (str, opcional): Nova descrição da transação.
            date (datetime, opcional): Nova data da transação.

        Raises:
            ValueError: Se a nova categoria for inválida.
        """
        if amount is not None:
            self.amount = amount
        if category is not None:
            if category not in CATEGORIES.keys():
                raise ValueError("Categoria inválida.")
            self.category = category
        if description is not None:
            self.description = description
        if date is not None:
            self.date = date
