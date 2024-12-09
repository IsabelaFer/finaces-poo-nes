from datetime import datetime

class Investment:
    def __init__(self, type: int, amount: float, rate_of_return: float, client: "Client") -> None:
        """
        Inicializa uma instância de Investment.

        Args:
            type (int)): Identificador do tipo de investimento.
            amount (float): Valor inicial do investimento.
            rate_of_return (float): Taxa mensal de retorno.
        """
        self.type = type
        self.initial_amount = amount
        self.date_purchased = datetime.now()
        self.rate_of_return = rate_of_return
        self.client = client

    def calculate_value(self) -> float:
        """
        Calcula o valor atual do investimento com base na taxa de retorno mensal.

        Returns:
            float: O valor atual do investimento.
        """
        # Número de meses completos desde a compra
        now = datetime.now()
        months = (now.year - self.date_purchased.year)*12 + (now.month - self.date_purchased.month)
        # Juros compostos aplicados mensalmente
        current_value = self.initial_amount * ((1 + self.rate_of_return) ** months)
        return current_value

    def sell(self, account: "Account") -> None:
        """
        Vende o investimento e deposita o valor atual em uma conta.

        Args:
            account (Account): Conta onde o valor será depositado.
        """
        current_value = self.calculate_value()
        account.add_transaction(current_value, category=3, description=f"Venda do investimento: {self.type}")
