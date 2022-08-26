valor_emprestimo = float(input("Informe o valor do empréstimo:R$"))
num_parcelas = int(input("Informe o número de parcelas por favor:"))
juros = valor_emprestimo * 20 / 100
valor_tot_juros = valor_emprestimo + juros
print(f"O valor total do empréstimo + juros de 20% é de R${valor_tot_juros:.2f}")
tot_parcela_juros = valor_tot_juros / num_parcelas
print(f"Cada parcela será de R${tot_parcela_juros:.2f} ")