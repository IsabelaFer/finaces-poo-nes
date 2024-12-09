from finances.transaction import Transaction
from datetime import datetime

class Account:
    def __init__(self, name: str) -> None:
        """
        Inicializa uma instância de Account.

        Args:
            name (str): Nome da conta.
        """
        self.name = name
        self.balance = 0.0
        self.transactions = []

    def add_transaction(self, amount: float, category: int, description: str = "") -> Transaction:
        """
        Cria uma nova transação e atualiza o saldo da conta.

        Args:
            amount (float): Valor da transação.
            category (int): Identificador da categoria.
            description (str, opcional): Descrição da transação.

        Returns:
            Transaction: A transação criada.

        Raises:
            ValueError: Se a categoria não for válida.
        """
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.balance += amount
        return transaction

    def get_transactions(self, start_date: datetime = None, end_date: datetime = None, category: int = None):
        """
        Gera uma lista de transações filtradas por data e/ou categoria.

        Args:
            start_date (datetime, opcional): Data inicial para o filtro.
            end_date (datetime, opcional): Data final para o filtro.
            category (int, opcional): Categoria para o filtro.

        Returns:
            List[Transaction]: Lista de transações filtradas.
        """
        filtered_transactions = self.transactions

        if start_date:
            filtered_transactions = [t for t in filtered_transactions if t.date >= start_date]

        if end_date:
            filtered_transactions = [t for t in filtered_transactions if t.date <= end_date]

        if category is not None:
            filtered_transactions = [t for t in filtered_transactions if t.category == category]

        return filtered_transactions
