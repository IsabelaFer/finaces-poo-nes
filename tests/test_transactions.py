from finances.transaction import Transaction, CATEGORIES
from datetime import datetime

# Constantes para testes
DEFAULT_AMOUNT = 100.0
DEFAULT_CATEGORY = 1
DEFAULT_DESCRIPTION = "Transação de teste"

def get_transaction() -> Transaction:
    """
    Cria uma transação padrão para ser usada nos testes.

    Returns:
        Transaction: Uma instância de Transaction com valores padrão.
    """
    return Transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)

def test_transaction_instance() -> None:
    """ Testa se a classe Transaction instancia corretamente. """
    tr = get_transaction()
    assert isinstance(tr, Transaction), "Falha ao instanciar um objeto Transaction"

def test_transaction_atributes() -> None:
    """ Testa os atributos de uma instancia de Transaction. """
    tr = get_transaction()
    # Checa os tipos
    assert type(tr.amount) is float, "Tipo incorreto para o valor."
    assert type(tr.date) is datetime, "Tipo incorreto para a data."
    assert type(tr.category) is int, "Tipo incorreto para a categoria."
    assert type(tr.description) is str, "Tipo incorreto para a descrição."
    # Checa os valores
    assert tr.amount == DEFAULT_AMOUNT, "Valor incorreto."
    assert tr.category == DEFAULT_CATEGORY, "Valor incorreto para categoria."
    assert tr.description == DEFAULT_DESCRIPTION, "Valor incorreto para descrição."

def test_transaction_cat() -> None:
    """ Testa se a transação é válida. """
    tr = get_transaction()
    assert tr.category in CATEGORIES.keys(), "Categoria inválida."

def test_transaction_update():
    """ Testa se os atributos da transação podem ser atualizados. """
    tr = get_transaction()
    tr.update(amount=200.0)
    assert tr.amount == 200.0, "Falha ao atualizar o valor."
    new_date = datetime.now()
    tr.update(date=new_date)
    assert tr.date == new_date, "Falha ao atualizar a data."
    tr.update(category=2)
    assert tr.category == 2, "Falha ao atualizar a categoria."
    tr.update(description="Teste")
    assert tr.description == "Teste", "Falha ao atualizar a descrição."

def test_transaction_representation():
    """ Testa a representação textual da transação. """
    tr = get_transaction()
    expected = f"Transação: {DEFAULT_DESCRIPTION} R$ {DEFAULT_AMOUNT:.2f} ({CATEGORIES[DEFAULT_CATEGORY]})"
    assert str(tr) == expected, "Representação fora do formato esperado."
