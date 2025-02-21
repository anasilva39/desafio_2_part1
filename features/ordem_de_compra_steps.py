from behave import given, then
from features.impl.ordem_de_compra import OrdemDeCompra

ordem_de_compra = OrdemDeCompra()

@given(u'que o usuário selecionou o animal desejado na petstore')
def step_impl(context):
    # Implementação do step
    ordem_de_compra.id = 1
    ordem_de_compra.petId = 1
    ordem_de_compra.quantidade = 1
    response = ordem_de_compra.post_criar_uma_nova_ordem()
    context.response = response
    print("Usuário selecionou o animal desejado na petstore")

@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente')
def step_impl(context):
    # Implementação do step
    detalhes_ordem = ordem_de_compra.get_detalhes_ordem()
    assert detalhes_ordem["id"] == ordem_de_compra.id
    assert detalhes_ordem["petId"] == ordem_de_compra.petId
    assert detalhes_ordem["quantity"] == ordem_de_compra.quantidade
    print("O sistema validou se a ordem de pedido foi armazenada corretamente")
