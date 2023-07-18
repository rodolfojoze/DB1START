#Preciso definir a compra de um produto, pelo mais barato
produtos = {
'produto1' : 45.99,
'produto2' : 48.99,
'produto3' : 49.99,
'produto4' : 41.95,
'produto5' : 40.00,
'produto6' : 35.59
}

produto_mais_barato = min(produtos, key=produtos.get)
preco_mais_barato = produtos[produto_mais_barato]

print(f"O recomendado é comprar o {produto_mais_barato} que custa R$ {preco_mais_barato:.2f}")