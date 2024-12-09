from finances.account import Account

class Client:
    def __init__(self, name: str) -> None:
        """
        Inicializa uma instância de Client.

        Args:
            name (str): Nome do cliente.
        """
        self.name = name
        self.accounts = []
        self.investments = []

    def add_account(self, account_name: str) -> "Account":
        """
        Cria uma nova conta associada ao cliente.

        Args:
            account_name (str): Nome da nova conta.

        Returns:
            Account: A conta criada.
        """
        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: "Investment") -> None:
        """
        Adiciona um investimento ao cliente.

        Args:
            investment (Investment): O investimento a ser adicionado.
        """
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        """
        Calcula a soma do valor atual de todas as contas e investimentos do cliente.

        Returns:
            float: O patrimônio líquido total do cliente.
        """
        accounts_balance = sum(account.balance for account in self.accounts)
        investments_value = sum(investment.calculate_value() for investment in self.investments)
        return accounts_balance + investments_value
