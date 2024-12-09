from finances.account import Account
from finances.transaction import Transaction
from datetime import datetime, timedelta

# Constantes para os testes
DEFAULT_ACCOUNT_NAME = "Conta Teste"
DEFAULT_AMOUNT = 100.0
DEFAULT_CATEGORY = 1
DEFAULT_DESCRIPTION = "Descrição de teste"

def get_account():
    """
    Cria uma conta padrão para ser usada nos testes.

    Returns:
        Account: Uma instância de Account com valores padrão.
    """
    return Account(DEFAULT_ACCOUNT_NAME)

def test_account_instance() -> None:
    """ Testa se a classe Account instancia corretamente. """
    conta = get_account()
    assert isinstance(conta, Account), "Falha ao instânciar um objeto Account."

def test_account_atributes() -> None:
    """ Testa os atributos de uma instância de Account. """
    conta = get_account()
    # Testa os tipos
    assert type(conta.name) is str, "Tipo incorreto para o nome da conta."
    assert type(conta.balance) is float, "Tipo incorreto para o saldo da conta."
    assert type(conta.transactions) is list, "Tipo incorreto para transações."
    # Testa os valores
    assert conta.name == DEFAULT_ACCOUNT_NAME, "Valor incorreto para o nome da conta."
    assert conta.balance == 0.0, "Valor incorreto para o saldo (inicialmente deve ser 0.)."
    assert len(conta.transactions) == 0, "Valor incorreto para a quantidade de transações (inicialmente deve ser 0)."

def test_add_transaction() -> None:
    """ Testa se adicionar uma transação atualiza corretamente a conta. """
    conta = get_account()
    transaction = conta.add_transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)
    assert isinstance(transaction, Transaction), "O método não retornou uma instância de Transaction."
    assert len(conta.transactions) == 1, "A transação não foi adicionada à conta."
    assert conta.balance == DEFAULT_AMOUNT, "O saldo da conta não foi atualizado corretamente."

def test_get_transactions() -> None:
    """
    Testa o método get_transactions da classe Account.
    Verifica:
        1. Se retorna todas as transações sem filtros.
        2. Se filtra por data corretamente.
        3. Se filtra por categoria corretamente.
    """
    conta = get_account()
    # Adiciona transações
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    conta.add_transaction(100.0, 1, "Hoje")
    conta.add_transaction(200.0, 2, "Ontem", date=yesterday)
    conta.add_transaction(300.0, 1, "Categoria 1")
    # Testa sem filtros
    transactions = conta.get_transactions()
    assert len(transactions) == 3, "Deve retornar todas as transações sem filtros."
    # Testa filtro por data
    transactions_today = conta.get_transactions(start_date=today)
    assert len(transactions_today) == 1, "Filtro por data inicial não funcionou corretamente."
    assert transactions_today[0].description == "Hoje", "Transação de hoje não foi encontrada."
    # Testa filtro por categoria
    transactions_category = conta.get_transactions(category=1)
    assert len(transactions_category) == 2, "Filtro por categoria não funcionou corretamente."
    assert all(tr.category == 1 for tr in transactions_category), "Categorias retornadas estão incorretas."

