import fundamentus
dfraw = fundamentus.get_resultado_raw()
dfraw
print(dfraw.columns)

df = fundamentus.get_resultado()
df
print(df.columns)


# 'Cotação', 'P/L', 'P/VP', 'PSR', 'Div.Yield', 'P/Ativo', 'P/Cap.Giro',
#       'P/EBIT', 'P/Ativ Circ.Liq', 'EV/EBIT', 'EV/EBITDA', 'Mrg Ebit',
#       'Mrg. Líq.', 'Liq. Corr.', 'ROIC', 'ROE', 'Liq.2meses', 'Patrim. Líq',
#       'Dív.Brut/ Patrim.', 'Cresc. Rec.5a'],
# 'cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl',
#       'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe', 'liqc',
#       'liq2m', 'patrliq', 'divbpatr', 'c5y'

# Escolher a ação pelo código do ticker
ticker = 'PETR4'  # Exemplo para Petrobras PN (alterar para a ação desejada)

# Filtrar os dados para obter apenas os dados da ação específica
acao_dados = df[df.index == ticker]  # Usa o índice (que é o ticker) para filtrar

# Exibe os dados da ação específica
print(acao_dados)

# Para acessar uma coluna específica, por exemplo, o "P/L" (Price-to-Earnings ratio)
pl = acao_dados['pl']  # Nome da coluna de P/L (pode mudar dependendo do DataFrame)
print(f"P/L da {ticker}: {pl.values[0]}")  # Acessa o valor de P/L da ação específica

