from finances.client import Client
from finances.account import Account
from finances.investment import Investment
from datetime import datetime, timedelta

# Constantes para os testes
DEFAULT_CLIENT_NAME = "Cliente Teste"
DEFAULT_ACCOUNT_NAME = "Conta Corrente"
DEFAULT_INVESTMENT_TYPE = "Ações"
DEFAULT_INVESTMENT_AMOUNT = 2000.0
DEFAULT_RATE_OF_RETURN = 0.02  # 2% ao mês

def get_client():
    return Client(DEFAULT_CLIENT_NAME)

def test_client_instance() -> None:
    """ Testa se a classe Client é instanciada corretamente. """
    client = get_client()
    assert isinstance(client, Client), "Falha ao instânciar um objeto do tipo Client."

def test_client_atributes() -> None:
    client = get_client()
    assert client.name == DEFAULT_CLIENT_NAME, "Nome do cliente está incorreto."
    assert type(client.accounts) is list, "Atributo accounts deve ser uma lista."
    assert type(client.investments) is list, "Atributo investments deve ser uma lista."
    assert len(client.accounts) == 0, "A lista de contas deve estar vazia inicialmente."
    assert len(client.investments) == 0, "A lista de investimentos deve estar vazia inicialmente."

def test_add_account() -> None:
    """ Testa o método add_account da classe Client. """
    client = get_client()
    account = client.add_account(DEFAULT_ACCOUNT_NAME)
    assert isinstance(account, Account), "O método não retornou uma instância de Account."
    assert account.name == DEFAULT_ACCOUNT_NAME, "O nome da conta criada está incorreto."
    assert len(client.accounts) == 1, "A conta não foi adicionada corretamente à lista do cliente."
    assert client.accounts[0] == account, "A conta adicionada não está corretamente associada ao cliente."

def test_add_investment() -> None:
    """ Testa o método add_investment da classe Client. """
    client = get_client()
    investment = Investment(DEFAULT_INVESTMENT_TYPE, DEFAULT_INVESTMENT_AMOUNT, DEFAULT_RATE_OF_RETURN, client)
    client.add_investment(investment)
    assert len(client.investments) == 1, "O investimento não foi adicionado corretamente à lista do cliente."
    assert client.investments[0] == investment, "O investimento adicionado não está corretamente associado ao cliente."

def test_get_net_worth() -> None:
    """ Testa o método get_net_worth da classe Client. """
    client = get_client()
    account = client.add_account(DEFAULT_ACCOUNT_NAME)
    account.add_transaction(1000.0, 1, "Depósito inicial")
    
    investment = Investment(DEFAULT_INVESTMENT_TYPE, DEFAULT_INVESTMENT_AMOUNT, DEFAULT_RATE_OF_RETURN, client)
    investment.date_purchased = datetime.now() - timedelta(days=60)
    client.add_investment(investment)

    expected_net_worth = account.balance + investment.calculate_value()
    assert abs(client.get_net_worth() - expected_net_worth) < 0.01, "Patrimônio líquido calculado incorretamente."
