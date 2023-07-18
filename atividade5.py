#Preciso definir a compra de um produto, pelo mais caro
produtos = {
'produto1' : 45.99,
'produto2' : 48.99,
'produto3' : 49.99,
'produto4' : 41.95,
'produto5' : 40.00,
'produto6' : 35.59
}

produto_mais_caro = max(produtos, key=produtos.get)
preco_mais_caro = produtos[produto_mais_caro]

print(f"O recomendado é comprar o {produto_mais_caro} que custa R$ {preco_mais_caro:.2f}")