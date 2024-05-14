# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:55:39 2024

@author: davir
"""
import pandas as pd
import streamlit as st

df = pd.read_excel('C:/Users/davir/OneDrive/Documentos/Test_Options_02.xls')
select = df.loc[df['Vale a pena'] != '-']

st.write("""# Hunter Options*""")



# # Cria um DataFrame apenas com as puts
# puts = df[df['Tipo'] == 'PUT']

# # Cria um DataFrame apenas com as calls
# calls = df[df['Tipo'] == 'CALL']

# # Realiza um merge entre as calls e as puts correspondentes com strike superior
# result_df = pd.merge(calls, puts, how='inner', on='Empresa', suffixes=('', '_Put'))
# result_df = result_df[result_df['Strike_Put'] > result_df['Strike']]

# # Exclui as linhas em que a coluna 'Empresa' possui os valores 'PETR4', 'ELET6', 'ITUB4' e 'CMIG4'
# #result_df = result_df[~result_df['Empresa'].isin(['PETR4', 'ELET6', 'ITUB4', 'CMIG4'])]

# # Adiciona as colunas Call_Compra, Venda_Put e Compra_Put
# result_df['Call_Compra'] = result_df['Bid']
# result_df['Venda_Put'] = result_df.apply(lambda row: puts[(puts['Empresa'] == row['Empresa']) & (puts['Strike'] == row['Strike'])]['Ask'].values[0] if not puts[(puts['Empresa'] == row['Empresa']) & (puts['Strike'] == row['Strike'])].empty else None, axis=1)
# result_df['Compra_Put'] = result_df['Bid_Put']

# #result_df['Compra_Put'] = result_df.apply(lambda row: puts[(puts['Empresa'] == row['Empresa']) & (puts['Strike'] > row['Strike'])]['Bid'].values[0] if not puts[(puts['Empresa'] == row['Empresa']) & (puts['Strike'] > row['Strike'])].empty else None, axis=1)

# # Exclui as linhas em que qualquer uma das colunas 'Call_Compra', 'Venda_Put' ou 'Compra_Put' seja igual a 0, NaN ou None
# result_df = result_df[~result_df[['Call_Compra', 'Venda_Put', 'Compra_Put']].apply(lambda x: (x == 0) | pd.isnull(x)).any(axis=1)]

# # Exclui as colunas desnecessárias e renomeia a coluna de Strike da Put
# result_df = result_df[['Opcao', 'Data', 'Empresa', 'Ask', 'Bid', 'Strike', 'Tipo', 'Ult', 'Strike_Put', 'Call_Compra', 'Venda_Put', 'Compra_Put']]
# result_df = result_df.rename(columns={'Strike_Put': 'Strike_Put_superior'})

# #Calculando o Resultado Final
# result_df['Result'] = -result_df['Call_Compra'] - result_df['Compra_Put'] + result_df['Venda_Put'] + (result_df['Strike_Put_superior'] - result_df['Strike'])

# # Adiciona a coluna '% Lucro' com o cálculo especificado
# result_df['% Lucro'] = result_df['Result'] / (result_df['Compra_Put'] + result_df['Call_Compra'] - result_df['Venda_Put'])

# # Ordena o DataFrame result_df pela coluna 'Result' de forma decrescente
# result_df = result_df.sort_values(by='% Lucro', ascending=False)

# result_df.to_excel('resultado.xlsx')
