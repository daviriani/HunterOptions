# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:55:39 2024

@author: davir
"""
import pandas as pd
import streamlit as st

df = pd.read_excel('Test_Options_02.xls')
select = df.loc[df['Vale a pena'] != '-']

st.write("""# Hunter Options*""")



