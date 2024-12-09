from finances.investment import Investment
from finances.account import Account
from finances.client import Client
from datetime import datetime, timedelta

# Constantes para os testes
DEFAULT_TYPE = "Ações"
DEFAULT_AMOUNT = 1000.0
DEFAULT_RATE_OF_RETURN = 0.02
DEFAULT_DATE_PURCHASED = datetime.now() - timedelta(days=60)

def get_investment():
    client = Client("Cliente Teste")
    return Investment(DEFAULT_TYPE, DEFAULT_AMOUNT, DEFAULT_RATE_OF_RETURN, client)

def test_investment_instance() -> None:
    """ Testa se a classe Investment instancia corretamente. """
    investment = get_investment()
    assert isinstance(investment, Investment), "Falha ao instânciar um objetodo tipo Investment."

def test_investment_atributes() -> None:
    """ Testa os atributos de uma instância de Investment. """
    investment = get_investment()
    assert investment.type == DEFAULT_TYPE, "Tipo do investimento está incorreto."
    assert investment.initial_amount == DEFAULT_AMOUNT, "Valor inicial está incorreto."
    assert investment.rate_of_return == DEFAULT_RATE_OF_RETURN, "Taxa de retorno está incorreta."
    assert investment.client == client, "Cliente associado ao investimento está incorreto."

def test_calculate_value() -> None:
    """ Testa o cálculo do valor atual do investimento. """
    investment = get_investment()
    investment.date_purchased = DEFAULT_DATE_PURCHASED  # Data fixa para o teste
    expected_value = DEFAULT_AMOUNT * (1 + DEFAULT_RATE_OF_RETURN) ** 2
    calculated_value = investment.calculate_value()
    assert abs(calculated_value - expected_value) < 0.01, f"Valor calculado incorreto: {calculated_value}"

def test_sell_investment() -> None:
    """ Testa o método de venda do investimento.  """
    account = Account("Conta Teste")
    investment = get_investment()
    investment.date_purchased = DEFAULT_DATE_PURCHASED  # Data fixa para o teste

    expected_value = investment.calculate_value()
    investment.sell(account)

    assert account.balance == expected_value, "Saldo da conta não foi atualizado corretamente após a venda."
    assert len(account.transactions) == 1, "A transação da venda não foi registrada."
    assert account.transactions[0].amount == expected_value, "Valor da transação está incorreto."
