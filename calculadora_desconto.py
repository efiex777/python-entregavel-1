preco = float(input("Preco do produto: "))
percentual_desconto = float(input("Percentual de desconto: "))

preco_final = preco * (1 - percentual_desconto / 100)

print(f"Preco final: R$ {preco_final:.2f}")
