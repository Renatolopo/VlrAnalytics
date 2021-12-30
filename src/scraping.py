import pandas as pd
import lxml

# coletando a tabela com os dados no pandas e exportando em csv
df = pd.read_html('https://www.vlr.gg/stats')
df = df[0]
df.to_csv("../data/stats_vlr.csv")
